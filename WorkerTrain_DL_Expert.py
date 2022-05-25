# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:28:00 2022

@author: boukrana
"""

from bibliotheque import *



class Worker_Expert(QThread):
    message = pyqtSignal()
    progress = pyqtSignal()
    load_model = pyqtSignal(list)
    def __init__(self):
        super().__init__()
        self.use_cuda = torch.cuda.is_available()
        self.device = torch.device('cuda' if self.use_cuda else 'cpu')       
        self.scores=0
    def train_DL_expert(self,train_inputs,idx):
           self.train_inputs=train_inputs
           self.idx=idx
           
           train_in = self.train_inputs.copy()
               
           for k, v in train_in.items():
               train_in[k] = torch.cat(v, 0)
               
           embedding_vectors = train_in['layer1']
           for layer_name in ['layer2', 'layer3']:
               embedding_vectors = self.embedding_concat(embedding_vectors, train_in[layer_name])
           self.progress.emit()
           embedding_vectors = torch.index_select(embedding_vectors, 1, self.idx)
           B, C, H, W = embedding_vectors.size()
           embedding_vectors = embedding_vectors.view(B, C, H * W)
           mean = torch.mean(embedding_vectors, dim=0).numpy()
           std = torch.std(embedding_vectors, dim=0).numpy()
           cov_inv = torch.zeros(C, C, H * W).numpy()
           I = np.identity(C)
           for i in range(H * W):
               cov_inv[:, :, i] = np.linalg.inv(np.cov(embedding_vectors[:, :, i].numpy(), rowvar=False) + 0.01 * I)           
           
           now = datetime.now()
           name_frame = now.strftime("%d-%m-%Y_%Hh%Mm%Ss%f")
           with open("./model/"+"model_"+name_frame+".pkl",'wb') as fh:
               pickle.dump([mean, cov_inv,round(30*np.amax(std),2)],fh)
           
           
           self.message.emit()
           


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


    def load(self,path):
        with open(path,'rb') as fh:
            model = pickle.load(fh)
        
        self.load_model.emit(model)





