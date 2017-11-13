# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 327)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 54, 12))
        self.label.setObjectName("label")
        self.iconNum = -1
        self.start = False

        self.horizontalLayoutWidget =[]
        self.horizontalLayout = []
        for i in range(3):
            horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
            horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 40+i*90, 274, 91))
            horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
            horizontalLayout = QtWidgets.QHBoxLayout(horizontalLayoutWidget)
            horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
            horizontalLayout.setContentsMargins(0, 0, 0, 0)
            horizontalLayout.setSpacing(0)
            horizontalLayout.setObjectName("horizontalLayout")
            self.horizontalLayoutWidget.append(horizontalLayoutWidget)
            self.horizontalLayout.append(horizontalLayout)
        
        self.pushButton =[]
        for i in range(3):
            for j in range(3):
                pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget[i])
                pushButton.setEnabled(True)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(pushButton.sizePolicy().hasHeightForWidth())
                pushButton.setSizePolicy(sizePolicy)
                pushButton.setMaximumSize(QtCore.QSize(90, 90))
                pushButton.setText("")
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("dog.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
                pushButton.setIcon(icon)
                pushButton.setIconSize(QtCore.QSize(80, 80))
                pushButton.setObjectName("pushButton")
                self.horizontalLayout[i].addWidget(pushButton)
                if j == 0:
                    self.pushButton.append([])
                    self.pushButton[i].append(pushButton)
                else:
                    self.pushButton[i].append(pushButton)

        self.pushButton[0][0].clicked.connect(lambda:self.changeIcon(0,0))
        self.pushButton[0][1].clicked.connect(lambda:self.changeIcon(0,1))
        self.pushButton[0][2].clicked.connect(lambda:self.changeIcon(0,2))
        self.pushButton[1][0].clicked.connect(lambda:self.changeIcon(1,0))
        self.pushButton[1][1].clicked.connect(lambda:self.changeIcon(1,1))
        self.pushButton[1][2].clicked.connect(lambda:self.changeIcon(1,2))
        self.pushButton[2][0].clicked.connect(lambda:self.changeIcon(2,0))
        self.pushButton[2][1].clicked.connect(lambda:self.changeIcon(2,1))
        self.pushButton[2][2].clicked.connect(lambda:self.changeIcon(2,2))
                        
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(320, 50, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(320, 80, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(320, 150, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(320, 180, 89, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(330, 230, 51, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.onStartBtn)
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(330, 280, 51, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        
        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "井字棋"))
        self.radioButton.setText(_translate("Dialog", "先手"))
        self.radioButton_2.setText(_translate("Dialog", "后手"))
        self.radioButton_3.setText(_translate("Dialog", "人机对战"))
        self.radioButton_4.setText(_translate("Dialog", "人人对战"))
        self.pushButton_10.setText(_translate("Dialog", "开始"))
        self.pushButton_11.setText(_translate("Dialog", "退出"))

    def changeIcon(self,i,j):
        if self.start:
            icon = QtGui.QIcon()
            if self.iconNum == -1:
                icon.addPixmap(QtGui.QPixmap("O.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
            else:
                icon.addPixmap(QtGui.QPixmap("X.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
            self.iconNum *= -1
            self.pushButton[i][j].setIcon(icon)
            self.pushButton[i][j].setIconSize(QtCore.QSize(80, 80))

    def onStartBtn(self):
        self.start = True
        self.pushButton_10.checkable = True
        self.pushButton_10.checked = True
        
if __name__ == "__main__":   
    app = QApplication(sys.argv)   
    myapp = Ui_Dialog()   #MyForm是自己的窗体类名
    myapp.setupUi(myapp)
    myapp.show()   
    sys.exit(app.exec_())  
