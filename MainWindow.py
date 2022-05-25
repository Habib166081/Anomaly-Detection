# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 12:39:51 2022

@author: boukrana
"""

from bibliotheque import *

from WorkerTrain_DL import Worker
from Movie import MovieThread
from WorkerTrain_DL_Expert import Worker_Expert






class StartWindow(qtw.QMainWindow,Ui_MainWindow):
    train_signal = pyqtSignal(dict,torch.Tensor)
    train_signal_expert = pyqtSignal(dict,torch.Tensor)
    signal_model  = pyqtSignal(str)
    def __init__(self, camera = None, cam_status = False):
        super(StartWindow, self).__init__()
        self.setupUi(self)
        self.camera = camera
        self.cam_status = cam_status
                
        self.frame = None
        
        self.is_trained = False
        
        self.use_cuda = torch.cuda.is_available()
        self.device = torch.device('cuda' if self.use_cuda else 'cpu')
        self.updateTime()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.value_mask=0.77
##############################################################################################



        
        exp_min = ueye.DOUBLE()
        exp_max = ueye.DOUBLE()
        exp_inc = ueye.DOUBLE()
        exp_curr = ueye.DOUBLE()
        ueye.is_Exposure(self.camera.h_cam, ueye.IS_EXPOSURE_CMD_GET_EXPOSURE_RANGE_MIN, exp_min, ueye.sizeof(exp_min))
        ueye.is_Exposure(self.camera.h_cam, ueye.IS_EXPOSURE_CMD_GET_EXPOSURE_RANGE_MAX, exp_max, ueye.sizeof(exp_max))
        ueye.is_Exposure(self.camera.h_cam, ueye.IS_EXPOSURE_CMD_GET_EXPOSURE_RANGE_INC, exp_inc, ueye.sizeof(exp_inc))
        ueye.is_Exposure(self.camera.h_cam, ueye.IS_EXPOSURE_CMD_GET_EXPOSURE, exp_curr, ueye.sizeof(exp_curr))
        
        
        self.button_frame.clicked.connect(self.update_image)
        self.button_movie.clicked[bool].connect(self.start_stop_movie)
        self.button_movie.setCheckable(True)

        self.slider_exposure_time.setRange(int(exp_min*1000),int(exp_max*1000))
        self.slider_exposure_time.setValue(int(exp_curr*1000))
        self.slider_exposure_time.setTickPosition(QSlider.TicksBelow)
        self.slider_exposure_time.setTickInterval(int(exp_inc*1000))
        self.slider_exposure_label.setText(str(int(exp_curr*1000)/1000))
        self.slider_exposure_time.valueChanged.connect(self.update_exposure_time)
        
        self.cursor_mask.valueChanged.connect(self.updateCursor_mask)
        

##############################################################################################
    
        
        self.test_types = ['Test', 'Conf', 'Def']
        self.test_colors = ['blue', 'green', 'red']        
        
        

        test_cb_model = self.test_combo.model()
        for ind in range(len(self.test_types)):
            cb_item = QStandardItem(self.test_types[ind])
            cb_item.setBackground(QColor(self.test_colors[ind]))
            test_cb_model.appendRow(cb_item)
        #self.test_combo.setStyleSheet("QComboBox{{ background-color: {}}}".format('blue'))
        
        self.test_combo.setDisabled(True)
        
        self.test_type_index = 0        
##############################################################################################        
         
         
        self.worker = Worker()
        self.worker_thread = QThread(parent=self)
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()
        
        self.train_signal.connect(self.worker.train_DL)
        self.worker.message.connect(self.message)
        self.worker.SigInfo.connect(self.InfoWorker)
        self.worker.progress.connect(self.progressBar)
##############################################################################################          
        
        
        self.button_Train.clicked.connect(self.class_train)
        self.button_addTrain.clicked.connect(self.add_Train)
        self.test_combo.currentIndexChanged.connect(self.change_test_type)        
        
##############################################################################################




        self.hist_plot.canvas.mpl_connect("button_press_event", self.on_press)  
        
##############################################################################################        
        
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_movie)
        
        
        self.outputs = []
        self.embedding_net()
        
        self.test_transforms = T.Compose([T.Resize(224, Image.ANTIALIAS), T.ToTensor()])
        self.train_inputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', [])])
        
        self.hist_vals_test = []
        self.hist_vals_conf = []
        self.hist_vals_def = []
        
        self.norm_val = 0
        
        
##############################################################################################        
        box = self.hist_plot.canvas.axes.get_position()
        self.hist_plot.canvas.axes.set_position([box.x0*0.5, box.y0, box.width , box.height])
        self.DesignePlot()
        self.Restart.clicked.connect(self.restart)
        
        
        self.Supp.clicked.connect(self.Delete)
        
        
#################################################################################""
########################## ------------Mode Expert ---------------#####################################################        
       #######################################################################
       
       ## TODO
        self.cwd = os.getcwd()
        
        
        self.start_expert.clicked.connect(self.start_cam)
        self.start_expert.setCheckable(True)
       
        self.update_timer_expert = QTimer()
        self.update_timer_expert.timeout.connect(self.update_movie_expert)
        self.frame_expert = None
        self.stop_expert.setEnabled(False)
        self.is_trained_expert = False
        self.stop_expert.clicked.connect(self.stop_cam)

       

        self.slider_exposure_time_expert.setRange(int(exp_min*1000),int(exp_max*1000))
        self.slider_exposure_time_expert.setValue(int(exp_curr*1000))
        self.slider_exposure_time_expert.setTickPosition(QSlider.TicksBelow)
        self.slider_exposure_time_expert.setTickInterval(int(exp_inc*1000))
        self.slider_exposure_label_expert.setText(str(int(exp_curr*1000)/1000))
        self.slider_exposure_time_expert.valueChanged.connect(self.update_exposure_time_expert)
        
        
        self.fileLoadedPath=""
        self.bouton_parcourir.clicked.connect(self.Path_Acquisition)
        self.SaveImg.clicked.connect(self.Acquisitions)
        self.Supp_Expert.clicked.connect(self.Delete_expert)
        
        
        self.Load_images.clicked.connect(self.LoadImg)
        self.c_directory =''
        
        
        self.train_inputs_exeprt = OrderedDict([('layer1', []), ('layer2', []), ('layer3', [])])
        
        
        #----------Thread---------
                 
        self.worker_expert = Worker_Expert()
        self.worker_thread_expert = QThread(parent=self)
        self.worker_expert.moveToThread(self.worker_thread_expert)
        self.worker_thread_expert.start()
        
        self.train_signal_expert.connect(self.worker_expert.train_DL_expert)
        self.worker_expert.message.connect(self.message_expert)
        self.worker_expert.progress.connect(self.progressBar_Expert)
        
        self.button_Train_expert.clicked.connect(self.class_train_expert)
        self.train_signal_expert.connect(self.worker_expert.train_DL_expert)
        self.bouton_Load_model.clicked.connect(self.LoadModel_signal)
        self.worker_expert.load_model.connect(self.LoadModel)
        
        self.signal_model.connect(self.worker_expert.load)
        
        
        self.cursor_mask_expert.valueChanged.connect(self.updateCursor_mask_expert)
        self.value_mask_expert=0.77
        
        self.bouton_parcourir_test.clicked.connect(self.load_test)
        
        self.dir_test=""
        self.img=None
        self.img_Flag= False
        self.modelFlag=False
        
        
        self.checkBox_test.stateChanged.connect(self.testImg)
        
#####################################################
    def embedding_concat(self, x, y):
        B, C1, H1, W1 = x.size()
        _, C2, H2, W2 = y.size()
        s = int(H1 / H2)
        x = F.unfold(x, kernel_size=s, dilation=1, stride=s)
        x = x.view(B, C1, -1, H2, W2)
        z = torch.zeros(B, C1 + C2, x.size(2), H2, W2)
        for i in range(x.size(2)):
            z[:, :, i, :, :] = torch.cat((x[:, :, i, :, :], y), 1)
        z = z.view(B, -1, H2 * W2)
        z = F.fold(z, kernel_size=s, output_size=(H1, W1), stride=s)
    
        return z

    def hook(self, module, input, output):
        self.outputs.append(output)
    
    def embedding_net(self):

        self.model = resnet18(pretrained=True, progress=True)
        t_d = 448
        d = 100
        # self.model = wide_resnet50_2(pretrained=True, progress=True)
        # t_d = 1792
        # d = 550
        self.model.to(self.device)
        self.model.eval()
        random.seed(1024)
        torch.manual_seed(1024)
        if self.use_cuda:
            torch.cuda.manual_seed_all(1024)
    
        self.idx = torch.tensor(sample(range(0, t_d), d))
    
        self.model.layer1[-1].register_forward_hook(self.hook)
        self.model.layer2[-1].register_forward_hook(self.hook)
        self.model.layer3[-1].register_forward_hook(self.hook)
        


        
        
    def add_Train(self):
        self.is_trained = False
        self.button_addTrain.setEnabled(False)
        self.Apply_AI_image(self.frame, True)
        
        
    def test_DL(self, img):   
        
        
        test_inputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', [])])
            
        img = Image.fromarray(img)
            
        image_tensor = self.test_transforms(img).float()
        image_tensor = image_tensor.unsqueeze_(0)
        
        with torch.no_grad():
            _ = self.model(image_tensor.to(self.device))
        for k, v in zip(test_inputs.keys(), self.outputs):
            test_inputs[k].append(v.cpu().detach())
        self.outputs = []
            
        for k, v in test_inputs.items():
            test_inputs[k] = torch.cat(v, 0)
            
        embedding_vectors = test_inputs['layer1']
        for layer_name in ['layer2', 'layer3']:
            embedding_vectors = self.embedding_concat(embedding_vectors, test_inputs[layer_name])
        
        embedding_vectors = torch.index_select(embedding_vectors, 1, self.idx)
        B, C, H, W = embedding_vectors.size()
        embedding_vectors = embedding_vectors.view(B, C, H * W)
        
        dist_list = []
        for i in range(H * W):
            mean = self.train_outputs[0][:, i]
            conv_inv = self.train_outputs[1][:, :, i]
            dist = [mahalanobis(sample[:, i], mean, conv_inv) for sample in embedding_vectors]
            dist_list.append(dist)
    
        dist_list = np.array(dist_list).transpose(1, 0).reshape(B, H, W)
                
        dist_list = torch.tensor(dist_list)
        self.scores = F.interpolate(dist_list.unsqueeze(1), size=224, mode='bilinear', align_corners=False).squeeze().numpy()
        
    
    #########################################################################################################
    def Apply_AI_image(self, disp_img, add_train = False):
        height, width, channel = disp_img.shape
        
        if not self.is_trained and not self.button_movie.isChecked():
            img = Image.fromarray(disp_img)
            
            image_tensor = self.test_transforms(img).float()
            image_tensor = image_tensor.unsqueeze_(0)
            
            with torch.no_grad():
                _ = self.model(image_tensor.to(self.device))
            for k, v in zip(self.train_inputs.keys(), self.outputs):
                self.train_inputs[k].append(v.cpu().detach())
            self.outputs = []
            
            print(len(self.train_inputs['layer1']))
            self.nb_img_train.setText(str(len(self.train_inputs['layer1'])))
    
            bytesPerLine = 3 * width
            q_frame = QImage(disp_img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            qpixmap_frame = QPixmap.fromImage(q_frame)
            
            #----------------------Save --------------------
            """
            now = datetime.now()
            name_frame = now.strftime("%d-%m-%Y_%Hh%Mm%Ss%f") # nom qui sera donné à l'image enregistrée
            qpixmap_frame.save("N:/P3/STAGIAIRES/habib boukrana/OneClass_APP_Final/Save/image_{}".format(name_frame+".png"))
            """
            ##########################QlistWidget for images######
            prov=QListWidgetItem()
            prov.setSizeHint(QSize(218,218))
            lab = QLabel()
            lab.setGeometry(QRect(0, 30, 218, 218))
            lab.setScaledContents(True)
            frame_resized = qpixmap_frame.scaled(QSize(218,218))
            lab.setPixmap(frame_resized)
            self.listImages.addItem(prov)
            self.listImages.setItemWidget(prov,lab)
            
            
            if add_train:
                self.class_train()

            
        elif self.is_trained :
            self.test_DL(disp_img)
            
            if not self.button_movie.isChecked():
                self.update_hist()
                

            heat_map = self.scores/np.amax(self.scores) * 255
            #--------Mask
            

            
            heat_map = heat_map.astype('uint8')
            heat_map = gaussian_filter(heat_map, sigma=3)
            
            mask = heat_map > (self.value_mask*255)
            print("valeur Mask",self.value_mask)
            heat_map = cv2.applyColorMap(heat_map, cv2.COLORMAP_JET)
            img = cv2.resize(disp_img, dsize=(224, 224))
            heat_map = cv2.addWeighted(heat_map, 0.5, img, 0.5, 0)
            
            self.norm_val = max(self.norm_val, np.amax(self.scores))
            if self.heatmap.isChecked():
                self.score_label.setText(str(round(np.amax(self.scores),2)))
                if round(np.amax(self.scores),2) > round(float(self.thr_AI_val.value()),2):
                    self.score_label.setStyleSheet("color: red;")
                    if self.button_movie.isChecked():
                        cv2.putText(heat_map, 'NOK', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 
                           1, (0,0,255), 1, cv2.LINE_AA)
                else:
                    self.score_label.setStyleSheet("color: green;")
                    if self.button_movie.isChecked():
                        cv2.putText(heat_map, 'OK', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 
                           1, (0,255,0), 1, cv2.LINE_AA)
    
                bytesPerLine = 3 * 224
                self.q_heat = QImage(heat_map.data, 224, 224, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                self.qpixmap_heat = QPixmap.fromImage(self.q_heat)
                self.heatLabel.setPixmap(self.qpixmap_heat)
            
            else:
                self.score_label.setText(str(round(np.amax(self.scores),2)))
                if round(np.amax(self.scores),2) > round(float(self.thr_AI_val.value()),2):
                    self.score_label.setStyleSheet("color: red;")
                    if self.button_movie.isChecked():
                        cv2.putText(img, 'NOK', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 
                           1, (0,0,255), 1, cv2.LINE_AA)
                    vis_img = mark_boundaries(img, mask, color=(0, 0, 1), mode='thick')
                    vis_img = vis_img*255
                    vis_img = vis_img.astype('uint8')
                    bytesPerLine = 3 * 224
                    q_frame = QImage(vis_img, 224, 224, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                    qpixmap_frame = QPixmap.fromImage(q_frame)
                    self.heatLabel.setPixmap(qpixmap_frame)
                else:
                    self.score_label.setStyleSheet("color: green;")
                    if self.button_movie.isChecked():
                        cv2.putText(img, 'OK', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 
                           1, (0,255,0), 1, cv2.LINE_AA)
                    bytesPerLine = 3 * 224
                    q_frame = QImage(img, 224, 224, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                    qpixmap_frame = QPixmap.fromImage(q_frame)
                    self.heatLabel.setPixmap(qpixmap_frame)
            

        bytesPerLine = 3 * width
        self.q_frame = QImage(disp_img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap_frame = QPixmap.fromImage(self.q_frame)
        self.imageLabel.setPixmap(self.qpixmap_frame)
        

        

        
        
    def update_hist(self):
        
        if self.test_type_index == 0:
            self.hist_vals_test.append(np.amax(self.scores))
        elif self.test_type_index == 1:
            self.hist_vals_conf.append(np.amax(self.scores))
        elif self.test_type_index == 2:
            self.hist_vals_def.append(np.amax(self.scores))
        
        
        max_val = np.amax(self.hist_vals_test+self.hist_vals_conf+self.hist_vals_def)
        min_val = np.amin(self.hist_vals_test+self.hist_vals_conf+self.hist_vals_def)
        n = np.arange(min_val, max_val + 1, 1)
        
        self.hist_plot.canvas.axes.clear()
        if len(self.hist_vals_test)>0:
            self.hist_plot.canvas.axes.hist(self.hist_vals_test, bins=n, histtype='barstacked', alpha=0.5, label='Test', color='blue')
        if len(self.hist_vals_conf)>0:
            self.hist_plot.canvas.axes.hist(self.hist_vals_conf, bins=n, histtype='barstacked', alpha=0.5, label='Conf', color='green')
        if len(self.hist_vals_def)>0:
            self.hist_plot.canvas.axes.hist(self.hist_vals_def, bins=n, histtype='barstacked', alpha=0.5, label='Def', color='red')
        self.hist_plot.canvas.axes.legend(bbox_to_anchor=(1.04,0.5), loc="center left", borderaxespad=0,edgecolor="#10191e" , facecolor="#10191e",shadow=True, fontsize='x-large',labelcolor="#4b677a")

        self.hist_plot.canvas.draw()

    def on_press(self, event):
        self.thr_AI_val.setValue(round(event.xdata,2))
        
    def change_test_type(self, i):
        self.test_type_index = i
        self.test_combo.setStyleSheet(" background-color: {}".format(self.test_colors[i]))
            

    def update_image(self):
        if self.button_movie.isChecked():
            self.button_movie.click()
        if self.Nb_acquisition.value()==1:       
            self.frame = self.camera.get_frame()
            self.Apply_AI_image(self.frame)
        else:
            for i in range(self.Nb_acquisition.value()):
                self.progressBarAcqui.setMinimum(0)
                self.progressBarAcqui.setMaximum(self.Nb_acquisition.value())
                self.frame = self.camera.get_frame()
                self.Apply_AI_image(self.frame)
                self.progressBarAcqui.setValue(i+1)
                
        self.progressBarAcqui.setValue(0)
        self.Nb_acquisition.setValue(1)
    
    def update_movie(self):
        self.frame = self.camera.last_frame
        self.Apply_AI_image(self.frame)
        
    def update_exposure_time(self, value):
        exp_val = ueye.double(value/1000)
        ueye.is_Exposure(self.camera.h_cam, ueye.IS_EXPOSURE_CMD_SET_EXPOSURE, exp_val, ueye.sizeof(exp_val))
        self.slider_exposure_label.setText(str(exp_val)[:4])


    def start_stop_movie(self, state):
        if state:
            self.button_movie.setIcon(QIcon('images/Stopp.svg'))
            self.movie_thread = MovieThread(self.camera)
            self.movie_thread.start()
            self.update_timer.start(30)
        else:
            self.button_movie.setIcon(QIcon('images/button_start_stop.png'))
            #self.button_frame.setDisabled(False)
            self.update_timer.stop()
            self.movie_thread.quit()
            #self.update_image()
        
    def close_cam(self):
        self.update_timer.stop()
        if hasattr(self, 'movie_thread'):
            self.movie_thread.quit()
        self.camera.close_camera()
            
                
    def closeEvent(self, event):
        if self.cam_status is True:
            print('Closing Cam')
            self.close_cam()
        print('Closing App')
        self.close()


    def DesignePlot(self):
        self.hist_plot.canvas.axes.spines['right'].set_visible(False)
        self.hist_plot.canvas.axes.spines['top'].set_visible(False)
        self.hist_plot.canvas.axes.spines['bottom'].set_color("white")
        self.hist_plot.canvas.axes.spines['left'].set_color("white")
   
        self.hist_plot.canvas.axes.tick_params(colors='gray', direction='out')
        self.hist_plot.canvas.axes.yaxis.set_tick_params(labelcolor = '#4b677a',color="white", left = True, labelsize = 13)
        self.hist_plot.canvas.axes.xaxis.set_tick_params(labelcolor = '#4b677a',color="white",  labelsize = 13)



    def class_train(self):
        self.worker_thread.start()
        self.train_signal.emit(self.train_inputs,self.idx)
        self.button_Train.setEnabled(False)

    def message(self,tic):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information) 
        msg.setWindowTitle("Training")
        msg.setText("Training is done in " + str(round(time.time()-tic,3)) + ' s !')
        x = msg.exec_()
        self.progressBarEntrain.setValue(0)
        
        
    def InfoWorker(self,thr_AI_val,train_outputs,norm_val,scores):
        self.thr_AI_val.setValue(float(thr_AI_val)) #str(np.amax(mean) + 
        self.train_outputs = train_outputs
        self.button_Train.setEnabled(True)
        self.button_addTrain.setEnabled(True)
        self.test_combo.setDisabled(False)
        self.is_trained = True

        self.test_DL(np.zeros((1024,1024,3), dtype = np.uint8))
        self.norm_val = norm_val
        self.scores=scores
        print(self.norm_val)
        self.movie_thread.quit()
        self.progressBarEntrain.setValue(0)
        
        
    def restart(self):
        self.hist_plot.canvas.axes.clear()
        self.hist_plot.canvas.draw()
        self.heatLabel.clear()
        self.is_trained = False

        self.train_inputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', [])])
        self.score_label.setText("0")
        self.hist_vals_test = []
        self.hist_vals_conf = []
        self.hist_vals_def = []
        self.norm_val = 0
        self.nb_img_train.setText("0")
        self.listImages.clear()

    def progressBar(self,num):
        if num==0:
            for i in range(50):
                self.progressBarEntrain.setValue(i)
        else:        
            for i in range(50,101):
                self.progressBarEntrain.setValue(i)
        
    
    def Delete(self):
        if len(self.train_inputs['layer1']) !=0:
            self.listImages.takeItem(len(self.train_inputs['layer1'])-1)
            for f in self.train_inputs.values():
                f.pop()
            self.nb_img_train.setText(str(len(self.train_inputs['layer1'])))
        else:
            return
    
    ########################  Time############
    def updateTime(self):
        current = QtCore.QDateTime.currentDateTime()
        self.dateEdit.setDate(current.date())
        self.timeEdit.setTime(current.time())        
        
        #############################
        
        
        
    def updateCursor_mask(self,value):
        self.value_mask = value/100
        self.cursor_mask_label.setText(str(self.value_mask))
        
        
        
########################################### -------Expert ------- #####################################################
   ######################################################################################################
          ###############################################################################

    #TODO
    
    def start_movie_expert(self, state=True):
        if state:
            self.start_expert.setEnabled(False)
            self.stop_expert.setEnabled(True)
            self.movie_thread = MovieThread(self.camera)
            self.movie_thread.start()
            self.update_timer_expert.start(30)
        else:
            self.start_expert.setEnabled(True)
            self.stop_expert.setEnabled(False)
            self.update_timer_expert.stop()
            self.movie_thread.quit()
        
    def stop_cam(self):
        self.start_movie_expert(False)
        
    def start_cam(self):
        self.start_movie_expert(True)        
        
        
    def update_movie_expert(self):
        self.frame_expert = self.camera.last_frame
        self.Apply_AI_image_expert(self.frame_expert)
        
        
        
    def update_exposure_time_expert(self, value):
       exp_val = ueye.double(value/1000)
       ueye.is_Exposure(self.camera.h_cam, ueye.IS_EXPOSURE_CMD_SET_EXPOSURE, exp_val, ueye.sizeof(exp_val))
       self.slider_exposure_label_expert.setText(str(exp_val)[:4])       
       
       
       
    def Path_Acquisition(self):
        file = QtWidgets.QFileDialog.getExistingDirectory(self, 'Choisir un Dossier:',f"{self.cwd}")
        self.fileLoadedPath=file
        if self.fileLoadedPath != "" : 
            self.txt_box.setText(file)
            self.fileLoadedPath=file
        else: 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information) 
            msg.setWindowTitle("Rappel")
            msg.setText("Vous n'avez pas choisis de dossier !!")
            x = msg.exec_()

        

        
    def Acquisitions(self):
        if self.fileLoadedPath != '':
            self.frame_expert = self.camera.last_frame
            height, width, channel = self.frame_expert.shape
            
            bytesPerLine = 3 * width
            q_frame = QImage(self.frame_expert.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            qpixmap_frame = QPixmap.fromImage(q_frame)
            now = datetime.now()
            name_frame = now.strftime("%d-%m-%Y_%Hh%Mm%Ss%f") # nom qui sera donné à l'image enregistrée
            # qpixmap_frame.save(self.fileLoadedPath+"/img_{}".format(name_frame+".png"))
            
            im = Image.fromarray(self.frame_expert)
            im.save(self.fileLoadedPath+"/img_{}".format(name_frame+".png"))
            
            i=int(self.nb_img_expert.text())+1
            self.nb_img_expert.setText(str(i))
            
            
            ##########################QlistWidget for images######
            prov=QListWidgetItem()
            prov.setSizeHint(QSize(130,120))
            lab = QLabel()
            lab.setGeometry(QRect(0, 30, 130, 120))
            lab.setScaledContents(True)
            frame_resized = qpixmap_frame.scaled(QSize(130,120))
            lab.setPixmap(frame_resized)
            self.listImages_expert.addItem(prov)
            self.listImages_expert.setItemWidget(prov,lab)

        else: 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information) 
            msg.setWindowTitle("Rappel")
            msg.setText("Vous n'avez pas choisis de dossier !!")
            x = msg.exec_()
        



    def Delete_expert(self):
        if int(self.nb_img_expert.text()) != 0:
            self.listImages_expert.takeItem(int(self.nb_img_expert.text())-1)
            files_path = os.path.join(self.fileLoadedPath, '*.png')
            files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True) 
           
            if os.path.exists(files[0]):
                os.remove(files[0])
            
            self.nb_img_expert.setText(str(int(self.nb_img_expert.text())-1))
        else:
            return
    



    def LoadImg(self):
        self.c_directory = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select your dataset folder:', f'{self.cwd}', QtWidgets.QFileDialog.ShowDirsOnly)
        self.txt_box_images.setText(self.c_directory)   
        if self.c_directory=='':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information) 
            msg.setWindowTitle("Rappel")
            msg.setText("Vous n'avez pas charger les images !!")
            x = msg.exec_()
            return
        else:    
            self.progressBarImages.setStyleSheet('color: rgb(255, 227, 82);')
            self.progressBarImages.setText("Chargement en cours !!")
            files_train = []
            imgs_list = []   
            types = ('*.jpg', '*.jpeg', '*.png', '*.bmp')
            for files in types:
                imgs_list.extend(glob.glob(self.c_directory+'/'+files))
            i=0
            for f in imgs_list:

                img = Image.open(f)
                height, width, channel = np.array(img).shape
                
                image_tensor = self.test_transforms(img).float()
                image_tensor = image_tensor.unsqueeze_(0)
                with torch.no_grad():
                    _ = self.model(image_tensor.to(self.device))
                for k, v in zip(self.train_inputs_exeprt.keys(), self.outputs):
                    self.train_inputs_exeprt[k].append(v.cpu().detach())
                self.outputs = []
                
        
        self.progressBarImages.setStyleSheet('color: #85ff77;')
        self.progressBarImages.setText(" Ok")
        
        
        
    def class_train_expert(self):
        if  self.c_directory !='':
            self.worker_thread_expert.start()
            self.train_signal_expert.emit(self.train_inputs_exeprt,self.idx)
            self.button_Train_expert.setEnabled(False)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information) 
            msg.setWindowTitle("Rappel")
            msg.setText("Vous n'avez pas charger les images !!")
            x = msg.exec_()




    def message_expert(self):
        self.progressBar_expert.setStyleSheet('color: #85ff77;')
        self.progressBar_expert.setText(" Le Modèle est enregistré  ")
        self.Label_Train_expert.setPixmap(QtGui.QPixmap("images/loading_done.png"))
        self.button_Train_expert.setEnabled(True)


    def progressBar_Expert(self):
        self.progressBar_expert.setStyleSheet('color: rgb(255, 227, 82);')
        self.progressBar_expert.setText("Entrainement en cours !!")

        
                
    def LoadModel_signal(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, 'Selectionner votre modele .pkl:', f"{self.cwd}" , filter="(**.pkl)")
        if file[0] != '' : 
            self.signal_model.emit(file[0])
            self.txt_box_load_model.setStyleSheet('color: rgb(255, 227, 82);')
            self.txt_box_load_model.setText("Chargement en cours !!")
            
        else: 
            print("Veuillez sélectionner un fichier")
        
        
    def LoadModel(self,model):
        self.train_inputs_exeprt=model
        self.thr_AI_val_expert.setValue(self.train_inputs_exeprt[2])
        self.Load_Model_expert.setPixmap(QtGui.QPixmap("images/loading_done.png"))
        self.txt_box_load_model.setStyleSheet('color: #85ff77;')
        self.txt_box_load_model.setText(" OK ")
        self.modelFlag=True
    
    
    def updateCursor_mask_expert(self,value):
        self.value_mask_expert = value/100
        self.cursor_mask_label_expert.setText(str(self.value_mask_expert))



    def load_test(self):
        self.dir_test =  QtWidgets.QFileDialog.getOpenFileName(self, 'Selectionner une image :', f"{self.cwd}" , filter="(**.png)")
        if self.dir_test[0] != '' : 
            self.txt_box_test.setText(self.dir_test[0])
            img = Image.open(self.dir_test[0])
            self.img=np.array(img)  
            self.img_Flag=True
        else: 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information) 
            msg.setWindowTitle("Rappel")
            msg.setText("Veuillez sélectionner une image")
            x = msg.exec_()
            return
        


    def testImg(self):
        if (self.test_img.isChecked() and self.img_Flag==False) or (self.live.isChecked() and  self.img_Flag==False):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information) 
            msg.setWindowTitle("Rappel")
            msg.setText("Veuillez : Charger une image !!")
            x = msg.exec_()
            self.checkBox_test.setCheckState(False)
            return
        else:
            #self.start_movie_expert(False)
            self.Apply_AI_image_expert(self.img,True)
        
        
        
        
    def Apply_AI_image_expert(self, disp_img, Flag=False):

        height, width, channel = disp_img.shape
        
        if self.checkBox_test.isChecked() :
            if self.live.isChecked() or Flag==True:
                if self.modelFlag == False:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information) 
                    msg.setWindowTitle("Rappel")
                    msg.setText("Il faut charger un modèle : Dosseir < Model > ")
                    x = msg.exec_()
                    self.checkBox_test.setCheckState(False)
                    return
                else:
                    self.test_DL_expert(disp_img)
                    
                    heat_map = self.scores/np.amax(self.scores) * 255
                    #--------Mask
                    
                    heat_map = heat_map.astype('uint8')
                    heat_map = gaussian_filter(heat_map, sigma=3)
                    
                    mask = heat_map > (self.value_mask_expert*255)
                    heat_map = cv2.applyColorMap(heat_map, cv2.COLORMAP_JET)
                    img = cv2.resize(disp_img, dsize=(224, 224))
                    heat_map = cv2.addWeighted(heat_map, 0.5, img, 0.5, 0)
                    
                    self.norm_val = max(self.norm_val, np.amax(self.scores))
                    if self.heatmap_expert.isChecked():
                        self.score_label_expert.setText(str(round(np.amax(self.scores),2)))
                        if round(np.amax(self.scores),2) > round(float(self.thr_AI_val_expert.value()),2):
                            self.score_label.setStyleSheet("color: red;")
                            cv2.putText(heat_map, 'NOK', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 
                                   1, (0,0,255), 1, cv2.LINE_AA)
                        else:
                            self.score_label_expert.setStyleSheet("color: green;")
                            #if self.button_movie.isChecked():
                            cv2.putText(heat_map, 'OK', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 
                                   1, (0,255,0), 1, cv2.LINE_AA)
                            
                        bytesPerLine = 3 * 224
                        q_heat = QImage(heat_map.data, 224, 224, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                        qpixmap_heat = QPixmap.fromImage(q_heat)
                        self.heatLabel_expert.setPixmap(qpixmap_heat)
                    
                    else:
                        self.score_label.setText(str(round(np.amax(self.scores),2)))
                        if round(np.amax(self.scores),2) > round(float(self.thr_AI_val_expert.value()),2):
                            self.score_label_expert.setStyleSheet("color: red;")
                            cv2.putText(img, 'NOK', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 
                                   1, (0,0,255), 1, cv2.LINE_AA)
                            vis_img = mark_boundaries(img, mask, color=(0, 0, 1), mode='thick')
                            vis_img = vis_img*255
                            vis_img = vis_img.astype('uint8')
                            bytesPerLine = 3 * 224
                            q_frame = QImage(vis_img, 224, 224, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                            qpixmap_frame = QPixmap.fromImage(q_frame)
                            self.heatLabel_expert.setPixmap(qpixmap_frame)
                        else:
                            self.score_label_expert.setStyleSheet("color: green;")
                            cv2.putText(img, 'OK', (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 
                                   1, (0,255,0), 1, cv2.LINE_AA)
                            bytesPerLine = 3 * 224
                            q_frame = QImage(img, 224, 224, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                            qpixmap_frame = QPixmap.fromImage(q_frame)
                            self.heatLabel_expert.setPixmap(qpixmap_frame)
            else:
                pass
                    
        else:
            pass
        bytesPerLine = 3 * width
        q_frame = QImage(disp_img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        qpixmap_frame = QPixmap.fromImage(q_frame)
        self.imageLabel_expert.setPixmap(qpixmap_frame)        
        
        
        
            
            
            
            
        
    def test_DL_expert(self, img):   
            
            test_inputs = OrderedDict([('layer1', []), ('layer2', []), ('layer3', [])])
            img = Image.fromarray(img)
                
            image_tensor = self.test_transforms(img).float()
            image_tensor = image_tensor.unsqueeze_(0)
            
            with torch.no_grad():
                _ = self.model(image_tensor.to(self.device))
            for k, v in zip(test_inputs.keys(), self.outputs):
                test_inputs[k].append(v.cpu().detach())
            self.outputs = []
                
            for k, v in test_inputs.items():
                test_inputs[k] = torch.cat(v, 0)
                
            embedding_vectors = test_inputs['layer1']
            for layer_name in ['layer2', 'layer3']:
                embedding_vectors = self.embedding_concat(embedding_vectors, test_inputs[layer_name])
            
            embedding_vectors = torch.index_select(embedding_vectors, 1, self.idx)
            B, C, H, W = embedding_vectors.size()
            embedding_vectors = embedding_vectors.view(B, C, H * W)
            
            dist_list = []
            for i in range(H * W):
                mean = self.train_inputs_exeprt[0][:, i]
                conv_inv = self.train_inputs_exeprt[1][:, :, i]
                dist = [mahalanobis(sample[:, i], mean, conv_inv) for sample in embedding_vectors]
                dist_list.append(dist)
        
            dist_list = np.array(dist_list).transpose(1, 0).reshape(B, H, W)
                    
            dist_list = torch.tensor(dist_list)
            self.scores = F.interpolate(dist_list.unsqueeze(1), size=224, mode='bilinear', align_corners=False).squeeze().numpy()        