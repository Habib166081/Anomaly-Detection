# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 10:28:45 2022

@author: boukrana
"""

from pyueye import ueye
from PyQt5.QtCore import Qt, QThread, QTimer, QDir,pyqtSignal, QSize, QRect
from PyQt5.QtGui import QFont, QPixmap, QImage, QDoubleValidator, QStandardItem, QColor
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem, QLineEdit, QWidget, QSpinBox, QDialog, QPushButton, QSizePolicy, QListView, QFileSystemModel, QFileDialog, QApplication, QSlider, QGridLayout, QVBoxLayout, QGroupBox, QComboBox, QLabel
from interface import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
import random
from random import sample
import numpy as np
import cv2
from scipy.ndimage import gaussian_filter
from scipy.spatial.distance import mahalanobis
from PIL import Image
import time

from PyQt5 import QtGui

from PyQt5 import QtWidgets
import os
import glob

import torch
import torch.nn.functional as F
from torchvision.models import wide_resnet50_2, resnet18
from collections import OrderedDict
from torchvision import transforms as T

from skimage.segmentation import mark_boundaries
#from skimage import morphology


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from datetime import datetime
import pickle

import ctypes # Ces trois lignes sont pour affichage du logo
myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
