# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Main_Page.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_page(object):
    def setupUi(self, Main_page):
        Main_page.setObjectName("Main_page")
        Main_page.resize(617, 534)
        self.label = QtWidgets.QLabel(Main_page)
        self.label.setGeometry(QtCore.QRect(470, 470, 141, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Pictures/ntu_logo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Main_page)
        self.label_3.setGeometry(QtCore.QRect(60, 10, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Main_page)
        self.label_4.setGeometry(QtCore.QRect(0, 220, 181, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Pictures/Capture.PNG"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Main_page)
        self.label_2.setGeometry(QtCore.QRect(230, 140, 141, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Pictures/McDonald.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Main_page)
        self.label_5.setGeometry(QtCore.QRect(230, 370, 141, 131))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Pictures/39840570-nasi-goreng-icon-indonesian-fried-rice.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Main_page)
        self.label_7.setGeometry(QtCore.QRect(0, 10, 611, 521))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Pictures/cpix.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_5.raise_()

        self.retranslateUi(Main_page)
        QtCore.QMetaObject.connectSlotsByName(Main_page)

    def retranslateUi(self, Main_page):
        _translate = QtCore.QCoreApplication.translate
        Main_page.setWindowTitle(_translate("Main_page", "Form"))
        self.label_3.setText(_translate("Main_page", "Welcome To Canteen Information System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_page = QtWidgets.QWidget()
    ui = Ui_Main_page()
    ui.setupUi(Main_page)
    Main_page.show()
    sys.exit(app.exec_())
