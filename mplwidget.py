# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:36:11 2021

@author: boukrana
"""

# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
import matplotlib as mpl

#mpl.style.use("seaborn-dark")

#for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
 #   mpl.rcParams[param] = '#1b252c'  # bluish dark grey

#for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
 # mpl.rcParams[param] = '0.9'  # very light grey


class MplWidget(QWidget):
     
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure(facecolor=("#283741") , dpi=80))
        
        toolbar = NavigationToolbar(self.canvas, self)
        vertical_layout = QVBoxLayout()    
        vertical_layout.addWidget(toolbar)
        vertical_layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(1,1,1)
        self.setLayout(vertical_layout)
        self.canvas.axes.set_facecolor("#1b252c")







   




    """
    def onclick(self,event):
        tx = event.ydata
        tx2 = event.xdata
        self.number = int(tx)
        self.Mesure = "Mesure " + str(tx2)
    """    
        


        
        #self.canvas.mpl_connect('button_press_event', self.onclick)