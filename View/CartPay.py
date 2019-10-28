from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget ,QMessageBox,QApplication,QStackedWidget ,QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, QTimer,QDate, QTime
import os
from datetime import datetime
import pytz

class Pay_First_Page(QWidget):
    #initialize
    def __init__(self,parent=None):
        super(Pay_First_Page,self).__init__(parent)
        self.setup_Ui()
    
    def setup_Ui(self):
        self.setObjectName("Pay_First_Page")
        self.resize(800, 600)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 90, 331, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Pictures/NTU.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setGeometry(QtCore.QRect(400, 90, 381, 411))
        self.tableView.setObjectName("tableView")
        self.BlueButton = QtWidgets.QPushButton(self)
        self.BlueButton.setGeometry(QtCore.QRect(30, 430, 96, 96))
        self.BlueButton.setStyleSheet("#BlueButton {\n"
"    background-color: #303d5e;\n"
"    min-width: 96px;\n"
"    max-width: 96px;\n"
"    min-height: 96px;\n"
"    max-height: 96px;\n"
"    border-radius: 48px; \n"
"}\n"
"#BlueButton:hover {\n"
"    background-color: #516cb0;\n"
"}\n"
"#BlueButton:pressed {\n"
"    background-color: #04070f;\n"
"}")
        self.BlueButton.setObjectName("BlueButton")
        self.BlueButton2 = QtWidgets.QPushButton(self)
        self.BlueButton2.setGeometry(QtCore.QRect(240, 430, 96, 96))
        self.BlueButton2.setStyleSheet("#BlueButton2{\n"
"    background-color: #303d5e;\n"
"    min-width: 96px;\n"
"    max-width: 96px;\n"
"    min-height: 96px;\n"
"    max-height: 96px;\n"
"    border-radius: 48px; n"
"}\n"
"#BlueButton2:hover {\n"
"    background-color: #516cb0;\n"
"}\n"
"#BlueButton2:pressed {\n"
"    background-color: #04070f;\n"
"}")
        self.BlueButton2.setObjectName("BlueButton2")
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Cart_and_Pay", "Form"))
        self.label_2.setText(_translate("Cart_and_Pay", "Pay Your Bill Here"))
        self.BlueButton.setText(_translate("Cart_and_Pay", "Waiting Time"))
        self.BlueButton2.setText(_translate("Cart_and_Pay", "Pay"))
if __name__ == '__main__':
    import sys
    
    app =QtWidgets.QApplication(sys.argv)
    w = Pay_First_Page()
    w.show()
    sys.exit(app.exec_())