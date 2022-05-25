# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:35:11 2022

@author: boukrana
"""
from bibliotheque import *



class MovieThread(QThread):
    def __init__(self, camera):
        super().__init__()
        self.camera = camera

    def run(self):
        self.camera.acquire_movie(200)



