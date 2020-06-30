import Main_Page
from PyQt5.QtWidgets import QApplication
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QListWidget, QStackedWidget, QHBoxLayout, QListWidgetItem, QLabel , QMessageBox
import sys
import pytz
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QSize 
from PyQt5.QtGui import QIcon
import Main_Page

class homePG_buttonsC(QWidget):
    
    def McButton(self):

        self.McButton.setGeometry(QtCore.QRect(500, 370, 151, 111))
        self.McButton.setObjectName("McButton")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.McButton.setFont(font)
        self.McButton.setStyleSheet("#McButton{\n"
        "	 background-color: #FFC300;\n"
        "	 min-width: 120px;\n"
        "	 max-width: 120px;\n"
        "	 min-height: 95px;\n"
        "	 max-height: 85px;\n"
        "	 border-radius: 30px; \n"
        "	 color: #ED1C22;\n"
        "}\n"
        "#McButton:hover {\n"
        "	 background-color: #ED1C22;\n"
        "	 color: #FFC300;\n"
        "}\n"
        "#McButton:pressed {\n"
        "	 background-color: #FC7A08;\n"
        "	 color: #000000;\n"
        "}")

    def SubButton(self):

        self.SubButton.setGeometry(QtCore.QRect(650, 370, 151, 111))
        self.SubButton.setObjectName("SubButton")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SubButton.setFont(font)
        self.SubButton.setStyleSheet("#SubButton{\n"
        "	 background-color: #009743;\n"
        "	 min-width: 120px;\n"
        "	 max-width: 120px;\n"
        "	 min-height: 95px;\n"
        "	 max-height: 85px;\n"
        "	 border-radius: 30px; \n"
        "	 color: #ffcb0a;\n"
        "}\n"
        "#SubButton:hover {\n"
        "	 background-color: #ffcb0a;\n"
        "	 color:  #009743;\n"
        "}\n"
        "#SubButton:pressed {\n"
        "	 background-color: #94F272;\n"
        "	 color: #000000;\n"
        "}")
    def MYButton(self):

        self.MYButton.setGeometry(QtCore.QRect(500, 480, 151, 111))
        self.MYButton.setObjectName("MYButton")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MYButton.setFont(font)
        self.MYButton.setStyleSheet("#MYButton{\n"
        "	 background-color: #F720F3;\n"
        "	 min-width: 120px;\n"
        "	 max-width: 120px;\n"
        "	 min-height: 95px;\n"
        "	 max-height: 85px;\n"
        "	 border-radius: 30px; \n"
        "	 color: #009000;\n"#009000
        "}\n"
        "#MYButton:hover {\n"
        "	 background-color: #009000;\n"
        "	 color: #F720F3;\n"
        "}\n"
        "#MYButton:pressed {\n"
        "	 background-color: #89F720;\n"
        "	 color: #000000;\n"
        "}")
    def KFCButton(self):

        self.KFCButton.setGeometry(QtCore.QRect(650, 480, 151, 111))
        self.KFCButton.setObjectName("KFCButton")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.KFCButton.setFont(font)
        self.KFCButton.setStyleSheet("#KFCButton{\n"
        "	 background-color: #A3080B;\n"
        "	 min-width: 120px;\n"
        "	 max-width: 120px;\n"
        "	 min-height: 95px;\n"
        "	 max-height: 85px;\n"
        "	 border-radius: 30px; \n"
        "	 color: #FFFFFF;\n"
        "}\n"
        "#KFCButton:hover {\n"
        "	 background-color: #000000;\n"
        "	 color: #A3080B;\n"
        "}\n"
        "#KFCButton:pressed {\n"
        "	 background-color: #FFFFFF;\n"
        "	 color: #000000;\n"
        "}")

    def four_store_picF(self,texts):
        pass
        #self.stackedWidget.addWidget(self.four_store_pic.show())

    