# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chessui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
#import RES
from chessBoard import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
class Ui_Form(QWidget):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(800, 600)
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.playmodeBox = QtWidgets.QComboBox(widget)
        self.playmodeBox.setObjectName("playmodeBox")
        self.playmodeBox.addItem("人人对战")
        self.playmodeBox.addItem("人机对战")
        self.verticalLayout_2.addWidget(self.playmodeBox)
        self.label_3 = QtWidgets.QLabel(widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.timeBox = QtWidgets.QComboBox(widget)
        self.timeBox.setObjectName("timeBox")
        self.timeBox.addItem("20秒")
        self.timeBox.addItem("60秒")
        self.timeBox.addItem("120秒")
        self.timeBox.addItem("600秒")
        self.verticalLayout_2.addWidget(self.timeBox)
        self.label = QtWidgets.QLabel(widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lcurrentPlayer = QtWidgets.QLineEdit(widget)
        self.lcurrentPlayer.setObjectName("lcurrentPlayer")
        self.verticalLayout_2.addWidget(self.lcurrentPlayer)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.startButton = QtWidgets.QPushButton(widget)
        self.startButton.setObjectName("startButton")
        self.verticalLayout_2.addWidget(self.startButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pauseButton = QtWidgets.QPushButton(widget)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout.addWidget(self.pauseButton)
        self.endButton = QtWidgets.QPushButton(widget)
        self.endButton.setObjectName("endButton")
        self.horizontalLayout.addWidget(self.endButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.timeCount = QtWidgets.QLCDNumber(widget)
        self.timeCount.setObjectName("timeCount")
        self.verticalLayout_2.addWidget(self.timeCount, 0, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.listWidget = QtWidgets.QListWidget(widget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.board = chessBoard(widget)
        self.board.setMinimumSize(QtCore.QSize(520, 576))
        self.board.setObjectName("board")
        
        self.verticalLayout.addWidget(self.board)
        
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 3, 1, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)
        

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "中国象棋"))
        self.label_2.setText(_translate("widget", "游戏模式"))
        self.label_3.setText(_translate("widget", "限时"))
        self.label.setText(_translate("widget", "目前玩家"))
        self.startButton.setText(_translate("widget", "开始"))
        self.pauseButton.setText(_translate("widget", "暂停"))
        self.endButton.setText(_translate("widget", "结束"))
        self.label_4.setText(_translate("widget", "剩余时间"))

