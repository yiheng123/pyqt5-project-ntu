# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\wait_time.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 410, 141, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Pictures/ntu_lion.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 400, 551, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Pictures/Queuing.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(180, 40, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(310, 150, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(190, 160, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(190, 230, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.BlueButton = QtWidgets.QPushButton(Form)
        self.BlueButton.setGeometry(QtCore.QRect(530, 130, 72, 72))
        self.BlueButton.setStyleSheet("#BlueButton {\n"
"    background-color: #303d5e;\n"
"    min-width: 72px;\n"
"    max-width: 72px;\n"
"    min-height: 72px;\n"
"    max-height: 72px;\n"
"    border-radius: 36px; \n"
"    color: #FFFFFF;\n"
"}\n"
"#BlueButton:hover {\n"
"    background-color: #516cb0;\n"
"}\n"
"#BlueButton:pressed {\n"
"    background-color: #04070f;\n"
"}")
        self.BlueButton.setObjectName("BlueButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Enter the number of people in front of you"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">asd</p></body></html>"))
        self.label_4.setText(_translate("Form", "Number:"))
        self.label_5.setText(_translate("Form", "Your estimating waiting time is 5 mins"))
        self.BlueButton.setText(_translate("Form", "Click"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
