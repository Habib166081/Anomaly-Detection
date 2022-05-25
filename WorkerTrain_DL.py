# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:28:00 2022

@author: boukrana
"""

from bibliotheque import *



class Worker(QThread):
    message = pyqtSignal(float)
    SigInfo = pyqtSignal(str,list,float,object)
    progress = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.use_cuda = torch.cuda.is_available()
        self.device = torch.device('cuda' if self.use_cuda else 'cpu')       
        self.scores=0
    def train_DL(self,train_inputs,idx):
           self.train_inputs=train_inputs
           self.idx=idx
           tic = time.time()
           
           train_in = self.train_inputs.copy()
               
           for k, v in train_in.items():
               train_in[k] = torch.cat(v, 0)
               
           embedding_vectors = train_in['layer1']
           for layer_name in ['layer2', 'layer3']:
               embedding_vectors = self.embedding_concat(embedding_vectors, train_in[layer_name])
           self.progress.emit(0)
           embedding_vectors = torch.index_select(embedding_vectors, 1, self.idx)
           B, C, H, W = embedding_vectors.size()
           embedding_vectors = embedding_vectors.view(B, C, H * W)
           mean = torch.mean(embedding_vectors, dim=0).numpy()
           std = torch.std(embedding_vectors, dim=0).numpy()
           cov_inv = torch.zeros(C, C, H * W).numpy()
           I = np.identity(C)
           for i in range(H * W):
               cov_inv[:, :, i] = np.linalg.inv(np.cov(embedding_vectors[:, :, i].numpy(), rowvar=False) + 0.01 * I)
           self.SigInfo.emit(str(round(30*np.amax(std),2)) ,[mean, cov_inv], np.amax(self.scores),self.scores )
           self.progress.emit(1)
           self.message.emit(tic)
           


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
