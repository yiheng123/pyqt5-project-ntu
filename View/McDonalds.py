# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\McDonalds.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

class Ui_Mcdonalds(object):


    def setupUi(self, Mcdonalds):
        Mcdonalds.setObjectName("Mcdonalds")
        Mcdonalds.resize(800, 600)
        self.item_six_price = QtWidgets.QLabel(Mcdonalds)
        self.item_six_price.setGeometry(QtCore.QRect(280, 310, 31, 16))
        self.item_six_price.setObjectName("item_six_price")
        self.item_six_num = QtWidgets.QSpinBox(Mcdonalds)
        self.item_six_num.setGeometry(QtCore.QRect(280, 330, 42, 22))
        self.item_six_num.setObjectName("item_six_num")
        self.item_seven_pic = QtWidgets.QLabel(Mcdonalds)
        self.item_seven_pic.setGeometry(QtCore.QRect(450, 229, 100, 71))
        self.item_seven_pic.setText("")
        self.item_seven_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Mc Nugguts.png"))
        self.item_seven_pic.setScaledContents(True)
        self.item_seven_pic.setObjectName("item_seven_pic")
        self.item_eight_pic = QtWidgets.QLabel(Mcdonalds)
        self.item_eight_pic.setGeometry(QtCore.QRect(660, 219, 91, 81))
        self.item_eight_pic.setText("")
        self.item_eight_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Coke.png"))
        self.item_eight_pic.setScaledContents(True)
        self.item_eight_pic.setObjectName("item_eight_pic")
        self.item_eight_text = QtWidgets.QLabel(Mcdonalds)
        self.item_eight_text.setGeometry(QtCore.QRect(650, 290, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_eight_text.setFont(font)
        self.item_eight_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_eight_text.setObjectName("item_eight_text")
        self.item_five_num = QtWidgets.QSpinBox(Mcdonalds)
        self.item_five_num.setGeometry(QtCore.QRect(70, 330, 42, 22))
        self.item_five_num.setObjectName("item_five_num")
        self.item_five_price = QtWidgets.QLabel(Mcdonalds)
        self.item_five_price.setGeometry(QtCore.QRect(70, 310, 31, 16))
        self.item_five_price.setObjectName("item_five_price")
        self.item_seven_num = QtWidgets.QSpinBox(Mcdonalds)
        self.item_seven_num.setGeometry(QtCore.QRect(480, 330, 42, 22))
        self.item_seven_num.setObjectName("item_seven_num")
        self.item_six_text = QtWidgets.QLabel(Mcdonalds)
        self.item_six_text.setGeometry(QtCore.QRect(250, 290, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_six_text.setFont(font)
        self.item_six_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_six_text.setObjectName("item_six_text")
        self.item_seven_price = QtWidgets.QLabel(Mcdonalds)
        self.item_seven_price.setGeometry(QtCore.QRect(480, 310, 31, 16))
        self.item_seven_price.setObjectName("item_seven_price")
        self.item_five_pic = QtWidgets.QLabel(Mcdonalds)
        self.item_five_pic.setGeometry(QtCore.QRect(50, 220, 91, 71))
        self.item_five_pic.setText("")
        self.item_five_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Mc Chicken.png"))
        self.item_five_pic.setScaledContents(True)
        self.item_five_pic.setObjectName("item_five_pic")
        self.item_eight_num = QtWidgets.QSpinBox(Mcdonalds)
        self.item_eight_num.setGeometry(QtCore.QRect(690, 330, 42, 22))
        self.item_eight_num.setObjectName("item_eight_num")
        self.item_five_text = QtWidgets.QLabel(Mcdonalds)
        self.item_five_text.setGeometry(QtCore.QRect(40, 290, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_five_text.setFont(font)
        self.item_five_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_five_text.setObjectName("item_five_text")
        self.item_seven_text = QtWidgets.QLabel(Mcdonalds)
        self.item_seven_text.setGeometry(QtCore.QRect(440, 290, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_seven_text.setFont(font)
        self.item_seven_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_seven_text.setObjectName("item_seven_text")
        self.item_six_pic = QtWidgets.QLabel(Mcdonalds)
        self.item_six_pic.setGeometry(QtCore.QRect(260, 190, 100, 100))
        self.item_six_pic.setText("")
        self.item_six_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Mc Wrap.png"))
        self.item_six_pic.setScaledContents(True)
        self.item_six_pic.setObjectName("item_six_pic")
        self.item_eight_price = QtWidgets.QLabel(Mcdonalds)
        self.item_eight_price.setGeometry(QtCore.QRect(690, 310, 31, 16))
        self.item_eight_price.setObjectName("item_eight_price")
        self.item_two_price = QtWidgets.QLabel(Mcdonalds)
        self.item_two_price.setGeometry(QtCore.QRect(280, 130, 31, 16))
        self.item_two_price.setObjectName("item_two_price")
        self.item_two_num = QtWidgets.QSpinBox(Mcdonalds)
        self.item_two_num.setGeometry(QtCore.QRect(280, 150, 42, 22))
        self.item_two_num.setObjectName("item_two_num")
        self.item_three_pic = QtWidgets.QLabel(Mcdonalds)
        self.item_three_pic.setGeometry(QtCore.QRect(450, 20, 100, 100))
        self.item_three_pic.setText("")
        self.item_three_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Double Cheese Burger.png"))
        self.item_three_pic.setScaledContents(True)
        self.item_three_pic.setObjectName("item_three_pic")
        self.item_four_pic = QtWidgets.QLabel(Mcdonalds)
        self.item_four_pic.setGeometry(QtCore.QRect(670, 40, 71, 71))
        self.item_four_pic.setText("")
        self.item_four_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Filet O Fish.png"))
        self.item_four_pic.setScaledContents(True)
        self.item_four_pic.setObjectName("item_four_pic")
        self.item_four_text = QtWidgets.QLabel(Mcdonalds)
        self.item_four_text.setGeometry(QtCore.QRect(640, 110, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_four_text.setFont(font)
        self.item_four_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_four_text.setObjectName("item_four_text")
        self.item_one_num = QtWidgets.QSpinBox(Mcdonalds)
        self.item_one_num.setGeometry(QtCore.QRect(70, 150, 42, 22))
        self.item_one_num.setObjectName("item_one_num")
        self.item_one_price = QtWidgets.QLabel(Mcdonalds)
        self.item_one_price.setGeometry(QtCore.QRect(70, 130, 31, 16))
        self.item_one_price.setObjectName("item_one_price")
        self.item_three_num = QtWidgets.QSpinBox(Mcdonalds)
        self.item_three_num.setGeometry(QtCore.QRect(480, 150, 42, 22))
        self.item_three_num.setObjectName("item_three_num")
        self.item_two_text = QtWidgets.QLabel(Mcdonalds)
        self.item_two_text.setGeometry(QtCore.QRect(240, 110, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_two_text.setFont(font)
        self.item_two_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_two_text.setObjectName("item_two_text")
        self.item_three_price = QtWidgets.QLabel(Mcdonalds)
        self.item_three_price.setGeometry(QtCore.QRect(480, 130, 31, 16))
        self.item_three_price.setObjectName("item_three_price")
        self.item_one_pic = QtWidgets.QLabel(Mcdonalds)
        self.item_one_pic.setGeometry(QtCore.QRect(50, 20, 100, 100))
        self.item_one_pic.setText("")
        self.item_one_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Double Mcspicy.png"))
        self.item_one_pic.setScaledContents(True)
        self.item_one_pic.setObjectName("item_one_pic")
        self.item_four_num = QtWidgets.QSpinBox(Mcdonalds)
        self.item_four_num.setGeometry(QtCore.QRect(680, 150, 42, 22))
        self.item_four_num.setObjectName("item_four_num")
        self.item_one_text = QtWidgets.QLabel(Mcdonalds)
        self.item_one_text.setGeometry(QtCore.QRect(40, 110, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_one_text.setFont(font)
        self.item_one_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_one_text.setObjectName("item_one_text")
        self.item_three_text = QtWidgets.QLabel(Mcdonalds)
        self.item_three_text.setGeometry(QtCore.QRect(420, 110, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_three_text.setFont(font)
        self.item_three_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_three_text.setObjectName("item_three_text")
        self.item_two_pic = QtWidgets.QLabel(Mcdonalds)
        self.item_two_pic.setGeometry(QtCore.QRect(259, 29, 91, 81))
        self.item_two_pic.setText("")
        self.item_two_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Big Mac.png"))
        self.item_two_pic.setScaledContents(True)
        self.item_two_pic.setObjectName("item_two_pic")
        self.item_four_price = QtWidgets.QLabel(Mcdonalds)
        self.item_four_price.setGeometry(QtCore.QRect(680, 130, 31, 16))
        self.item_four_price.setObjectName("item_four_price")
        self.item_ten_price = QtWidgets.QLabel(Mcdonalds)
        self.item_ten_price.setGeometry(QtCore.QRect(290, 480, 31, 16))
        self.item_ten_price.setObjectName("item_ten_price")
        self.item_ten_num = QtWidgets.QSpinBox(Mcdonalds)
        self.item_ten_num.setGeometry(QtCore.QRect(280, 500, 42, 22))
        self.item_ten_num.setObjectName("item_ten_num")
        self.item_nine_num = QtWidgets.QSpinBox(Mcdonalds)
        self.item_nine_num.setGeometry(QtCore.QRect(70, 500, 42, 22))
        self.item_nine_num.setObjectName("item_nine_num")
        self.item_nine_price = QtWidgets.QLabel(Mcdonalds)
        self.item_nine_price.setGeometry(QtCore.QRect(70, 480, 31, 16))
        self.item_nine_price.setObjectName("item_nine_price")
        self.item_ten_text = QtWidgets.QLabel(Mcdonalds)
        self.item_ten_text.setGeometry(QtCore.QRect(250, 460, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_ten_text.setFont(font)
        self.item_ten_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_ten_text.setObjectName("item_ten_text")
        self.item_nine_pic = QtWidgets.QLabel(Mcdonalds)
        self.item_nine_pic.setGeometry(QtCore.QRect(50, 370, 100, 100))
        self.item_nine_pic.setText("")
        self.item_nine_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Apple Pie.png"))
        self.item_nine_pic.setScaledContents(True)
        self.item_nine_pic.setObjectName("item_nine_pic")
        self.item_nine_text = QtWidgets.QLabel(Mcdonalds)
        self.item_nine_text.setGeometry(QtCore.QRect(40, 460, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_nine_text.setFont(font)
        self.item_nine_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_nine_text.setObjectName("item_nine_text")
        self.item_ten_pic = QtWidgets.QLabel(Mcdonalds)
        self.item_ten_pic.setGeometry(QtCore.QRect(270, 370, 71, 91))
        self.item_ten_pic.setText("")
        self.item_ten_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Fries.png"))
        self.item_ten_pic.setScaledContents(True)
        self.item_ten_pic.setObjectName("item_ten_pic")
        self.BlueButton = QtWidgets.QPushButton(Mcdonalds)
        self.BlueButton.setGeometry(QtCore.QRect(580, 500, 72, 72))
        self.BlueButton.setStyleSheet("QPushButton {\n"
"    border: none; \n"
"    background-color: #303d5e;\n"
"    /*minimum size*/\n"
"    min-width: 72px;\n"
"    max-width: 72px;\n"
"    min-height: 72px;\n"
"    max-height: 72px;\n"
"    border-radius: 36px; /*Round*/\n"
"    color: #FFFFFF;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"     background-color: #516cb0;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"     background-color: #04070f;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.BlueButton.setObjectName("BlueButton")
        self.BlueButton_2 = QtWidgets.QPushButton(Mcdonalds)
        self.BlueButton_2.setGeometry(QtCore.QRect(700, 500, 72, 72))
        self.BlueButton_2.setStyleSheet("QPushButton {\n"
"    border: none; \n"
"    background-color: #303d5e;\n"
"    /*minimum size*/\n"
"    min-width: 72px;\n"
"    max-width: 72px;\n"
"    min-height: 72px;\n"
"    max-height: 72px;\n"
"    border-radius: 36px; /*Round*/\n"
"    color: #FFFFFF;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"     background-color: #516cb0;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"     background-color: #04070f;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.BlueButton_2.setObjectName("BlueButton_2")
        self.BlueButton.raise_()
        self.item_six_price.raise_()
        self.item_six_num.raise_()
        self.item_seven_pic.raise_()
        self.item_eight_pic.raise_()
        self.item_eight_text.raise_()
        self.item_five_num.raise_()
        self.item_five_price.raise_()
        self.item_seven_num.raise_()
        self.item_six_text.raise_()
        self.item_seven_price.raise_()
        self.item_five_pic.raise_()
        self.item_eight_num.raise_()
        self.item_five_text.raise_()
        self.item_seven_text.raise_()
        self.item_six_pic.raise_()
        self.item_eight_price.raise_()
        self.item_two_price.raise_()
        self.item_two_num.raise_()
        self.item_three_pic.raise_()
        self.item_four_pic.raise_()
        self.item_four_text.raise_()
        self.item_one_num.raise_()
        self.item_one_price.raise_()
        self.item_three_num.raise_()
        self.item_two_text.raise_()
        self.item_three_price.raise_()
        self.item_one_pic.raise_()
        self.item_four_num.raise_()
        self.item_one_text.raise_()
        self.item_three_text.raise_()
        self.item_two_pic.raise_()
        self.item_four_price.raise_()
        self.item_ten_price.raise_()
        self.item_ten_num.raise_()
        self.item_nine_num.raise_()
        self.item_nine_price.raise_()
        self.item_ten_text.raise_()
        self.item_nine_pic.raise_()
        self.item_nine_text.raise_()
        self.item_ten_pic.raise_()
        self.BlueButton_2.raise_()
        
        self.retranslateUi(Mcdonalds)

        

    def btn_click(self):
        print("hello")
    def clear_all(self): 
        self.item_one_num.setValue(0)
        self.item_two_num.setValue(0)
        self.item_three_num.setValue(0)
        self.item_four_num.setValue(0)
        self.item_five_num.setValue(0)
        self.item_six_num.setValue(0)
        self.item_seven_num.setValue(0)
        self.item_eight_num.setValue(0)
        self.item_nine_num.setValue(0)
        self.item_ten_num.setValue(0)
        print("hello")


    def retranslateUi(self, Mcdonalds):
        _translate = QtCore.QCoreApplication.translate
        Mcdonalds.setWindowTitle(_translate("Mcdonalds", "Form"))
        self.item_six_price.setText(_translate("Mcdonalds", "$5.7"))
        self.item_eight_text.setText(_translate("Mcdonalds", "Coke"))
        self.item_five_price.setText(_translate("Mcdonalds", "$4.2"))
        self.item_six_text.setText(_translate("Mcdonalds", "Mc Wrap"))
        self.item_seven_price.setText(_translate("Mcdonalds", "$3.2"))
        self.item_five_text.setText(_translate("Mcdonalds", "Mc Chicken"))
        self.item_seven_text.setText(_translate("Mcdonalds", "Mc Nugguts"))
        self.item_eight_price.setText(_translate("Mcdonalds", "$1.5"))
        self.item_two_price.setText(_translate("Mcdonalds", "$7.2"))
        self.item_four_text.setText(_translate("Mcdonalds", "Fliet O Fish"))
        self.item_one_price.setText(_translate("Mcdonalds", "$5.7"))
        self.item_two_text.setText(_translate("Mcdonalds", "Big Mac"))
        self.item_three_price.setText(_translate("Mcdonalds", "$4.3"))
        self.item_one_text.setText(_translate("Mcdonalds", "Double Mcspicy"))
        self.item_three_text.setText(_translate("Mcdonalds", "Double Cheese Burger"))
        self.item_four_price.setText(_translate("Mcdonalds", "$4.7"))
        self.item_ten_price.setText(_translate("Mcdonalds", "$1.6"))
        self.item_nine_price.setText(_translate("Mcdonalds", "$2.0"))
        self.item_ten_text.setText(_translate("Mcdonalds", "Fries"))
        self.item_nine_text.setText(_translate("Mcdonalds", "Apple Pie"))
        self.BlueButton.setText(_translate("Mcdonalds", "Clear all"))
        self.BlueButton_2.setText(_translate("Mcdonalds", "Add to Cart"))

        self.BlueButton.clicked.connect(self.clear_all)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mcdonalds = QtWidgets.QWidget()
    ui = Ui_Mcdonalds()
    
    ui.setupUi(Mcdonalds)
    Mcdonalds.show()
    sys.exit(app.exec_())