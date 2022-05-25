from PyQt5.QtWidgets import QApplication
import sys
from cam_control import Camera
from MainWindow import StartWindow
import os
from PyQt5.QtGui import  QIcon

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

camera = Camera(0)
cam_status = camera.initialize()


app = QApplication.instance() # checks if QApplication already exists 
if not app: # create QApplication if it doesnt exist 
    app = QApplication([])
app.setStyle('Fusion')
start_window = StartWindow(camera, cam_status)
start_window.setWindowIcon(QIcon("images/Logo_mini.png"))
start_window.show()
start_window.activateWindow()
start_window.raise_()
sys.exit(app.exec_())
                              





