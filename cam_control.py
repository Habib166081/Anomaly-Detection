import numpy as np
from pyueye import ueye

class Camera:
    def __init__(self, cam_num):
        self.cam_num = cam_num
        self.last_frame = np.zeros((1,1))
        
        # x_i = 0#int(1280/4)
        # y_i = 0#int(1024/4)
        # self.width = 224
        # self.height = 224
        
         
        #---------------------------------------------------------------------------------------------------------------------------------------
        print("START")
        print()   
            
        
        self.h_cam = ueye.HIDS(self.cam_num)
        
        ret = ueye.is_InitCamera(self.h_cam, None)
        if ret != ueye.IS_SUCCESS:
            print('ERROR: NO Camera Available')
            
        cInfo = ueye.CAMINFO()
        nRet = ueye.is_GetCameraInfo(self.h_cam, cInfo)
        if nRet != ueye.IS_SUCCESS:
            print("is_GetCameraInfo ERROR")
        
        sInfo = ueye.SENSORINFO()
        nRet = ueye.is_GetSensorInfo(self.h_cam, sInfo)
        if nRet != ueye.IS_SUCCESS:
            print("is_GetSensorInfo ERROR")
            
        self.width = 1024
        self.height = 1024
        x_i = int(sInfo.nMaxWidth)//2 - self.width//2
        y_i = int(sInfo.nMaxHeight)//2 - self.height//2
        
        pixRate = ueye.UINT(118)
        ueye.is_PixelClock(self.h_cam, ueye.IS_PIXELCLOCK_CMD_SET, pixRate, ueye.sizeof(pixRate))
                
        newFPS = ueye.double(10)
        nRet = ueye.is_SetFrameRate(self.h_cam, newFPS, newFPS)
        if nRet != ueye.IS_SUCCESS:
            print("is_SetFrameRate ERROR")

#        nRet = ueye.is_ResetToDefault(self.h_cam)
#        if nRet != ueye.IS_SUCCESS:
#            print("is_ResetToDefault ERROR")
            
        #nRet = ueye.is_SetDisplayMode(self.h_cam, ueye.IS_SET_DM_DIB)
        
#        ret = ueye.is_SetColorMode(self.h_cam, ueye.IS_CM_BGR8_PACKED)
#        if ret != ueye.IS_SUCCESS:
#            print('ERROR: Cannot Set Color Mode')
        
        rect_aoi = ueye.IS_RECT()
        rect_aoi.s32X = ueye.int(x_i)
        rect_aoi.s32Y = ueye.int(y_i)
        rect_aoi.s32Width = ueye.int(self.width) 
        rect_aoi.s32Height = ueye.int(self.height) 
        ueye.is_AOI(self.h_cam, ueye.IS_AOI_IMAGE_SET_AOI, rect_aoi, ueye.sizeof(rect_aoi))
        
        self.bpp = self.get_bits_per_pixel(ueye.is_SetColorMode(self.h_cam, ueye.IS_GET_COLOR_MODE))
        
        self.nBitsPerPixel = ueye.INT(self.bpp)
        
        self.pcImageMemory = ueye.c_mem_p()
        self.MemID = ueye.int()
        self.pitch = ueye.INT()
        
        rectAOI = ueye.IS_RECT()
        nRet = ueye.is_AOI(self.h_cam, ueye.IS_AOI_IMAGE_GET_AOI, rectAOI, ueye.sizeof(rectAOI))
        if nRet != ueye.IS_SUCCESS:
            print("is_AOI ERROR")
        
        self.width_ueye = rectAOI.s32Width
        self.height_ueye = rectAOI.s32Height
        
        print(rectAOI.s32Width)
        print(rectAOI.s32Height)

    def initialize(self):
        
        #---------------------------------------------------------------------------------------------------------------------------------------
        
        # Allocates an image memory for an image having its dimensions defined by width and height and its color depth defined by nBitsPerPixel
        nRet = ueye.is_AllocImageMem(self.h_cam, self.width_ueye, self.height_ueye, self.nBitsPerPixel, self.pcImageMemory, self.MemID)
        if nRet != ueye.IS_SUCCESS:
            print("is_AllocImageMem ERROR")
        else:
            # Makes the specified image memory the active memory
            nRet = ueye.is_SetImageMem(self.h_cam, self.pcImageMemory, self.MemID)
            if nRet != ueye.IS_SUCCESS:
                print("is_SetImageMem ERROR")
            else:
                # Set the desired color mode
                nRet = ueye.is_SetColorMode(self.h_cam, ueye.IS_CM_BGR8_PACKED)
        
        
        # Activates the camera's live video mode (free run mode)
        nRet = ueye.is_CaptureVideo(self.h_cam, ueye.IS_DONT_WAIT)
        if nRet != ueye.IS_SUCCESS:
            print("is_CaptureVideo ERROR")
        
        # Enables the queue mode for existing image memory sequences
        nRet = ueye.is_InquireImageMem(self.h_cam, self.pcImageMemory, self.MemID, self.width_ueye, self.height_ueye, self.nBitsPerPixel, self.pitch)
        if nRet != ueye.IS_SUCCESS:
            print("is_InquireImageMem ERROR")
            return False
        else:
            print("Cam is ready")
            return True
        
        #---------------------------------------------------------------------------------------------------------------------------------------

    def get_frame(self):
        array = ueye.get_data(self.pcImageMemory, self.width_ueye, self.height_ueye, self.nBitsPerPixel, self.pitch, copy=False)
        self.last_frame = np.reshape(array,(self.height, self.width, int(self.bpp / 8)))
        return self.last_frame

    def acquire_movie(self, num_frames):
        movie = []
        for _ in range(num_frames):
            movie.append(self.get_frame())
        return movie

#    def set_brightness(self, value):
#        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, value)
#
#    def get_brightness(self):
#        return self.cap.get(cv2.CAP_PROP_BRIGHTNESS)

    def close_camera(self):
        ueye.is_FreeImageMem(self.h_cam, self.pcImageMemory, self.MemID)
        ueye.is_ExitCamera(self.h_cam)

    def __str__(self):
        return 'OpenCV Camera {}'.format(self.cam_num)
    
    def get_bits_per_pixel(self, color_mode):
        """
        returns the number of bits per pixel for the given color mode
        raises exception if color mode is not is not in dict
        """
        
        return {
            ueye.IS_CM_SENSOR_RAW8: 8,
            ueye.IS_CM_SENSOR_RAW10: 16,
            ueye.IS_CM_SENSOR_RAW12: 16,
            ueye.IS_CM_SENSOR_RAW16: 16,
            ueye.IS_CM_MONO8: 8,
            ueye.IS_CM_RGB8_PACKED: 24,
            ueye.IS_CM_BGR8_PACKED: 24,
            ueye.IS_CM_RGBA8_PACKED: 32,
            ueye.IS_CM_BGRA8_PACKED: 32,
            ueye.IS_CM_BGR10_PACKED: 32,
            ueye.IS_CM_RGB10_PACKED: 32,
            ueye.IS_CM_BGRA12_UNPACKED: 64,
            ueye.IS_CM_BGR12_UNPACKED: 48,
            ueye.IS_CM_BGRY8_PACKED: 32,
            ueye.IS_CM_BGR565_PACKED: 16,
            ueye.IS_CM_BGR5_PACKED: 16,
            ueye.IS_CM_UYVY_PACKED: 16,
            ueye.IS_CM_UYVY_MONO_PACKED: 16,
            ueye.IS_CM_UYVY_BAYER_PACKED: 16,
            ueye.IS_CM_CBYCRY_PACKED: 16,        
        } [color_mode]


if __name__ == '__main__':
#    cam = Camera(0)
#    cam.initialize()
#    print(cam)
#    frame = cam.get_frame()
#    print(frame)
#    cam.set_brightness(1)
#    print(cam.get_brightness())
#    cam.set_brightness(0.5)
#    print(cam.get_brightness())
#    cam.close_camera()
    
    print('aa')