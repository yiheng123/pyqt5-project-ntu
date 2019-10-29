
from PyQt5.QtWidgets import QWidget ,QMessageBox,QApplication,QStackedWidget ,QHeaderView,QVBoxLayout ,QFrame,QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, QTimer,QDate, QTime
import os
from datetime import datetime
import pytz


class Ui_Cart_and_Pay(QWidget):
     def __init__(self,parent=None):
        super(Ui_Cart_and_Pay,self).__init__(parent)
        self.setup_Ui()

    def setup_Ui(self):
        self.setObjectName("Cart_and_Pay")
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
        self.BlueButton = QtWidgets.QPushButton(self)
        self.BlueButton.setGeometry(QtCore.QRect(30, 430, 96, 96))
        self.BlueButton.setStyleSheet("#BlueButton {\n"
"    background-color: #303d5e;\n"
"    /*限制最小最大尺寸*/\n"
"    min-width: 96px;\n"
"    max-width: 96px;\n"
"    min-height: 96px;\n"
"    max-height: 96px;\n"
"    border-radius: 48px; /*圆形*/\n"
"}\n"
"#BlueButton:hover {\n"
"    background-color: #516cb0;\n"
"}\n"
"#BlueButton:pressed {\n"
"    background-color: #04070f;\n"
"}")
        self.BlueButton.setObjectName("BlueButton")
        self.BlueButton2 = QtWidgets.QPushButton(Cart_and_Pay)
        self.BlueButton2.setGeometry(QtCore.QRect(240, 430, 96, 96))
        self.BlueButton2.setStyleSheet("#BlueButton2{\n"
"    background-color: #303d5e;\n"
"    /*限制最小最大尺寸*/\n"
"    min-width: 96px;\n"
"    max-width: 96px;\n"
"    min-height: 96px;\n"
"    max-height: 96px;\n"
"    border-radius: 48px; /*圆形*/\n"
"}\n"
"#BlueButton2:hover {\n"
"    background-color: #516cb0;\n"
"}\n"
"#BlueButton2:pressed {\n"
"    background-color: #04070f;\n"
"}")
        self.BlueButton2.setObjectName("BlueButton2")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(400, 90, 341, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Cart_and_Pay", "Form"))
        self.label_2.setText(_translate("Cart_and_Pay", "Pay Your Bill Here"))
        self.BlueButton.setText(_translate("Cart_and_Pay", "Waiting Time"))
        self.BlueButton2.setText(_translate("Cart_and_Pay", "Pay"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cart_and_Pay = QtWidgets.QWidget()
    ui = Ui_Cart_and_Pay()
    ui.setupUi(Cart_and_Pay)
    Cart_and_Pay.show()
    sys.exit(app.exec_())
