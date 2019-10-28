# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\cart_and_pay.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cart_and_Pay(object):
    def setupUi(self, Cart_and_Pay):
        Cart_and_Pay.setObjectName("Cart_and_Pay")
        Cart_and_Pay.resize(800, 600)
        self.label = QtWidgets.QLabel(Cart_and_Pay)
        self.label.setGeometry(QtCore.QRect(20, 90, 331, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Pictures/NTU.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Cart_and_Pay)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tableView = QtWidgets.QTableView(Cart_and_Pay)
        self.tableView.setGeometry(QtCore.QRect(400, 90, 381, 411))
        self.tableView.setObjectName("tableView")
        self.BlueButton = QtWidgets.QPushButton(Cart_and_Pay)
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

        self.retranslateUi(Cart_and_Pay)
        QtCore.QMetaObject.connectSlotsByName(Cart_and_Pay)

    def retranslateUi(self, Cart_and_Pay):
        _translate = QtCore.QCoreApplication.translate
        Cart_and_Pay.setWindowTitle(_translate("Cart_and_Pay", "Form"))
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
