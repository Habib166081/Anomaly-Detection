# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 828)
        MainWindow.setStyleSheet("*{\n"
"    border: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(24, 24, 36);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_body)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_body_contents = QtWidgets.QFrame(self.main_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        self.main_body_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_contents.setObjectName("main_body_contents")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.main_body_contents)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.header_frame = QtWidgets.QFrame(self.main_body_contents)
        self.header_frame.setMinimumSize(QtCore.QSize(0, 80))
        self.header_frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.header_frame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.header_frame.setAutoFillBackground(False)
        self.header_frame.setStyleSheet("background-color: rgb(9, 5, 13);")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.header_frame)
        self.widget_3.setMinimumSize(QtCore.QSize(300, 80))
        self.widget_3.setMaximumSize(QtCore.QSize(300, 80))
        self.widget_3.setStyleSheet("background-color: #283741\n"
"")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.widget_4)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(9, 5, 9, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.statut_2 = QtWidgets.QLabel(self.frame)
        self.statut_2.setMinimumSize(QtCore.QSize(0, 20))
        self.statut_2.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.statut_2.setFont(font)
        self.statut_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"background-color: rgb(0, 255, 0);\n"
"padding: 5px 10px;\n"
"border-radius: 10px;\n"
"background-color: rgb(107, 211, 38);\n"
"    \n"
"")
        self.statut_2.setObjectName("statut_2")
        self.horizontalLayout_6.addWidget(self.statut_2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(25, 20))
        self.label_4.setMaximumSize(QtCore.QSize(25, 20))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("images/output-onlinepngtools.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(23, 20))
        self.label.setMaximumSize(QtCore.QSize(23, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/reglage.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(self.widget_4)
        self.frame_3.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setMinimumSize(QtCore.QSize(30, 20))
        self.label_7.setMaximumSize(QtCore.QSize(30, 20))
        self.label_7.setToolTipDuration(0)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("images/clock.PNG"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.timeEdit = QtWidgets.QTimeEdit(self.frame_3)
        self.timeEdit.setMinimumSize(QtCore.QSize(41, 22))
        self.timeEdit.setMaximumSize(QtCore.QSize(41, 22))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.timeEdit.setFont(font)
        self.timeEdit.setMouseTracking(False)
        self.timeEdit.setTabletTracking(False)
        self.timeEdit.setAcceptDrops(False)
        self.timeEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"")
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(False)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 3), QtCore.QTime(0, 0, 0)))
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_7.addWidget(self.timeEdit)
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setMinimumSize(QtCore.QSize(7, 1))
        self.line_3.setMaximumSize(QtCore.QSize(7, 1))
        self.line_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_7.addWidget(self.line_3)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_3)
        self.dateEdit.setMinimumSize(QtCore.QSize(91, 22))
        self.dateEdit.setMaximumSize(QtCore.QSize(91, 22))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.dateEdit.setFrame(False)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_7.addWidget(self.dateEdit)
        self.verticalLayout_3.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_5.addWidget(self.widget_4)
        self.line_2 = QtWidgets.QFrame(self.widget_3)
        self.line_2.setMinimumSize(QtCore.QSize(1, 40))
        self.line_2.setMaximumSize(QtCore.QSize(1, 40))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.line_2)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.header_frame)
        self.widget_2.setMinimumSize(QtCore.QSize(600, 80))
        self.widget_2.setMaximumSize(QtCore.QSize(555555, 80))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #ffffff;\n"
"\n"
"background-color: #283741\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.header_frame)
        self.widget.setMinimumSize(QtCore.QSize(300, 80))
        self.widget.setMaximumSize(QtCore.QSize(300, 80))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setStyleSheet("background-color: #283741\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(300, 80))
        self.label_2.setMaximumSize(QtCore.QSize(300, 80))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/logo.PNG"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setMinimumSize(QtCore.QSize(1, 40))
        self.line.setMaximumSize(QtCore.QSize(1, 40))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout_11.addWidget(self.header_frame)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.main_body_contents)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(1, 0))
        self.tabWidget_2.setStyleSheet("\n"
"\n"
" QTabWidget::pane { /* The tab widget frame */\n"
"     position: absolute;\n"
"     top: -0.5em;\n"
"\n"
" }\n"
"\n"
" QTabWidget::tab-bar {\n"
"     alignment: center;\n"
"\n"
" }\n"
"\n"
" /* Style the tab using the tab sub-control. Note that\n"
"     it reads QTabBar _not_ QTabWidget */\n"
" QTabBar::tab {\n"
"background-color: rgb(27, 37, 44);\n"
"\n"
"color: rgb(91, 125, 148);\n"
"color: rgb(208, 208, 208);\n"
"\n"
"padding:5px 30px 5px 30px;\n"
"border-bottom-right-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"\n"
"\n"
" }\n"
"\n"
"\n"
" QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background-color: rgba(40,55,65,255);\n"
"}")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.Production = QtWidgets.QWidget()
        self.Production.setObjectName("Production")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Production)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_5 = QtWidgets.QWidget(self.Production)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.graphique = QtWidgets.QWidget(self.widget_5)
        self.graphique.setMinimumSize(QtCore.QSize(0, 33))
        self.graphique.setStyleSheet("border-width: 2px;\n"
"border-radius:10px;\n"
"\n"
"")
        self.graphique.setObjectName("graphique")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.graphique)
        self.verticalLayout_5.setContentsMargins(0, 9, 0, 5)
        self.verticalLayout_5.setSpacing(11)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.graphique)
        self.frame_5.setMinimumSize(QtCore.QSize(464, 336))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setStyleSheet("color: #ffffff;\n"
"\n"
"background-color: #283741\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 1)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget_13 = QtWidgets.QWidget(self.frame_5)
        self.widget_13.setMinimumSize(QtCore.QSize(465, 336))
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_6.setContentsMargins(2, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_14 = QtWidgets.QWidget(self.widget_13)
        self.widget_14.setMinimumSize(QtCore.QSize(465, 30))
        self.widget_14.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_14.setStyleSheet("")
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.heatmap = QtWidgets.QRadioButton(self.widget_14)
        self.heatmap.setEnabled(True)
        self.heatmap.setChecked(True)
        self.heatmap.setObjectName("heatmap")
        self.horizontalLayout_20.addWidget(self.heatmap, 0, QtCore.Qt.AlignHCenter)
        self.mask = QtWidgets.QRadioButton(self.widget_14)
        self.mask.setMinimumSize(QtCore.QSize(232, 0))
        self.mask.setObjectName("mask")
        self.horizontalLayout_20.addWidget(self.mask)
        self.verticalLayout_6.addWidget(self.widget_14)
        self.heatLabel = QtWidgets.QLabel(self.widget_13)
        self.heatLabel.setMinimumSize(QtCore.QSize(465, 299))
        self.heatLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.heatLabel.setStyleSheet("background-color: rgb(27, 37, 44);\n"
"")
        self.heatLabel.setText("")
        self.heatLabel.setScaledContents(True)
        self.heatLabel.setObjectName("heatLabel")
        self.verticalLayout_6.addWidget(self.heatLabel, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_9.addWidget(self.widget_13, 0, QtCore.Qt.AlignLeft)
        self.widget_15 = QtWidgets.QWidget(self.frame_5)
        self.widget_15.setObjectName("widget_15")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_15)
        self.gridLayout_8.setContentsMargins(2, 1, 2, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.imageLabel = QtWidgets.QLabel(self.widget_15)
        self.imageLabel.setMinimumSize(QtCore.QSize(448, 293))
        self.imageLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.imageLabel.setStyleSheet("background-color: rgb(27, 37, 44);\n"
"")
        self.imageLabel.setText("")
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setObjectName("imageLabel")
        self.gridLayout_8.addWidget(self.imageLabel, 0, 0, 1, 1)
        self.horizontalLayout_9.addWidget(self.widget_15)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.graphique)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 301))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 301))
        self.frame_6.setStyleSheet("color: #ffffff;\n"
"\n"
"background-color: #283741\n"
"\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_17.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_17.setSpacing(1)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.hist_plot = MplWidget(self.frame_6)
        self.hist_plot.setMinimumSize(QtCore.QSize(682, 283))
        self.hist_plot.setMaximumSize(QtCore.QSize(16777215, 400))
        self.hist_plot.setStyleSheet("background-color: rgb(27, 37, 44);\n"
"")
        self.hist_plot.setObjectName("hist_plot")
        self.horizontalLayout_17.addWidget(self.hist_plot)
        self.widget_10 = QtWidgets.QWidget(self.frame_6)
        self.widget_10.setStyleSheet("background-color: rgb(27, 37, 44);\n"
"")
        self.widget_10.setObjectName("widget_10")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_10)
        self.gridLayout_4.setContentsMargins(2, 0, 0, 3)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listImages = QtWidgets.QListWidget(self.widget_10)
        self.listImages.setStyleSheet("    QListWidget{\n"
"color: rgb(208, 208, 208);\n"
"background-color: #283741\n"
"selection-background-color: #0099ff;\n"
"border-radius: 10px;\n"
"}\n"
"        QScrollBar:vertical {    \n"
"          \n"
"            background:rgba(40,55,65,255);\n"
"            width:15px;\n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {\n"
"            background:rgba(40,55,65,255);\n"
"            min-height: 0px;\n"
"        }\n"
"        QScrollBar::add-line:vertical {\n"
"background-color:white\n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"background-color:white;\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.listImages.setObjectName("listImages")
        self.gridLayout_4.addWidget(self.listImages, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.widget_11 = QtWidgets.QWidget(self.widget_10)
        self.widget_11.setStyleSheet("")
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_18.setContentsMargins(0, 0, 57, 2)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_18 = QtWidgets.QLabel(self.widget_11)
        self.label_18.setMinimumSize(QtCore.QSize(51, 20))
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("\n"
"color: rgb(208, 208, 208);")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_18.addWidget(self.label_18)
        self.Supp = QtWidgets.QToolButton(self.widget_11)
        self.Supp.setMinimumSize(QtCore.QSize(45, 45))
        self.Supp.setMaximumSize(QtCore.QSize(45, 45))
        self.Supp.setStyleSheet("border-radius: 19px; \n"
"background-color: None;\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.Supp.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons8-supprimer-400.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Supp.setIcon(icon)
        self.Supp.setIconSize(QtCore.QSize(90, 90))
        self.Supp.setCheckable(False)
        self.Supp.setAutoRepeat(False)
        self.Supp.setAutoExclusive(False)
        self.Supp.setObjectName("Supp")
        self.horizontalLayout_18.addWidget(self.Supp, 0, QtCore.Qt.AlignLeft)
        self.gridLayout_4.addWidget(self.widget_11, 1, 0, 1, 1)
        self.horizontalLayout_17.addWidget(self.widget_10)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.horizontalLayout_8.addWidget(self.graphique)
        self.Reglage = QtWidgets.QWidget(self.widget_5)
        self.Reglage.setMinimumSize(QtCore.QSize(250, 0))
        self.Reglage.setMaximumSize(QtCore.QSize(250, 16777215))
        self.Reglage.setStyleSheet("border-width: 2px;\n"
"border-radius:10px;\n"
"\n"
"")
        self.Reglage.setObjectName("Reglage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Reglage)
        self.verticalLayout_4.setContentsMargins(5, 9, 0, 5)
        self.verticalLayout_4.setSpacing(13)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.Reglage)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 320))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("color: #ffffff;\n"
"\n"
"background-color: #283741\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setContentsMargins(9, 10, 9, 9)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 10))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(208, 208, 208);\n"
"border-radius: none;\n"
"border-top: 20px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.widget_6 = QtWidgets.QWidget(self.frame_2)
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_7 = QtWidgets.QFrame(self.widget_6)
        self.frame_7.setMinimumSize(QtCore.QSize(140, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(140, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.slider_exposure_time = QtWidgets.QSlider(self.frame_7)
        self.slider_exposure_time.setMinimumSize(QtCore.QSize(122, 60))
        self.slider_exposure_time.setStyleSheet("QSlider:horizontal {\n"
"    min-height: 60px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 1px;\n"
"    background: white; \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    width: 30px;\n"
"    margin-top: -15px;\n"
"    margin-bottom: -15px;\n"
"    border-radius: 15px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(210, 210, 210, 255), stop:0.7 rgba(210, 210, 210, 100));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(255, 255, 255, 255), stop:0.7 rgba(255, 255, 255, 100));\n"
"}")
        self.slider_exposure_time.setMaximum(1000)
        self.slider_exposure_time.setSingleStep(1)
        self.slider_exposure_time.setProperty("value", 240)
        self.slider_exposure_time.setOrientation(QtCore.Qt.Horizontal)
        self.slider_exposure_time.setObjectName("slider_exposure_time")
        self.verticalLayout_9.addWidget(self.slider_exposure_time, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_10.addWidget(self.frame_7)
        self.frame_16 = QtWidgets.QFrame(self.widget_6)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout.setObjectName("gridLayout")
        self.slider_exposure_label = QtWidgets.QLabel(self.frame_16)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.slider_exposure_label.setFont(font)
        self.slider_exposure_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.slider_exposure_label.setAlignment(QtCore.Qt.AlignCenter)
        self.slider_exposure_label.setObjectName("slider_exposure_label")
        self.gridLayout.addWidget(self.slider_exposure_label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_10.addWidget(self.frame_16)
        self.verticalLayout_7.addWidget(self.widget_6)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 89))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_18 = QtWidgets.QFrame(self.frame_8)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 4)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.frame_18)
        self.label_10.setMinimumSize(QtCore.QSize(0, 15))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(208, 208, 208);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.button_frame = QtWidgets.QToolButton(self.frame_18)
        self.button_frame.setMinimumSize(QtCore.QSize(55, 55))
        self.button_frame.setMaximumSize(QtCore.QSize(55, 55))
        self.button_frame.setStyleSheet("border-radius: 19px; \n"
"background-color: None;\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.button_frame.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_frame.setIcon(icon1)
        self.button_frame.setIconSize(QtCore.QSize(90, 90))
        self.button_frame.setCheckable(False)
        self.button_frame.setAutoRepeat(False)
        self.button_frame.setAutoExclusive(False)
        self.button_frame.setObjectName("button_frame")
        self.gridLayout_2.addWidget(self.button_frame, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_12.addWidget(self.frame_18)
        self.frame_17 = QtWidgets.QFrame(self.frame_8)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_3.setContentsMargins(0, 6, 0, 9)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.button_movie = QtWidgets.QToolButton(self.frame_17)
        self.button_movie.setMinimumSize(QtCore.QSize(55, 55))
        self.button_movie.setMaximumSize(QtCore.QSize(55, 55))
        self.button_movie.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_movie.setStyleSheet("border-radius: 19px; \n"
"background-color: None;\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.button_movie.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/button_start_stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("images/Stop_.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.button_movie.setIcon(icon2)
        self.button_movie.setIconSize(QtCore.QSize(80, 80))
        self.button_movie.setObjectName("button_movie")
        self.gridLayout_3.addWidget(self.button_movie, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_12 = QtWidgets.QLabel(self.frame_17)
        self.label_12.setMinimumSize(QtCore.QSize(0, 17))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(208, 208, 208);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.horizontalLayout_12.addWidget(self.frame_17)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 98))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_7 = QtWidgets.QWidget(self.frame_9)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Nb_acquisition = QtWidgets.QSpinBox(self.widget_7)
        self.Nb_acquisition.setMinimumSize(QtCore.QSize(80, 46))
        self.Nb_acquisition.setMaximumSize(QtCore.QSize(100, 46))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Nb_acquisition.setFont(font)
        self.Nb_acquisition.setStyleSheet("QSpinBox {\n"
"color: rgb(209, 209, 209);\n"
"    border:3px solid rgb(27, 37, 44);\n"
"    border-radius:8px;    \n"
"    min-height:40px;\n"
"    max-height:40px;\n"
"    qproperty-alignment: AlignCenter;    \n"
"}\n"
" \n"
" QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    top:9.5px;\n"
"    width: 20px;\n"
"    height:25px;  \n"
"\n"
" }\n"
" \n"
" QSpinBox::down-button {\n"
"   subcontrol-origin: border;\n"
"\n"
"     subcontrol-position: left; \n"
"    buttom:7px;\n"
"    width: 20px;\n"
"    height:25px;  \n"
" }\n"
"\n"
" \n"
"")
        self.Nb_acquisition.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.Nb_acquisition.setMinimum(1)
        self.Nb_acquisition.setMaximum(999999999)
        self.Nb_acquisition.setProperty("value", 1)
        self.Nb_acquisition.setObjectName("Nb_acquisition")
        self.verticalLayout_10.addWidget(self.Nb_acquisition, 0, QtCore.Qt.AlignHCenter)
        self.progressBarAcqui = QtWidgets.QProgressBar(self.widget_7)
        self.progressBarAcqui.setMinimumSize(QtCore.QSize(80, 16))
        self.progressBarAcqui.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.progressBarAcqui.setFont(font)
        self.progressBarAcqui.setAutoFillBackground(False)
        self.progressBarAcqui.setStyleSheet("QProgressBar {\n"
"    color: rgb(177, 177, 177);\n"
"    border: none;\n"
"    background-color: rgb(27, 37, 44);;\n"
"    border-radius:8px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(7, 255, 119);\n"
"    border-radius : 8px;\n"
"}     ")
        self.progressBarAcqui.setMaximum(100)
        self.progressBarAcqui.setProperty("value", 0)
        self.progressBarAcqui.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBarAcqui.setTextVisible(False)
        self.progressBarAcqui.setOrientation(QtCore.Qt.Horizontal)
        self.progressBarAcqui.setInvertedAppearance(False)
        self.progressBarAcqui.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBarAcqui.setObjectName("progressBarAcqui")
        self.verticalLayout_10.addWidget(self.progressBarAcqui, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_11.addWidget(self.widget_7)
        self.middele_circle_frame_5 = QtWidgets.QFrame(self.frame_9)
        self.middele_circle_frame_5.setMinimumSize(QtCore.QSize(81, 81))
        self.middele_circle_frame_5.setMaximumSize(QtCore.QSize(81, 81))
        self.middele_circle_frame_5.setStyleSheet("background-color: None;\n"
"\n"
"border: 7px solid rgb(27, 37, 44);;\n"
"border-radius:40px; /*50% of it\'s size*/\n"
"\n"
"")
        self.middele_circle_frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.middele_circle_frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.middele_circle_frame_5.setObjectName("middele_circle_frame_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.middele_circle_frame_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.nb_img_train = QtWidgets.QLabel(self.middele_circle_frame_5)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.nb_img_train.setFont(font)
        self.nb_img_train.setStyleSheet("  border: 2px ;\n"
"background-color: None;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"")
        self.nb_img_train.setAlignment(QtCore.Qt.AlignCenter)
        self.nb_img_train.setObjectName("nb_img_train")
        self.gridLayout_6.addWidget(self.nb_img_train, 0, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.middele_circle_frame_5, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.frame_9)
        self.widget_12 = QtWidgets.QWidget(self.frame_2)
        self.widget_12.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_13 = QtWidgets.QFrame(self.widget_12)
        self.frame_13.setMinimumSize(QtCore.QSize(140, 0))
        self.frame_13.setMaximumSize(QtCore.QSize(140, 16777215))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.cursor_mask = QtWidgets.QSlider(self.frame_13)
        self.cursor_mask.setMinimumSize(QtCore.QSize(122, 60))
        self.cursor_mask.setStyleSheet("QSlider:horizontal {\n"
"    min-height: 60px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 1px;\n"
"    background: white; \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    width: 30px;\n"
"    margin-top: -15px;\n"
"    margin-bottom: -15px;\n"
"    border-radius: 15px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(210, 210, 210, 255), stop:0.7 rgba(210, 210, 210, 100));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(255, 255, 255, 255), stop:0.7 rgba(255, 255, 255, 100));\n"
"}")
        self.cursor_mask.setMaximum(100)
        self.cursor_mask.setSingleStep(0)
        self.cursor_mask.setProperty("value", 77)
        self.cursor_mask.setOrientation(QtCore.Qt.Horizontal)
        self.cursor_mask.setObjectName("cursor_mask")
        self.verticalLayout_16.addWidget(self.cursor_mask, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_19.addWidget(self.frame_13)
        self.frame_21 = QtWidgets.QFrame(self.widget_12)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_21)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.cursor_mask_label = QtWidgets.QLabel(self.frame_21)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.cursor_mask_label.setFont(font)
        self.cursor_mask_label.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.cursor_mask_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cursor_mask_label.setObjectName("cursor_mask_label")
        self.gridLayout_7.addWidget(self.cursor_mask_label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_19.addWidget(self.frame_21)
        self.verticalLayout_7.addWidget(self.widget_12)
        self.widget_9 = QtWidgets.QWidget(self.frame_2)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 4)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.Restart = QtWidgets.QToolButton(self.widget_9)
        self.Restart.setMinimumSize(QtCore.QSize(45, 45))
        self.Restart.setMaximumSize(QtCore.QSize(45, 45))
        self.Restart.setStyleSheet("border-radius: 19px; \n"
"background-color: None;\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.Restart.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/refresh2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Restart.setIcon(icon3)
        self.Restart.setIconSize(QtCore.QSize(90, 90))
        self.Restart.setCheckable(False)
        self.Restart.setAutoRepeat(False)
        self.Restart.setAutoExclusive(False)
        self.Restart.setObjectName("Restart")
        self.verticalLayout_15.addWidget(self.Restart, 0, QtCore.Qt.AlignHCenter)
        self.label_16 = QtWidgets.QLabel(self.widget_9)
        self.label_16.setMinimumSize(QtCore.QSize(0, 15))
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(208, 208, 208);")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_15.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.widget_9)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.Reglage)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 301))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 301))
        self.frame_4.setStyleSheet("color: #ffffff;\n"
"\n"
"background-color: #283741\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setContentsMargins(9, 3, 9, 1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setMinimumSize(QtCore.QSize(0, 10))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label_6.setStyleSheet("color: rgb(208, 208, 208);\n"
"border-radius: none;\n"
"border-top: 20px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.model_combo = QtWidgets.QComboBox(self.frame_12)
        self.model_combo.setMinimumSize(QtCore.QSize(180, 25))
        self.model_combo.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(27, 37, 44);\n"
"\n"
"\n"
"selection-background-color: rgba(16,25,30,255);\n"
"color: rgb(208, 208, 208);\n"
"border-radius: 10px;\n"
"")
        self.model_combo.setObjectName("model_combo")
        self.model_combo.addItem("")
        self.model_combo.addItem("")
        self.gridLayout_5.addWidget(self.model_combo, 0, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_12)
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 102))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setContentsMargins(13, 3, 15, 23)
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_19 = QtWidgets.QFrame(self.frame_10)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 9)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.button_Train = QtWidgets.QToolButton(self.frame_19)
        self.button_Train.setMinimumSize(QtCore.QSize(55, 55))
        self.button_Train.setMaximumSize(QtCore.QSize(55, 55))
        self.button_Train.setStyleSheet("border-radius: 19px; \n"
"background-color: None;\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.button_Train.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/cpu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("images/cpu2.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.button_Train.setIcon(icon4)
        self.button_Train.setIconSize(QtCore.QSize(90, 90))
        self.button_Train.setCheckable(False)
        self.button_Train.setAutoRepeat(False)
        self.button_Train.setAutoExclusive(False)
        self.button_Train.setObjectName("button_Train")
        self.verticalLayout_12.addWidget(self.button_Train, 0, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.frame_19)
        self.label_11.setMinimumSize(QtCore.QSize(0, 20))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(208, 208, 208);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_12.addWidget(self.label_11, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_13.addWidget(self.frame_19)
        self.widget_8 = QtWidgets.QWidget(self.frame_10)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.progressBarEntrain = QtWidgets.QProgressBar(self.widget_8)
        self.progressBarEntrain.setMinimumSize(QtCore.QSize(16, 70))
        self.progressBarEntrain.setMaximumSize(QtCore.QSize(16, 80))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.progressBarEntrain.setFont(font)
        self.progressBarEntrain.setAutoFillBackground(False)
        self.progressBarEntrain.setStyleSheet("QProgressBar {\n"
"    color: rgb(177, 177, 177);\n"
"    border: none;\n"
"    background-color: rgb(27, 37, 44);;\n"
"    border-radius:8px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(7, 255, 119);\n"
"    border-radius : 8px;\n"
"}     ")
        self.progressBarEntrain.setMaximum(100)
        self.progressBarEntrain.setProperty("value", 0)
        self.progressBarEntrain.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBarEntrain.setTextVisible(False)
        self.progressBarEntrain.setOrientation(QtCore.Qt.Vertical)
        self.progressBarEntrain.setInvertedAppearance(False)
        self.progressBarEntrain.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBarEntrain.setObjectName("progressBarEntrain")
        self.horizontalLayout_16.addWidget(self.progressBarEntrain)
        self.horizontalLayout_13.addWidget(self.widget_8)
        self.frame_20 = QtWidgets.QFrame(self.frame_10)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.button_addTrain = QtWidgets.QToolButton(self.frame_20)
        self.button_addTrain.setMinimumSize(QtCore.QSize(55, 55))
        self.button_addTrain.setMaximumSize(QtCore.QSize(55, 55))
        self.button_addTrain.setStyleSheet("border-radius: 19px; \n"
"background-color: None;\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.button_addTrain.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("images/plus-circle2.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.button_addTrain.setIcon(icon5)
        self.button_addTrain.setIconSize(QtCore.QSize(90, 90))
        self.button_addTrain.setCheckable(False)
        self.button_addTrain.setAutoRepeat(False)
        self.button_addTrain.setAutoExclusive(False)
        self.button_addTrain.setObjectName("button_addTrain")
        self.verticalLayout_13.addWidget(self.button_addTrain, 0, QtCore.Qt.AlignHCenter)
        self.label_13 = QtWidgets.QLabel(self.frame_20)
        self.label_13.setMinimumSize(QtCore.QSize(0, 20))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(208, 208, 208);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_13.addWidget(self.label_13, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_13.addWidget(self.frame_20)
        self.verticalLayout_8.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.test_combo = QtWidgets.QComboBox(self.frame_11)
        self.test_combo.setMinimumSize(QtCore.QSize(180, 25))
        self.test_combo.setMaximumSize(QtCore.QSize(209, 16777215))
        self.test_combo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.test_combo.setStyleSheet("        border-radius: 10px;\n"
"background-color: rgb(27, 37, 44);\n"
"\n"
"\n"
"selection-background-color: rgba(16,25,30,255);\n"
"color: rgb(208, 208, 208);\n"
"border-radius: 10px;\n"
"")
        self.test_combo.setObjectName("test_combo")
        self.verticalLayout_14.addWidget(self.test_combo)
        self.verticalLayout_8.addWidget(self.frame_11)
        self.frame_14 = QtWidgets.QFrame(self.frame_4)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_14 = QtWidgets.QLabel(self.frame_14)
        self.label_14.setMinimumSize(QtCore.QSize(0, 30))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(27, 37, 44);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_14.addWidget(self.label_14, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.score_label = QtWidgets.QLabel(self.frame_14)
        self.score_label.setMinimumSize(QtCore.QSize(100, 40))
        self.score_label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.score_label.setFont(font)
        self.score_label.setText("")
        self.score_label.setAlignment(QtCore.Qt.AlignCenter)
        self.score_label.setObjectName("score_label")
        self.horizontalLayout_14.addWidget(self.score_label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_8.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_4)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_15 = QtWidgets.QLabel(self.frame_15)
        self.label_15.setMinimumSize(QtCore.QSize(0, 50))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(27, 37, 44);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_15.addWidget(self.label_15, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.thr_AI_val = QtWidgets.QDoubleSpinBox(self.frame_15)
        self.thr_AI_val.setMinimumSize(QtCore.QSize(80, 46))
        self.thr_AI_val.setMaximumSize(QtCore.QSize(100, 46))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.thr_AI_val.setFont(font)
        self.thr_AI_val.setStyleSheet("QDoubleSpinBox {\n"
"color: rgb(209, 209, 209);\n"
"    border:3px solid #283741;\n"
"    border-radius:8px;    \n"
"    min-height:40px;\n"
"    max-height:40px;\n"
"    qproperty-alignment: AlignCenter;    \n"
"}\n"
" \n"
" QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    top:9.5px;\n"
"    width: 20px;\n"
"    height:25px;  \n"
"\n"
" }\n"
" \n"
" QDoubleSpinBox::down-button {\n"
"   subcontrol-origin: border;\n"
"\n"
"     subcontrol-position: left; \n"
"    buttom:7px;\n"
"    width: 20px;\n"
"    height:25px;  \n"
" }\n"
"\n"
" \n"
"")
        self.thr_AI_val.setMaximum(100.0)
        self.thr_AI_val.setObjectName("thr_AI_val")
        self.horizontalLayout_15.addWidget(self.thr_AI_val)
        self.verticalLayout_8.addWidget(self.frame_15)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.horizontalLayout_8.addWidget(self.Reglage)
        self.horizontalLayout_3.addWidget(self.widget_5)
        self.tabWidget_2.addTab(self.Production, "")
        self.Expert = QtWidgets.QWidget()
        self.Expert.setObjectName("Expert")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.Expert)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.widget_16 = QtWidgets.QWidget(self.Expert)
        self.widget_16.setMinimumSize(QtCore.QSize(1000, 500))
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_16)
        self.verticalLayout_17.setContentsMargins(9, 9, 9, 4)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.widget_17 = QtWidgets.QWidget(self.widget_16)
        self.widget_17.setMinimumSize(QtCore.QSize(0, 497))
        self.widget_17.setStyleSheet("border-width: 2px;\n"
"border-radius:10px;\n"
"")
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_21.setContentsMargins(0, 9, 0, 0)
        self.horizontalLayout_21.setSpacing(3)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.frame_23 = QtWidgets.QFrame(self.widget_17)
        self.frame_23.setStyleSheet("background-color: #283741\n"
"")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.widget_19 = QtWidgets.QWidget(self.frame_23)
        self.widget_19.setMinimumSize(QtCore.QSize(465, 30))
        self.widget_19.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_19.setStyleSheet("")
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.heatmap_expert = QtWidgets.QRadioButton(self.widget_19)
        self.heatmap_expert.setEnabled(True)
        self.heatmap_expert.setChecked(True)
        self.heatmap_expert.setObjectName("heatmap_expert")
        self.horizontalLayout_23.addWidget(self.heatmap_expert, 0, QtCore.Qt.AlignHCenter)
        self.mask_expert = QtWidgets.QRadioButton(self.widget_19)
        self.mask_expert.setMinimumSize(QtCore.QSize(232, 0))
        self.mask_expert.setObjectName("mask_expert")
        self.horizontalLayout_23.addWidget(self.mask_expert)
        self.verticalLayout_19.addWidget(self.widget_19)
        self.heatLabel_expert = QtWidgets.QLabel(self.frame_23)
        self.heatLabel_expert.setStyleSheet("background-color: rgb(27, 37, 44);")
        self.heatLabel_expert.setText("")
        self.heatLabel_expert.setScaledContents(True)
        self.heatLabel_expert.setObjectName("heatLabel_expert")
        self.verticalLayout_19.addWidget(self.heatLabel_expert)
        self.horizontalLayout_21.addWidget(self.frame_23)
        self.frame_22 = QtWidgets.QFrame(self.widget_17)
        self.frame_22.setStyleSheet("background-color: #283741\n"
"")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_22)
        self.gridLayout_9.setContentsMargins(-1, 6, -1, 9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.imageLabel_expert = QtWidgets.QLabel(self.frame_22)
        self.imageLabel_expert.setStyleSheet("background-color: rgb(27, 37, 44);")
        self.imageLabel_expert.setText("")
        self.imageLabel_expert.setScaledContents(True)
        self.imageLabel_expert.setObjectName("imageLabel_expert")
        self.gridLayout_9.addWidget(self.imageLabel_expert, 0, 0, 1, 1)
        self.horizontalLayout_21.addWidget(self.frame_22)
        self.verticalLayout_17.addWidget(self.widget_17)
        self.widget_18 = QtWidgets.QWidget(self.widget_16)
        self.widget_18.setMinimumSize(QtCore.QSize(0, 220))
        self.widget_18.setMaximumSize(QtCore.QSize(16777215, 220))
        self.widget_18.setStyleSheet("border-width: 2px;\n"
"border-radius:10px;\n"
"")
        self.widget_18.setObjectName("widget_18")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.widget_18)
        self.horizontalLayout_22.setContentsMargins(0, 9, 0, 5)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.frame_24 = QtWidgets.QFrame(self.widget_18)
        self.frame_24.setStyleSheet("background-color: #283741\n"
"")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.frame_29 = QtWidgets.QFrame(self.frame_24)
        self.frame_29.setMaximumSize(QtCore.QSize(316, 16777215))
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_31.setContentsMargins(9, 10, 9, 1)
        self.verticalLayout_31.setSpacing(9)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_25 = QtWidgets.QLabel(self.frame_29)
        self.label_25.setMinimumSize(QtCore.QSize(0, 16))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(208, 208, 208);\n"
"border-radius: none;\n"
"border-top: 20px;")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_31.addWidget(self.label_25)
        self.frame_48 = QtWidgets.QFrame(self.frame_29)
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.frame_48)
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.widget_27 = QtWidgets.QWidget(self.frame_48)
        self.widget_27.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_27.setMaximumSize(QtCore.QSize(278, 30))
        self.widget_27.setStyleSheet("")
        self.widget_27.setObjectName("widget_27")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.widget_27)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setSpacing(6)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.test_img = QtWidgets.QRadioButton(self.widget_27)
        self.test_img.setEnabled(True)
        self.test_img.setMinimumSize(QtCore.QSize(62, 0))
        self.test_img.setChecked(False)
        self.test_img.setObjectName("test_img")
        self.horizontalLayout_33.addWidget(self.test_img, 0, QtCore.Qt.AlignHCenter)
        self.live = QtWidgets.QRadioButton(self.widget_27)
        self.live.setMinimumSize(QtCore.QSize(62, 0))
        self.live.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.live.setCheckable(True)
        self.live.setChecked(True)
        self.live.setObjectName("live")
        self.horizontalLayout_33.addWidget(self.live)
        self.horizontalLayout_41.addWidget(self.widget_27)
        self.frame_38 = QtWidgets.QFrame(self.frame_48)
        self.frame_38.setMaximumSize(QtCore.QSize(16777215, 34))
        self.frame_38.setStyleSheet("border-radius: 10px;")
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_38)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.bouton_parcourir_test = QtWidgets.QToolButton(self.frame_38)
        self.bouton_parcourir_test.setMinimumSize(QtCore.QSize(0, 0))
        self.bouton_parcourir_test.setMaximumSize(QtCore.QSize(52, 16777215))
        self.bouton_parcourir_test.setStyleSheet("background-repeat: no-repeat;\n"
"background-position: center;\n"
"\n"
"border-radius: 20px;")
        self.bouton_parcourir_test.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bouton_parcourir_test.setIcon(icon6)
        self.bouton_parcourir_test.setIconSize(QtCore.QSize(70, 70))
        self.bouton_parcourir_test.setObjectName("bouton_parcourir_test")
        self.horizontalLayout_34.addWidget(self.bouton_parcourir_test)
        self.txt_box_test = QtWidgets.QLineEdit(self.frame_38)
        self.txt_box_test.setMaximumSize(QtCore.QSize(208, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txt_box_test.setFont(font)
        self.txt_box_test.setStyleSheet("background-color: rgb(27, 37, 44);\n"
"color: rgb(208, 208, 208);\n"
"selection-background-color: rgba(16,25,30,255);\n"
"border-radius: 10px;")
        self.txt_box_test.setText("")
        self.txt_box_test.setObjectName("txt_box_test")
        self.horizontalLayout_34.addWidget(self.txt_box_test, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_41.addWidget(self.frame_38)
        self.verticalLayout_31.addWidget(self.frame_48)
        self.frame_42 = QtWidgets.QFrame(self.frame_29)
        self.frame_42.setMaximumSize(QtCore.QSize(5555555, 16777215))
        self.frame_42.setStyleSheet("background-color: #283741\n"
"")
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.frame_42)
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_28 = QtWidgets.QLabel(self.frame_42)
        self.label_28.setMinimumSize(QtCore.QSize(101, 23))
        self.label_28.setMaximumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(27, 37, 44);")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_38.addWidget(self.label_28, 0, QtCore.Qt.AlignVCenter)
        self.cursor_mask_expert = QtWidgets.QSlider(self.frame_42)
        self.cursor_mask_expert.setMinimumSize(QtCore.QSize(120, 35))
        self.cursor_mask_expert.setMaximumSize(QtCore.QSize(120, 34))
        self.cursor_mask_expert.setToolTipDuration(-1)
        self.cursor_mask_expert.setStyleSheet("QSlider:horizontal {\n"
"    min-height: 35px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 1px;\n"
"    background: white; \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    width: 30px;\n"
"    margin-top: -15px;\n"
"    margin-bottom: -15px;\n"
"    border-radius: 15px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(210, 210, 210, 255), stop:0.7 rgba(210, 210, 210, 100));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(255, 255, 255, 255), stop:0.7 rgba(255, 255, 255, 100));\n"
"}")
        self.cursor_mask_expert.setMaximum(100)
        self.cursor_mask_expert.setSingleStep(0)
        self.cursor_mask_expert.setProperty("value", 77)
        self.cursor_mask_expert.setOrientation(QtCore.Qt.Horizontal)
        self.cursor_mask_expert.setObjectName("cursor_mask_expert")
        self.horizontalLayout_38.addWidget(self.cursor_mask_expert, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.cursor_mask_label_expert = QtWidgets.QLabel(self.frame_42)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.cursor_mask_label_expert.setFont(font)
        self.cursor_mask_label_expert.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.cursor_mask_label_expert.setAlignment(QtCore.Qt.AlignCenter)
        self.cursor_mask_label_expert.setObjectName("cursor_mask_label_expert")
        self.horizontalLayout_38.addWidget(self.cursor_mask_label_expert)
        self.verticalLayout_31.addWidget(self.frame_42)
        self.frame_41 = QtWidgets.QFrame(self.frame_29)
        self.frame_41.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_41.setStyleSheet("background-color: #283741\n"
"")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.frame_41)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout_36.setSpacing(39)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_27 = QtWidgets.QLabel(self.frame_41)
        self.label_27.setMinimumSize(QtCore.QSize(101, 23))
        self.label_27.setMaximumSize(QtCore.QSize(101, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(27, 37, 44);")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_36.addWidget(self.label_27, 0, QtCore.Qt.AlignVCenter)
        self.thr_AI_val_expert = QtWidgets.QDoubleSpinBox(self.frame_41)
        self.thr_AI_val_expert.setMinimumSize(QtCore.QSize(100, 46))
        self.thr_AI_val_expert.setMaximumSize(QtCore.QSize(100, 46))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.thr_AI_val_expert.setFont(font)
        self.thr_AI_val_expert.setStyleSheet("QDoubleSpinBox {\n"
"color: rgb(209, 209, 209);\n"
"    border:3px solid #283741;\n"
"    border-radius:8px;    \n"
"    min-height:40px;\n"
"    max-height:40px;\n"
"    qproperty-alignment: AlignCenter;    \n"
"}\n"
" \n"
" QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    top:9.5px;\n"
"    width: 20px;\n"
"    height:25px;  \n"
"\n"
" }\n"
" \n"
" QDoubleSpinBox::down-button {\n"
"   subcontrol-origin: border;\n"
"\n"
"     subcontrol-position: left; \n"
"    buttom:7px;\n"
"    width: 20px;\n"
"    height:25px;  \n"
" }\n"
"\n"
" \n"
"")
        self.thr_AI_val_expert.setObjectName("thr_AI_val_expert")
        self.horizontalLayout_36.addWidget(self.thr_AI_val_expert)
        self.verticalLayout_31.addWidget(self.frame_41)
        self.frame_47 = QtWidgets.QFrame(self.frame_29)
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.frame_47)
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.label_30 = QtWidgets.QLabel(self.frame_47)
        self.label_30.setMinimumSize(QtCore.QSize(0, 30))
        self.label_30.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(27, 37, 44);")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_40.addWidget(self.label_30, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.score_label_expert = QtWidgets.QLabel(self.frame_47)
        self.score_label_expert.setMinimumSize(QtCore.QSize(100, 40))
        self.score_label_expert.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.score_label_expert.setFont(font)
        self.score_label_expert.setAlignment(QtCore.Qt.AlignCenter)
        self.score_label_expert.setObjectName("score_label_expert")
        self.horizontalLayout_40.addWidget(self.score_label_expert, 0, QtCore.Qt.AlignHCenter)
        self.checkBox_test = QtWidgets.QCheckBox(self.frame_47)
        self.checkBox_test.setStyleSheet("QCheckBox{\n"
"color:rgb(91,125,148);\n"
"background-color: #283741;\n"
"border-radius: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"\n"
"\n"
"border: 2px solid black;\n"
"\n"
"width: 15px;\n"
"\n"
"height: 15px;\n"
"\n"
"subcontrol-position: center;\n"
"\n"
"\n"
"\n"
"subcontrol-origin: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"\n"
"background-color:#54c147;\n"
"\n"
"border:5px white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"background-color:rgb(191, 19, 19);\n"
"\n"
"\n"
"border:5px black;\n"
"\n"
"}")
        self.checkBox_test.setText("")
        self.checkBox_test.setObjectName("checkBox_test")
        self.horizontalLayout_40.addWidget(self.checkBox_test)
        self.verticalLayout_31.addWidget(self.frame_47)
        self.horizontalLayout_24.addWidget(self.frame_29)
        self.line_8 = QtWidgets.QFrame(self.frame_24)
        self.line_8.setMinimumSize(QtCore.QSize(0, 177))
        self.line_8.setMaximumSize(QtCore.QSize(16777215, 177))
        self.line_8.setStyleSheet("background-color: rgb(27, 37, 44);")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_24.addWidget(self.line_8)
        self.Test = QtWidgets.QFrame(self.frame_24)
        self.Test.setMinimumSize(QtCore.QSize(0, 0))
        self.Test.setMaximumSize(QtCore.QSize(281, 16777215))
        self.Test.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Test.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Test.setObjectName("Test")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.Test)
        self.verticalLayout_27.setContentsMargins(0, 8, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_22 = QtWidgets.QLabel(self.Test)
        self.label_22.setMinimumSize(QtCore.QSize(0, 16))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(208, 208, 208);\n"
"border-radius: none;\n"
"border-top: 20px;")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_27.addWidget(self.label_22)
        self.frame_35 = QtWidgets.QFrame(self.Test)
        self.frame_35.setMaximumSize(QtCore.QSize(16777215, 66))
        self.frame_35.setStyleSheet("border-radius: 10px;")
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_35)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.frame_28 = QtWidgets.QFrame(self.frame_35)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.Load_images = QtWidgets.QToolButton(self.frame_28)
        self.Load_images.setMinimumSize(QtCore.QSize(0, 0))
        self.Load_images.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Load_images.setStyleSheet("background-repeat: no-repeat;\n"
"background-position: center;\n"
"\n"
"border-radius: 20px;")
        self.Load_images.setText("")
        self.Load_images.setIcon(icon6)
        self.Load_images.setIconSize(QtCore.QSize(70, 70))
        self.Load_images.setObjectName("Load_images")
        self.verticalLayout_21.addWidget(self.Load_images, 0, QtCore.Qt.AlignHCenter)
        self.label_23 = QtWidgets.QLabel(self.frame_28)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(208, 208, 208);")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_21.addWidget(self.label_23, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_31.addWidget(self.frame_28)
        self.widget_28 = QtWidgets.QWidget(self.frame_35)
        self.widget_28.setObjectName("widget_28")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.widget_28)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.txt_box_images = QtWidgets.QLineEdit(self.widget_28)
        self.txt_box_images.setMaximumSize(QtCore.QSize(208, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txt_box_images.setFont(font)
        self.txt_box_images.setStyleSheet("background-color: rgb(27, 37, 44);\n"
"color: rgb(208, 208, 208);\n"
"selection-background-color: rgba(16,25,30,255);\n"
"border-radius: 10px;")
        self.txt_box_images.setText("")
        self.txt_box_images.setObjectName("txt_box_images")
        self.verticalLayout_28.addWidget(self.txt_box_images)
        self.progressBarImages = QtWidgets.QLabel(self.widget_28)
        self.progressBarImages.setMaximumSize(QtCore.QSize(189, 16777210))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.progressBarImages.setFont(font)
        self.progressBarImages.setStyleSheet("    background-color: rgb(27, 37, 44);;\n"
"    border-radius:6px;")
        self.progressBarImages.setText("")
        self.progressBarImages.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBarImages.setObjectName("progressBarImages")
        self.verticalLayout_28.addWidget(self.progressBarImages)
        self.horizontalLayout_31.addWidget(self.widget_28)
        self.verticalLayout_27.addWidget(self.frame_35)
        self.widget_21 = QtWidgets.QWidget(self.Test)
        self.widget_21.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.widget_21)
        self.horizontalLayout_32.setContentsMargins(0, 0, 14, 0)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.widget_26 = QtWidgets.QWidget(self.widget_21)
        self.widget_26.setObjectName("widget_26")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.widget_26)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.frame_36 = QtWidgets.QFrame(self.widget_26)
        self.frame_36.setMaximumSize(QtCore.QSize(16777215, 64))
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_36)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 9)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.button_Train_expert = QtWidgets.QToolButton(self.frame_36)
        self.button_Train_expert.setMinimumSize(QtCore.QSize(45, 45))
        self.button_Train_expert.setMaximumSize(QtCore.QSize(45, 45))
        self.button_Train_expert.setStyleSheet("border-radius: 19px; \n"
"background-color: None;\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.button_Train_expert.setText("")
        self.button_Train_expert.setIcon(icon4)
        self.button_Train_expert.setIconSize(QtCore.QSize(90, 90))
        self.button_Train_expert.setCheckable(False)
        self.button_Train_expert.setAutoRepeat(False)
        self.button_Train_expert.setAutoExclusive(False)
        self.button_Train_expert.setObjectName("button_Train_expert")
        self.verticalLayout_26.addWidget(self.button_Train_expert, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.gridLayout_15.addWidget(self.frame_36, 0, 0, 1, 1)
        self.progressBar_expert = QtWidgets.QLabel(self.widget_26)
        self.progressBar_expert.setMinimumSize(QtCore.QSize(160, 23))
        self.progressBar_expert.setMaximumSize(QtCore.QSize(160, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.progressBar_expert.setFont(font)
        self.progressBar_expert.setStyleSheet("    background-color: rgb(27, 37, 44);;\n"
"    border-radius:8px;")
        self.progressBar_expert.setText("")
        self.progressBar_expert.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_expert.setObjectName("progressBar_expert")
        self.gridLayout_15.addWidget(self.progressBar_expert, 0, 1, 1, 1)
        self.horizontalLayout_32.addWidget(self.widget_26)
        self.Label_Train_expert = QtWidgets.QLabel(self.widget_21)
        self.Label_Train_expert.setMinimumSize(QtCore.QSize(35, 35))
        self.Label_Train_expert.setMaximumSize(QtCore.QSize(35, 35))
        self.Label_Train_expert.setText("")
        self.Label_Train_expert.setPixmap(QtGui.QPixmap("images/output-onlinepngtools (6).png"))
        self.Label_Train_expert.setScaledContents(True)
        self.Label_Train_expert.setObjectName("Label_Train_expert")
        self.horizontalLayout_32.addWidget(self.Label_Train_expert)
        self.verticalLayout_27.addWidget(self.widget_21)
        self.widget_29 = QtWidgets.QWidget(self.Test)
        self.widget_29.setObjectName("widget_29")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.widget_29)
        self.horizontalLayout_35.setContentsMargins(0, 0, 14, 0)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.widget_30 = QtWidgets.QWidget(self.widget_29)
        self.widget_30.setObjectName("widget_30")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.widget_30)
        self.horizontalLayout_39.setContentsMargins(0, 4, 0, 4)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.frame_37 = QtWidgets.QFrame(self.widget_30)
        self.frame_37.setMaximumSize(QtCore.QSize(62, 16777215))
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.bouton_Load_model = QtWidgets.QToolButton(self.frame_37)
        self.bouton_Load_model.setMinimumSize(QtCore.QSize(0, 0))
        self.bouton_Load_model.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bouton_Load_model.setStyleSheet("background-repeat: no-repeat;\n"
"background-position: center;\n"
"\n"
"border-radius: 20px;")
        self.bouton_Load_model.setText("")
        self.bouton_Load_model.setIcon(icon6)
        self.bouton_Load_model.setIconSize(QtCore.QSize(70, 70))
        self.bouton_Load_model.setObjectName("bouton_Load_model")
        self.verticalLayout_29.addWidget(self.bouton_Load_model, 0, QtCore.Qt.AlignHCenter)
        self.label_29 = QtWidgets.QLabel(self.frame_37)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(208, 208, 208);")
        self.label_29.setObjectName("label_29")
        self.verticalLayout_29.addWidget(self.label_29, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_39.addWidget(self.frame_37)
        self.txt_box_load_model = QtWidgets.QLabel(self.widget_30)
        self.txt_box_load_model.setMinimumSize(QtCore.QSize(160, 23))
        self.txt_box_load_model.setMaximumSize(QtCore.QSize(160, 19))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.txt_box_load_model.setFont(font)
        self.txt_box_load_model.setStyleSheet("    background-color: rgb(27, 37, 44);;\n"
"    border-radius:8px;")
        self.txt_box_load_model.setText("")
        self.txt_box_load_model.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_box_load_model.setObjectName("txt_box_load_model")
        self.horizontalLayout_39.addWidget(self.txt_box_load_model)
        self.horizontalLayout_35.addWidget(self.widget_30, 0, QtCore.Qt.AlignLeft)
        self.Load_Model_expert = QtWidgets.QLabel(self.widget_29)
        self.Load_Model_expert.setMinimumSize(QtCore.QSize(35, 35))
        self.Load_Model_expert.setMaximumSize(QtCore.QSize(35, 35))
        self.Load_Model_expert.setText("")
        self.Load_Model_expert.setPixmap(QtGui.QPixmap("images/output-onlinepngtools (6).png"))
        self.Load_Model_expert.setScaledContents(True)
        self.Load_Model_expert.setObjectName("Load_Model_expert")
        self.horizontalLayout_35.addWidget(self.Load_Model_expert)
        self.verticalLayout_27.addWidget(self.widget_29)
        self.horizontalLayout_24.addWidget(self.Test)
        self.line_7 = QtWidgets.QFrame(self.frame_24)
        self.line_7.setMinimumSize(QtCore.QSize(0, 177))
        self.line_7.setMaximumSize(QtCore.QSize(16777215, 177))
        self.line_7.setStyleSheet("background-color: rgb(27, 37, 44);")
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_24.addWidget(self.line_7)
        self.widget_25 = QtWidgets.QWidget(self.frame_24)
        self.widget_25.setMaximumSize(QtCore.QSize(150, 16777215))
        self.widget_25.setObjectName("widget_25")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.widget_25)
        self.verticalLayout_25.setContentsMargins(5, 7, 5, 5)
        self.verticalLayout_25.setSpacing(7)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_24 = QtWidgets.QLabel(self.widget_25)
        self.label_24.setMinimumSize(QtCore.QSize(0, 16))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(208, 208, 208);\n"
"border-radius: none;\n"
"border-top: 20px;")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_25.addWidget(self.label_24)
        self.widget_23 = QtWidgets.QWidget(self.widget_25)
        self.widget_23.setStyleSheet("background-color: rgb(27, 37, 44);\n"
"")
        self.widget_23.setObjectName("widget_23")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.widget_23)
        self.gridLayout_14.setContentsMargins(2, 0, 0, 3)
        self.gridLayout_14.setHorizontalSpacing(0)
        self.gridLayout_14.setVerticalSpacing(4)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.widget_24 = QtWidgets.QWidget(self.widget_23)
        self.widget_24.setStyleSheet("")
        self.widget_24.setObjectName("widget_24")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.widget_24)
        self.horizontalLayout_30.setContentsMargins(0, 0, 57, 2)
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_21 = QtWidgets.QLabel(self.widget_24)
        self.label_21.setMinimumSize(QtCore.QSize(45, 10))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("\n"
"color: rgb(208, 208, 208);")
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_30.addWidget(self.label_21)
        self.Supp_Expert = QtWidgets.QToolButton(self.widget_24)
        self.Supp_Expert.setMinimumSize(QtCore.QSize(35, 35))
        self.Supp_Expert.setMaximumSize(QtCore.QSize(35, 35))
        self.Supp_Expert.setStyleSheet("border-radius: 19px; \n"
"background-color: None;\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.Supp_Expert.setText("")
        self.Supp_Expert.setIcon(icon)
        self.Supp_Expert.setIconSize(QtCore.QSize(90, 90))
        self.Supp_Expert.setCheckable(False)
        self.Supp_Expert.setAutoRepeat(False)
        self.Supp_Expert.setAutoExclusive(False)
        self.Supp_Expert.setObjectName("Supp_Expert")
        self.horizontalLayout_30.addWidget(self.Supp_Expert, 0, QtCore.Qt.AlignLeft)
        self.gridLayout_14.addWidget(self.widget_24, 1, 0, 1, 1)
        self.listImages_expert = QtWidgets.QListWidget(self.widget_23)
        self.listImages_expert.setStyleSheet("    QListWidget{\n"
"color: rgb(208, 208, 208);\n"
"background-color: #283741\n"
"selection-background-color: #0099ff;\n"
"border-radius: 10px;\n"
"}\n"
"        QScrollBar:vertical {    \n"
"          \n"
"            background:rgba(40,55,65,255);\n"
"            width:15px;\n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {\n"
"            background:rgba(40,55,65,255);\n"
"            min-height: 0px;\n"
"        }\n"
"        QScrollBar::add-line:vertical {\n"
"background-color:white\n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"background-color:white;\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.listImages_expert.setObjectName("listImages_expert")
        self.gridLayout_14.addWidget(self.listImages_expert, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_25.addWidget(self.widget_23)
        self.horizontalLayout_24.addWidget(self.widget_25)
        self.line_6 = QtWidgets.QFrame(self.frame_24)
        self.line_6.setMinimumSize(QtCore.QSize(0, 177))
        self.line_6.setMaximumSize(QtCore.QSize(16777215, 177))
        self.line_6.setStyleSheet("background-color: rgb(27, 37, 44);")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_24.addWidget(self.line_6)
        self.Acquisition = QtWidgets.QFrame(self.frame_24)
        self.Acquisition.setMinimumSize(QtCore.QSize(0, 0))
        self.Acquisition.setMaximumSize(QtCore.QSize(205, 16777215))
        self.Acquisition.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Acquisition.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Acquisition.setObjectName("Acquisition")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.Acquisition)
        self.verticalLayout_24.setContentsMargins(0, 7, -1, 3)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_9 = QtWidgets.QLabel(self.Acquisition)
        self.label_9.setMinimumSize(QtCore.QSize(0, 16))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(208, 208, 208);\n"
"border-radius: none;\n"
"border-top: 20px;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_24.addWidget(self.label_9)
        self.frame_34 = QtWidgets.QFrame(self.Acquisition)
        self.frame_34.setMaximumSize(QtCore.QSize(16777215, 58))
        self.frame_34.setStyleSheet("border-radius: 10px;")
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_29.setContentsMargins(0, 0, 13, 0)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.bouton_parcourir = QtWidgets.QToolButton(self.frame_34)
        self.bouton_parcourir.setMinimumSize(QtCore.QSize(0, 0))
        self.bouton_parcourir.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bouton_parcourir.setStyleSheet("background-repeat: no-repeat;\n"
"background-position: center;\n"
"\n"
"border-radius: 20px;")
        self.bouton_parcourir.setText("")
        self.bouton_parcourir.setIcon(icon6)
        self.bouton_parcourir.setIconSize(QtCore.QSize(70, 70))
        self.bouton_parcourir.setObjectName("bouton_parcourir")
        self.horizontalLayout_29.addWidget(self.bouton_parcourir)
        self.txt_box = QtWidgets.QLineEdit(self.frame_34)
        self.txt_box.setMaximumSize(QtCore.QSize(208, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txt_box.setFont(font)
        self.txt_box.setStyleSheet("background-color: rgb(27, 37, 44);\n"
"color: rgb(208, 208, 208);\n"
"selection-background-color: rgba(16,25,30,255);\n"
"border-radius: 10px;")
        self.txt_box.setText("")
        self.txt_box.setObjectName("txt_box")
        self.horizontalLayout_29.addWidget(self.txt_box)
        self.verticalLayout_24.addWidget(self.frame_34)
        self.frame_27 = QtWidgets.QFrame(self.Acquisition)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.widget_22 = QtWidgets.QWidget(self.frame_27)
        self.widget_22.setMaximumSize(QtCore.QSize(16777215, 76))
        self.widget_22.setObjectName("widget_22")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.widget_22)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.SaveImg = QtWidgets.QToolButton(self.widget_22)
        self.SaveImg.setMinimumSize(QtCore.QSize(45, 45))
        self.SaveImg.setMaximumSize(QtCore.QSize(45, 45))
        self.SaveImg.setStyleSheet("border-radius: 19px; \n"
"background-color: None;\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.SaveImg.setText("")
        self.SaveImg.setIcon(icon1)
        self.SaveImg.setIconSize(QtCore.QSize(90, 90))
        self.SaveImg.setCheckable(False)
        self.SaveImg.setAutoRepeat(False)
        self.SaveImg.setAutoExclusive(False)
        self.SaveImg.setObjectName("SaveImg")
        self.verticalLayout_23.addWidget(self.SaveImg, 0, QtCore.Qt.AlignHCenter)
        self.label_20 = QtWidgets.QLabel(self.widget_22)
        self.label_20.setMinimumSize(QtCore.QSize(0, 15))
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(208, 208, 208);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_23.addWidget(self.label_20, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_28.addWidget(self.widget_22)
        self.frame_33 = QtWidgets.QFrame(self.frame_27)
        self.frame_33.setMinimumSize(QtCore.QSize(0, 98))
        self.frame_33.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_33)
        self.horizontalLayout_27.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.middele_circle_frame_6 = QtWidgets.QFrame(self.frame_33)
        self.middele_circle_frame_6.setMinimumSize(QtCore.QSize(81, 81))
        self.middele_circle_frame_6.setMaximumSize(QtCore.QSize(81, 81))
        self.middele_circle_frame_6.setStyleSheet("background-color: None;\n"
"\n"
"border: 7px solid rgb(27, 37, 44);;\n"
"border-radius:40px; /*50% of it\'s size*/\n"
"\n"
"")
        self.middele_circle_frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.middele_circle_frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.middele_circle_frame_6.setObjectName("middele_circle_frame_6")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.middele_circle_frame_6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.nb_img_expert = QtWidgets.QLabel(self.middele_circle_frame_6)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.nb_img_expert.setFont(font)
        self.nb_img_expert.setStyleSheet("  border: 2px ;\n"
"background-color: None;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"")
        self.nb_img_expert.setAlignment(QtCore.Qt.AlignCenter)
        self.nb_img_expert.setObjectName("nb_img_expert")
        self.gridLayout_13.addWidget(self.nb_img_expert, 0, 0, 1, 1)
        self.horizontalLayout_27.addWidget(self.middele_circle_frame_6, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_28.addWidget(self.frame_33)
        self.verticalLayout_24.addWidget(self.frame_27)
        self.horizontalLayout_24.addWidget(self.Acquisition)
        self.line_5 = QtWidgets.QFrame(self.frame_24)
        self.line_5.setMinimumSize(QtCore.QSize(0, 177))
        self.line_5.setMaximumSize(QtCore.QSize(3, 177))
        self.line_5.setStyleSheet("background-color: rgb(27, 37, 44);")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_24.addWidget(self.line_5)
        self.Controle_camera = QtWidgets.QFrame(self.frame_24)
        self.Controle_camera.setMinimumSize(QtCore.QSize(0, 0))
        self.Controle_camera.setMaximumSize(QtCore.QSize(197, 16777215))
        self.Controle_camera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Controle_camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Controle_camera.setObjectName("Controle_camera")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.Controle_camera)
        self.verticalLayout_22.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_8 = QtWidgets.QLabel(self.Controle_camera)
        self.label_8.setMinimumSize(QtCore.QSize(0, 16))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(208, 208, 208);\n"
"border-radius: none;\n"
"border-top: 20px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_22.addWidget(self.label_8)
        self.widget_20 = QtWidgets.QWidget(self.Controle_camera)
        self.widget_20.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.widget_20)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.frame_25 = QtWidgets.QFrame(self.widget_20)
        self.frame_25.setMinimumSize(QtCore.QSize(140, 0))
        self.frame_25.setMaximumSize(QtCore.QSize(140, 16777215))
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.slider_exposure_time_expert = QtWidgets.QSlider(self.frame_25)
        self.slider_exposure_time_expert.setMinimumSize(QtCore.QSize(112, 60))
        self.slider_exposure_time_expert.setStyleSheet("QSlider:horizontal {\n"
"    min-height: 60px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    height: 1px;\n"
"    background: white; \n"
"}\n"
"QSlider::handle:horizontal {\n"
"    width: 30px;\n"
"    margin-top: -15px;\n"
"    margin-bottom: -15px;\n"
"    border-radius: 15px;\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(210, 210, 210, 255), stop:0.7 rgba(210, 210, 210, 100));\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(spread:reflect, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 rgba(255, 255, 255, 255), stop:0.7 rgba(255, 255, 255, 100));\n"
"}")
        self.slider_exposure_time_expert.setMaximum(1000)
        self.slider_exposure_time_expert.setSingleStep(1)
        self.slider_exposure_time_expert.setProperty("value", 240)
        self.slider_exposure_time_expert.setOrientation(QtCore.Qt.Horizontal)
        self.slider_exposure_time_expert.setObjectName("slider_exposure_time_expert")
        self.verticalLayout_20.addWidget(self.slider_exposure_time_expert, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_25.addWidget(self.frame_25)
        self.frame_26 = QtWidgets.QFrame(self.widget_20)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_26)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.slider_exposure_label_expert = QtWidgets.QLabel(self.frame_26)
        self.slider_exposure_label_expert.setMinimumSize(QtCore.QSize(67, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.slider_exposure_label_expert.setFont(font)
        self.slider_exposure_label_expert.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.slider_exposure_label_expert.setAlignment(QtCore.Qt.AlignCenter)
        self.slider_exposure_label_expert.setObjectName("slider_exposure_label_expert")
        self.gridLayout_10.addWidget(self.slider_exposure_label_expert, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.horizontalLayout_25.addWidget(self.frame_26)
        self.verticalLayout_22.addWidget(self.widget_20)
        self.frame_30 = QtWidgets.QFrame(self.Controle_camera)
        self.frame_30.setMinimumSize(QtCore.QSize(0, 89))
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.frame_31 = QtWidgets.QFrame(self.frame_30)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_31)
        self.gridLayout_11.setContentsMargins(0, 9, 0, 18)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_17 = QtWidgets.QLabel(self.frame_31)
        self.label_17.setMinimumSize(QtCore.QSize(0, 15))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(208, 208, 208);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_11.addWidget(self.label_17, 1, 0, 1, 1)
        self.start_expert = QtWidgets.QToolButton(self.frame_31)
        self.start_expert.setMinimumSize(QtCore.QSize(55, 55))
        self.start_expert.setMaximumSize(QtCore.QSize(55, 55))
        self.start_expert.setStyleSheet("border-radius: 19px; \n"
"background-color: None;\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.start_expert.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/button_start_stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("images/output-onlinepngtools (5).png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.start_expert.setIcon(icon7)
        self.start_expert.setIconSize(QtCore.QSize(90, 90))
        self.start_expert.setCheckable(False)
        self.start_expert.setAutoRepeat(False)
        self.start_expert.setAutoExclusive(False)
        self.start_expert.setObjectName("start_expert")
        self.gridLayout_11.addWidget(self.start_expert, 0, 0, 1, 1)
        self.horizontalLayout_26.addWidget(self.frame_31, 0, QtCore.Qt.AlignHCenter)
        self.frame_32 = QtWidgets.QFrame(self.frame_30)
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_32)
        self.gridLayout_12.setContentsMargins(0, 6, 0, 18)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.stop_expert = QtWidgets.QToolButton(self.frame_32)
        self.stop_expert.setEnabled(True)
        self.stop_expert.setMinimumSize(QtCore.QSize(55, 55))
        self.stop_expert.setMaximumSize(QtCore.QSize(55, 55))
        self.stop_expert.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stop_expert.setStyleSheet("border-radius: 19px; \n"
"background-color: None;\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.stop_expert.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/Stopp.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap("images/output-onlinepngtools (4).png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.stop_expert.setIcon(icon8)
        self.stop_expert.setIconSize(QtCore.QSize(80, 80))
        self.stop_expert.setObjectName("stop_expert")
        self.gridLayout_12.addWidget(self.stop_expert, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_19 = QtWidgets.QLabel(self.frame_32)
        self.label_19.setMinimumSize(QtCore.QSize(0, 15))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(208, 208, 208);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_12.addWidget(self.label_19, 1, 0, 1, 1)
        self.horizontalLayout_26.addWidget(self.frame_32, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_22.addWidget(self.frame_30)
        self.horizontalLayout_24.addWidget(self.Controle_camera)
        self.horizontalLayout_22.addWidget(self.frame_24)
        self.verticalLayout_17.addWidget(self.widget_18)
        self.verticalLayout_18.addWidget(self.widget_16)
        self.tabWidget_2.addTab(self.Expert, "")
        self.verticalLayout_11.addWidget(self.tabWidget_2)
        self.verticalLayout.addWidget(self.main_body_contents)
        self.horizontalLayout.addWidget(self.main_body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cetim"))
        self.statut_2.setText(_translate("MainWindow", "STATUT OK"))
        self.label_3.setText(_translate("MainWindow", "Anomaly Detection"))
        self.heatmap.setText(_translate("MainWindow", "Heatmap"))
        self.mask.setText(_translate("MainWindow", "Mask"))
        self.label_18.setText(_translate("MainWindow", "    delete "))
        self.label_5.setText(_translate("MainWindow", "Camera Control"))
        self.slider_exposure_label.setText(_translate("MainWindow", "24"))
        self.label_10.setText(_translate("MainWindow", "Acquire Frame"))
        self.label_12.setText(_translate("MainWindow", "Start/Stop Movie"))
        self.nb_img_train.setText(_translate("MainWindow", "0"))
        self.cursor_mask_label.setText(_translate("MainWindow", "0.77"))
        self.label_16.setText(_translate("MainWindow", "Restart"))
        self.label_6.setText(_translate("MainWindow", "AI"))
        self.model_combo.setItemText(0, _translate("MainWindow", "Resnet18"))
        self.model_combo.setItemText(1, _translate("MainWindow", "Resnet50"))
        self.label_11.setText(_translate("MainWindow", "Train"))
        self.label_13.setText(_translate("MainWindow", "Add to Train"))
        self.label_14.setText(_translate("MainWindow", "Score :"))
        self.label_15.setText(_translate("MainWindow", "Threshold :"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Production), _translate("MainWindow", "Production"))
        self.heatmap_expert.setText(_translate("MainWindow", "Heatmap"))
        self.mask_expert.setText(_translate("MainWindow", "Mask"))
        self.label_25.setText(_translate("MainWindow", "Test"))
        self.test_img.setText(_translate("MainWindow", "Load image"))
        self.live.setText(_translate("MainWindow", "Live"))
        self.label_28.setText(_translate("MainWindow", "Mask :"))
        self.cursor_mask_label_expert.setText(_translate("MainWindow", "0.77"))
        self.label_27.setText(_translate("MainWindow", "Threshold :"))
        self.label_30.setText(_translate("MainWindow", "Score :"))
        self.score_label_expert.setText(_translate("MainWindow", "0"))
        self.label_22.setText(_translate("MainWindow", "Train"))
        self.label_23.setText(_translate("MainWindow", "Load images"))
        self.label_29.setText(_translate("MainWindow", "Load model"))
        self.label_24.setText(_translate("MainWindow", "Visualisation "))
        self.label_21.setText(_translate("MainWindow", "    delete "))
        self.label_9.setText(_translate("MainWindow", "Acquisition"))
        self.label_20.setText(_translate("MainWindow", "Save"))
        self.nb_img_expert.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Camera Control"))
        self.slider_exposure_label_expert.setText(_translate("MainWindow", "24"))
        self.label_17.setText(_translate("MainWindow", "Start"))
        self.label_19.setText(_translate("MainWindow", "Stop"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Expert), _translate("MainWindow", "Expert"))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

