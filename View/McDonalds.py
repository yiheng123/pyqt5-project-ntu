from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget ,QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from datetime import datetime
import pytz

#must indicate the widget items should extend QWidget
class Lunch_Mcdonald(QWidget):
    #initialize
    def __init__(self,parent=None):
        super(Lunch_Mcdonald,self).__init__(parent)

        self.setup_Ui()
        self.string="" # prepare the string to write to file
        self.BlueButton.clicked.connect(self.clear_all) #button connnect to clear all user input and cart database
        self.BlueButton_2.clicked.connect(self.add_to_cart) #add the user input and calculate price
        self.BlueButton_3.clicked.connect(self.operate_hours) #to show operating hourss
        
    #function to clear all the user unput and remove database
    def clear_all(self): 
        #clear all the num value
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
        #clear the string write to data base
        self.string=""        
        try:
            os.remove("C:/Users/RUIZHI/Desktop/mini_project/cart.txt") #remove data base
        except:
            pass


    
    def add_to_cart(self):
        #group all items inside list 
        items_lists=[
            [self.item_one_num,self.item_one_price,self.item_one_text] ,
            [self.item_two_num,self.item_two_price,self.item_two_text] ,
            [self.item_three_num,self.item_three_price,self.item_three_text] ,
            [self.item_four_num,self.item_four_price,self.item_four_text] ,
            [self.item_five_num,self.item_five_price,self.item_five_text] ,
            [self.item_six_num,self.item_six_price,self.item_six_text] ,
            [self.item_seven_num,self.item_seven_price,self.item_seven_text] ,
            [self.item_eight_num,self.item_eight_price,self.item_eight_text] ,
            [self.item_nine_num,self.item_nine_price,self.item_nine_text] ,
            [self.item_ten_num,self.item_ten_price,self.item_ten_text] ,
        ]
        #prepare to write the data to database
        with open("C:/Users/RUIZHI/Desktop/mini_project/cart.txt","w") as f:
            for item_list in items_lists:
                print(item_list[0].value()) #for debugging
                if item_list[0].value() != 0:
                    item_name = str(item_list[2].text()) 
                    item_price_text = str(item_list[1].text())[1:]
                    item_price = float(item_price_text)
                    total_price = item_price*int(item_list[0].value())
                    self.string = self.string + item_name.replace(" ","_") + " " + str(item_list[0].value()) + " " +  str('{0:.2f}'.format(total_price)) + "\n" #format string and add together
            f.write(self.string) #write string to data base
            self.string=""  #clear string

    def operate_hours(self):
        operating_hour_dic = {
            (0,1,2,3,4) : "8am - 12pm", #weekdays
            (5,6) : "11am - 12pm", #weekends
        }
        tz_SG = pytz.timezone('Asia/Singapore') 
        now = datetime.now(tz_SG) 
        now_weekday = now.weekday() #get current time
        for key in operating_hour_dic:
            if now_weekday in key:
                self.operating_hour = operating_hour_dic[key] #get the operating hour from dic

        print(self.operating_hour)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Mcdonalds", "Form"))
        self.operating_hour_text.setText(_translate("Mcdonalds", "Operating Hours: "+self.operating_hour))
    #function to setup ui
    def setup_Ui(self):
        self.setObjectName("Mcdonald")
        self.resize(800,600)
        self.operating_hour_text = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.operating_hour_text.setFont(font)
        self.operating_hour_text.setAlignment(QtCore.Qt.AlignCenter)
        self.operating_hour_text.setGeometry(QtCore.QRect(460, 450, 300, 16))
        self.operating_hour_text.setObjectName("operating_hour_text")
        self.operating_hour_text.raise_()
        self.item_six_price = QtWidgets.QLabel(self)
        self.item_six_price.setGeometry(QtCore.QRect(280, 310, 31, 16))
        self.item_six_price.setObjectName("item_six_price")
        self.item_six_num = QtWidgets.QSpinBox(self)
        self.item_six_num.setGeometry(QtCore.QRect(280, 330, 42, 22))
        self.item_six_num.setObjectName("item_six_num")
        self.item_seven_pic = QtWidgets.QLabel(self)
        self.item_seven_pic.setGeometry(QtCore.QRect(450, 229, 100, 71))
        self.item_seven_pic.setText("")
        self.item_seven_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Mc Nugguts.png"))
        self.item_seven_pic.setScaledContents(True)
        self.item_seven_pic.setObjectName("item_seven_pic")
        self.item_eight_pic = QtWidgets.QLabel(self)
        self.item_eight_pic.setGeometry(QtCore.QRect(660, 219, 91, 81))
        self.item_eight_pic.setText("")
        self.item_eight_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Coke.png"))
        self.item_eight_pic.setScaledContents(True)
        self.item_eight_pic.setObjectName("item_eight_pic")
        self.item_eight_text = QtWidgets.QLabel(self)
        self.item_eight_text.setGeometry(QtCore.QRect(650, 290, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_eight_text.setFont(font)
        self.item_eight_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_eight_text.setObjectName("item_eight_text")
        self.item_five_num = QtWidgets.QSpinBox(self)
        self.item_five_num.setGeometry(QtCore.QRect(70, 330, 42, 22))
        self.item_five_num.setObjectName("item_five_num")
        self.item_five_price = QtWidgets.QLabel(self)
        self.item_five_price.setGeometry(QtCore.QRect(70, 310, 31, 16))
        self.item_five_price.setObjectName("item_five_price")
        self.item_seven_num = QtWidgets.QSpinBox(self)
        self.item_seven_num.setGeometry(QtCore.QRect(480, 330, 42, 22))
        self.item_seven_num.setObjectName("item_seven_num")
        self.item_six_text = QtWidgets.QLabel(self)
        self.item_six_text.setGeometry(QtCore.QRect(250, 290, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_six_text.setFont(font)
        self.item_six_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_six_text.setObjectName("item_six_text")
        self.item_seven_price = QtWidgets.QLabel(self)
        self.item_seven_price.setGeometry(QtCore.QRect(480, 310, 31, 16))
        self.item_seven_price.setObjectName("item_seven_price")
        self.item_five_pic = QtWidgets.QLabel(self)
        self.item_five_pic.setGeometry(QtCore.QRect(50, 220, 91, 71))
        self.item_five_pic.setText("")
        self.item_five_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Mc Chicken.png"))
        self.item_five_pic.setScaledContents(True)
        self.item_five_pic.setObjectName("item_five_pic")
        self.item_eight_num = QtWidgets.QSpinBox(self)
        self.item_eight_num.setGeometry(QtCore.QRect(690, 330, 42, 22))
        self.item_eight_num.setObjectName("item_eight_num")
        self.item_five_text = QtWidgets.QLabel(self)
        self.item_five_text.setGeometry(QtCore.QRect(40, 290, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_five_text.setFont(font)
        self.item_five_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_five_text.setObjectName("item_five_text")
        self.item_seven_text = QtWidgets.QLabel(self)
        self.item_seven_text.setGeometry(QtCore.QRect(440, 290, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_seven_text.setFont(font)
        self.item_seven_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_seven_text.setObjectName("item_seven_text")
        self.item_six_pic = QtWidgets.QLabel(self)
        self.item_six_pic.setGeometry(QtCore.QRect(260, 190, 100, 100))
        self.item_six_pic.setText("")
        self.item_six_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Mc Wrap.png"))
        self.item_six_pic.setScaledContents(True)
        self.item_six_pic.setObjectName("item_six_pic")
        self.item_eight_price = QtWidgets.QLabel(self)
        self.item_eight_price.setGeometry(QtCore.QRect(690, 310, 31, 16))
        self.item_eight_price.setObjectName("item_eight_price")
        self.item_two_price = QtWidgets.QLabel(self)
        self.item_two_price.setGeometry(QtCore.QRect(280, 130, 31, 16))
        self.item_two_price.setObjectName("item_two_price")
        self.item_two_num = QtWidgets.QSpinBox(self)
        self.item_two_num.setGeometry(QtCore.QRect(280, 150, 42, 22))
        self.item_two_num.setObjectName("item_two_num")
        self.item_three_pic = QtWidgets.QLabel(self)
        self.item_three_pic.setGeometry(QtCore.QRect(450, 20, 100, 100))
        self.item_three_pic.setText("")
        self.item_three_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Double Cheese Burger.png"))
        self.item_three_pic.setScaledContents(True)
        self.item_three_pic.setObjectName("item_three_pic")
        self.item_four_pic = QtWidgets.QLabel(self)
        self.item_four_pic.setGeometry(QtCore.QRect(670, 40, 71, 71))
        self.item_four_pic.setText("")
        self.item_four_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Filet O Fish.png"))
        self.item_four_pic.setScaledContents(True)
        self.item_four_pic.setObjectName("item_four_pic")
        self.item_four_text = QtWidgets.QLabel(self)
        self.item_four_text.setGeometry(QtCore.QRect(640, 110, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_four_text.setFont(font)
        self.item_four_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_four_text.setObjectName("item_four_text")
        self.item_one_num = QtWidgets.QSpinBox(self)
        self.item_one_num.setGeometry(QtCore.QRect(70, 150, 42, 22))
        self.item_one_num.setObjectName("item_one_num")
        self.item_one_price = QtWidgets.QLabel(self)
        self.item_one_price.setGeometry(QtCore.QRect(70, 130, 31, 16))
        self.item_one_price.setObjectName("item_one_price")
        self.item_three_num = QtWidgets.QSpinBox(self)
        self.item_three_num.setGeometry(QtCore.QRect(480, 150, 42, 22))
        self.item_three_num.setObjectName("item_three_num")
        self.item_two_text = QtWidgets.QLabel(self)
        self.item_two_text.setGeometry(QtCore.QRect(240, 110, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_two_text.setFont(font)
        self.item_two_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_two_text.setObjectName("item_two_text")
        self.item_three_price = QtWidgets.QLabel(self)
        self.item_three_price.setGeometry(QtCore.QRect(480, 130, 31, 16))
        self.item_three_price.setObjectName("item_three_price")
        self.item_one_pic = QtWidgets.QLabel(self)
        self.item_one_pic.setGeometry(QtCore.QRect(50, 20, 100, 100))
        self.item_one_pic.setText("")
        self.item_one_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Double Mcspicy.png"))
        self.item_one_pic.setScaledContents(True)
        self.item_one_pic.setObjectName("item_one_pic")
        self.item_four_num = QtWidgets.QSpinBox(self)
        self.item_four_num.setGeometry(QtCore.QRect(680, 150, 42, 22))
        self.item_four_num.setObjectName("item_four_num")
        self.item_one_text = QtWidgets.QLabel(self)
        self.item_one_text.setGeometry(QtCore.QRect(40, 110, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_one_text.setFont(font)
        self.item_one_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_one_text.setObjectName("item_one_text")
        self.item_three_text = QtWidgets.QLabel(self)
        self.item_three_text.setGeometry(QtCore.QRect(420, 110, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_three_text.setFont(font)
        self.item_three_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_three_text.setObjectName("item_three_text")
        self.item_two_pic = QtWidgets.QLabel(self)
        self.item_two_pic.setGeometry(QtCore.QRect(259, 29, 91, 81))
        self.item_two_pic.setText("")
        self.item_two_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Big Mac.png"))
        self.item_two_pic.setScaledContents(True)
        self.item_two_pic.setObjectName("item_two_pic")
        self.item_four_price = QtWidgets.QLabel(self)
        self.item_four_price.setGeometry(QtCore.QRect(680, 130, 31, 16))
        self.item_four_price.setObjectName("item_four_price")
        self.item_ten_price = QtWidgets.QLabel(self)
        self.item_ten_price.setGeometry(QtCore.QRect(290, 480, 31, 16))
        self.item_ten_price.setObjectName("item_ten_price")
        self.item_ten_num = QtWidgets.QSpinBox(self)
        self.item_ten_num.setGeometry(QtCore.QRect(280, 500, 42, 22))
        self.item_ten_num.setObjectName("item_ten_num")
        self.item_nine_num = QtWidgets.QSpinBox(self)
        self.item_nine_num.setGeometry(QtCore.QRect(70, 500, 42, 22))
        self.item_nine_num.setObjectName("item_nine_num")
        self.item_nine_price = QtWidgets.QLabel(self)
        self.item_nine_price.setGeometry(QtCore.QRect(70, 480, 31, 16))
        self.item_nine_price.setObjectName("item_nine_price")
        self.item_ten_text = QtWidgets.QLabel(self)
        self.item_ten_text.setGeometry(QtCore.QRect(250, 460, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_ten_text.setFont(font)
        self.item_ten_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_ten_text.setObjectName("item_ten_text")
        self.item_nine_pic = QtWidgets.QLabel(self)
        self.item_nine_pic.setGeometry(QtCore.QRect(50, 370, 100, 100))
        self.item_nine_pic.setText("")
        self.item_nine_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Apple Pie.png"))
        self.item_nine_pic.setScaledContents(True)
        self.item_nine_pic.setObjectName("item_nine_pic")
        self.item_nine_text = QtWidgets.QLabel(self)
        self.item_nine_text.setGeometry(QtCore.QRect(40, 460, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_nine_text.setFont(font)
        self.item_nine_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_nine_text.setObjectName("item_nine_text")
        self.item_ten_pic = QtWidgets.QLabel(self)
        self.item_ten_pic.setGeometry(QtCore.QRect(270, 370, 71, 91))
        self.item_ten_pic.setText("")
        self.item_ten_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Fries.png"))
        self.item_ten_pic.setScaledContents(True)
        self.item_ten_pic.setObjectName("item_ten_pic")
        self.BlueButton = QtWidgets.QPushButton(self)
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
        self.BlueButton_2 = QtWidgets.QPushButton(self)
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
        self.BlueButton_3 = QtWidgets.QPushButton(self)
        self.BlueButton_3.setGeometry(QtCore.QRect(460, 500, 72, 72))
        self.BlueButton_3.setStyleSheet("QPushButton {\n"
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
        self.BlueButton_3.setObjectName("BlueButton_3")
        self.BlueButton_3.raise_()
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
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Mcdonalds", "Form"))
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
        self.BlueButton_3.setText(_translate("Mcdonalds", "Operate Hours"))


class Breakfast_Mcdonald(QWidget):
    #initialize
    def __init__(self,parent=None):
        super(Breakfast_Mcdonald,self).__init__(parent)

        self.setup_Ui()
        self.string="" # string to write to file
        self.BlueButton.clicked.connect(self.clear_all) #button connnect to clear all user input and cart database
        self.BlueButton_2.clicked.connect(self.add_to_cart) #add the user input and calculate price
        self.BlueButton_3.clicked.connect(self.operate_hours)
        
    #function to clear all the user unput and remove database
    def clear_all(self): 
        #clear all the num value
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
        #clear the string write to data base
        self.string=""        
        try:
            os.remove("C:/Users/RUIZHI/Desktop/mini_project/cart.txt") #remove data base
        except:
            pass


    
    def add_to_cart(self):
        #group all items inside dictionary
        items_lists=[
            [self.item_one_num,self.item_one_price,self.item_one_text] ,
            [self.item_two_num,self.item_two_price,self.item_two_text] ,
            [self.item_three_num,self.item_three_price,self.item_three_text] ,
            [self.item_four_num,self.item_four_price,self.item_four_text] ,
            [self.item_five_num,self.item_five_price,self.item_five_text] ,
            [self.item_six_num,self.item_six_price,self.item_six_text] ,
            [self.item_seven_num,self.item_seven_price,self.item_seven_text] ,
            [self.item_eight_num,self.item_eight_price,self.item_eight_text] ,
            [self.item_nine_num,self.item_nine_price,self.item_nine_text] ,
            [self.item_ten_num,self.item_ten_price,self.item_ten_text] ,
        ]
        #prepare to write the data to database
        with open("C:/Users/RUIZHI/Desktop/mini_project/cart.txt","w") as f:
            for item_list in items_lists:
                print(item_list[0].value()) #for debugging
                if item_list[0].value() != 0:
                    item_name = str(item_list[2].text()) 
                    item_price_text = str(item_list[1].text())[1:]
                    item_price = float(item_price_text)
                    total_price = item_price*int(item_list[0].value())
                    self.string = self.string + item_name.replace(" ","_") + " " + str(item_list[0].value()) + " " +  str('{0:.2f}'.format(total_price)) + "\n" #format string and add together
            f.write(self.string) #write string to data base
            self.string=""  #clear string

    def operate_hours(self):
        operating_hour_dic = {
            (0,1,2,3,4) : "8am - 12pm", #weekdays
            (5,6) : "11am - 12pm", #weekends
        }
        
        tz_SG = pytz.timezone('Asia/Singapore') 
        now = datetime.now(tz_SG)
        now_weekday = now.weekday()
        for key in operating_hour_dic:
            if now_weekday in key:
                self.operating_hour = operating_hour_dic[key]
        print(self.operating_hour)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Mcdonalds", "Form"))
        self.operating_hour_text.setText(_translate("Mcdonalds", "Operating Hours: "+self.operating_hour))
    #function to setup ui
    def setup_Ui(self):
        self.setObjectName("Mcdonald")
        self.resize(800,600)
        self.operating_hour_text = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.operating_hour_text.setFont(font)
        self.operating_hour_text.setAlignment(QtCore.Qt.AlignCenter)
        self.operating_hour_text.setGeometry(QtCore.QRect(460, 450, 300, 16))
        self.operating_hour_text.setObjectName("operating_hour_text")
        self.operating_hour_text.raise_()
        self.item_six_price = QtWidgets.QLabel(self)
        self.item_six_price.setGeometry(QtCore.QRect(280, 310, 31, 16))
        self.item_six_price.setObjectName("item_six_price")
        self.item_six_num = QtWidgets.QSpinBox(self)
        self.item_six_num.setGeometry(QtCore.QRect(280, 330, 42, 22))
        self.item_six_num.setObjectName("item_six_num")
        self.item_seven_pic = QtWidgets.QLabel(self)
        self.item_seven_pic.setGeometry(QtCore.QRect(450, 229, 100, 71))
        self.item_seven_pic.setText("")
        self.item_seven_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Apple Pie.png"))
        self.item_seven_pic.setScaledContents(True)
        self.item_seven_pic.setObjectName("item_seven_pic")
        self.item_eight_pic = QtWidgets.QLabel(self)
        self.item_eight_pic.setGeometry(QtCore.QRect(660, 219, 91, 81))
        self.item_eight_pic.setText("")
        self.item_eight_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Mc Coffee.png"))
        self.item_eight_pic.setScaledContents(True)
        self.item_eight_pic.setObjectName("item_eight_pic")
        self.item_eight_text = QtWidgets.QLabel(self)
        self.item_eight_text.setGeometry(QtCore.QRect(650, 290, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_eight_text.setFont(font)
        self.item_eight_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_eight_text.setObjectName("item_eight_text")
        self.item_five_num = QtWidgets.QSpinBox(self)
        self.item_five_num.setGeometry(QtCore.QRect(70, 330, 42, 22))
        self.item_five_num.setObjectName("item_five_num")
        self.item_five_price = QtWidgets.QLabel(self)
        self.item_five_price.setGeometry(QtCore.QRect(70, 310, 31, 16))
        self.item_five_price.setObjectName("item_five_price")
        self.item_seven_num = QtWidgets.QSpinBox(self)
        self.item_seven_num.setGeometry(QtCore.QRect(480, 330, 42, 22))
        self.item_seven_num.setObjectName("item_seven_num")
        self.item_six_text = QtWidgets.QLabel(self)
        self.item_six_text.setGeometry(QtCore.QRect(250, 290, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_six_text.setFont(font)
        self.item_six_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_six_text.setObjectName("item_six_text")
        self.item_seven_price = QtWidgets.QLabel(self)
        self.item_seven_price.setGeometry(QtCore.QRect(480, 310, 31, 16))
        self.item_seven_price.setObjectName("item_seven_price")
        self.item_five_pic = QtWidgets.QLabel(self)
        self.item_five_pic.setGeometry(QtCore.QRect(50, 220, 91, 71))
        self.item_five_pic.setText("")
        self.item_five_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Filet O Fish.png"))
        self.item_five_pic.setScaledContents(True)
        self.item_five_pic.setObjectName("item_five_pic")
        self.item_eight_num = QtWidgets.QSpinBox(self)
        self.item_eight_num.setGeometry(QtCore.QRect(690, 330, 42, 22))
        self.item_eight_num.setObjectName("item_eight_num")
        self.item_five_text = QtWidgets.QLabel(self)
        self.item_five_text.setGeometry(QtCore.QRect(40, 290, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_five_text.setFont(font)
        self.item_five_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_five_text.setObjectName("item_five_text")
        self.item_seven_text = QtWidgets.QLabel(self)
        self.item_seven_text.setGeometry(QtCore.QRect(440, 290, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_seven_text.setFont(font)
        self.item_seven_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_seven_text.setObjectName("item_seven_text")
        self.item_six_pic = QtWidgets.QLabel(self)
        self.item_six_pic.setGeometry(QtCore.QRect(260, 190, 100, 100))
        self.item_six_pic.setText("")
        self.item_six_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Mcwings.png"))
        self.item_six_pic.setScaledContents(True)
        self.item_six_pic.setObjectName("item_six_pic")
        self.item_eight_price = QtWidgets.QLabel(self)
        self.item_eight_price.setGeometry(QtCore.QRect(690, 310, 31, 16))
        self.item_eight_price.setObjectName("item_eight_price")
        self.item_two_price = QtWidgets.QLabel(self)
        self.item_two_price.setGeometry(QtCore.QRect(280, 130, 31, 16))
        self.item_two_price.setObjectName("item_two_price")
        self.item_two_num = QtWidgets.QSpinBox(self)
        self.item_two_num.setGeometry(QtCore.QRect(280, 150, 42, 22))
        self.item_two_num.setObjectName("item_two_num")
        self.item_three_pic = QtWidgets.QLabel(self)
        self.item_three_pic.setGeometry(QtCore.QRect(450, 20, 100, 100))
        self.item_three_pic.setText("")
        self.item_three_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Hashbrown.png"))
        self.item_three_pic.setScaledContents(True)
        self.item_three_pic.setObjectName("item_three_pic")
        self.item_four_pic = QtWidgets.QLabel(self)
        self.item_four_pic.setGeometry(QtCore.QRect(670, 40, 71, 71))
        self.item_four_pic.setText("")
        self.item_four_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Corn Cup.png"))
        self.item_four_pic.setScaledContents(True)
        self.item_four_pic.setObjectName("item_four_pic")
        self.item_four_text = QtWidgets.QLabel(self)
        self.item_four_text.setGeometry(QtCore.QRect(640, 110, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_four_text.setFont(font)
        self.item_four_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_four_text.setObjectName("item_four_text")
        self.item_one_num = QtWidgets.QSpinBox(self)
        self.item_one_num.setGeometry(QtCore.QRect(70, 150, 42, 22))
        self.item_one_num.setObjectName("item_one_num")
        self.item_one_price = QtWidgets.QLabel(self)
        self.item_one_price.setGeometry(QtCore.QRect(70, 130, 31, 16))
        self.item_one_price.setObjectName("item_one_price")
        self.item_three_num = QtWidgets.QSpinBox(self)
        self.item_three_num.setGeometry(QtCore.QRect(480, 150, 42, 22))
        self.item_three_num.setObjectName("item_three_num")
        self.item_two_text = QtWidgets.QLabel(self)
        self.item_two_text.setGeometry(QtCore.QRect(240, 110, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_two_text.setFont(font)
        self.item_two_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_two_text.setObjectName("item_two_text")
        self.item_three_price = QtWidgets.QLabel(self)
        self.item_three_price.setGeometry(QtCore.QRect(480, 130, 31, 16))
        self.item_three_price.setObjectName("item_three_price")
        self.item_one_pic = QtWidgets.QLabel(self)
        self.item_one_pic.setGeometry(QtCore.QRect(50, 20, 100, 100))
        self.item_one_pic.setText("")
        self.item_one_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Chicken Muffin.png"))
        self.item_one_pic.setScaledContents(True)
        self.item_one_pic.setObjectName("item_one_pic")
        self.item_four_num = QtWidgets.QSpinBox(self)
        self.item_four_num.setGeometry(QtCore.QRect(680, 150, 42, 22))
        self.item_four_num.setObjectName("item_four_num")
        self.item_one_text = QtWidgets.QLabel(self)
        self.item_one_text.setGeometry(QtCore.QRect(40, 110, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_one_text.setFont(font)
        self.item_one_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_one_text.setObjectName("item_one_text")
        self.item_three_text = QtWidgets.QLabel(self)
        self.item_three_text.setGeometry(QtCore.QRect(420, 110, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_three_text.setFont(font)
        self.item_three_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_three_text.setObjectName("item_three_text")
        self.item_two_pic = QtWidgets.QLabel(self)
        self.item_two_pic.setGeometry(QtCore.QRect(259, 29, 91, 81))
        self.item_two_pic.setText("")
        self.item_two_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Mc Sausage Muffin.png"))
        self.item_two_pic.setScaledContents(True)
        self.item_two_pic.setObjectName("item_two_pic")
        self.item_four_price = QtWidgets.QLabel(self)
        self.item_four_price.setGeometry(QtCore.QRect(680, 130, 31, 16))
        self.item_four_price.setObjectName("item_four_price")
        self.item_ten_price = QtWidgets.QLabel(self)
        self.item_ten_price.setGeometry(QtCore.QRect(290, 480, 31, 16))
        self.item_ten_price.setObjectName("item_ten_price")
        self.item_ten_num = QtWidgets.QSpinBox(self)
        self.item_ten_num.setGeometry(QtCore.QRect(280, 500, 42, 22))
        self.item_ten_num.setObjectName("item_ten_num")
        self.item_nine_num = QtWidgets.QSpinBox(self)
        self.item_nine_num.setGeometry(QtCore.QRect(70, 500, 42, 22))
        self.item_nine_num.setObjectName("item_nine_num")
        self.item_nine_price = QtWidgets.QLabel(self)
        self.item_nine_price.setGeometry(QtCore.QRect(70, 480, 31, 16))
        self.item_nine_price.setObjectName("item_nine_price")
        self.item_ten_text = QtWidgets.QLabel(self)
        self.item_ten_text.setGeometry(QtCore.QRect(250, 460, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_ten_text.setFont(font)
        self.item_ten_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_ten_text.setObjectName("item_ten_text")
        self.item_nine_pic = QtWidgets.QLabel(self)
        self.item_nine_pic.setGeometry(QtCore.QRect(50, 370, 100, 100))
        self.item_nine_pic.setText("")
        self.item_nine_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Breakfast Platter.png"))
        self.item_nine_pic.setScaledContents(True)
        self.item_nine_pic.setObjectName("item_nine_pic")
        self.item_nine_text = QtWidgets.QLabel(self)
        self.item_nine_text.setGeometry(QtCore.QRect(40, 460, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.item_nine_text.setFont(font)
        self.item_nine_text.setAlignment(QtCore.Qt.AlignCenter)
        self.item_nine_text.setObjectName("item_nine_text")
        self.item_ten_pic = QtWidgets.QLabel(self)
        self.item_ten_pic.setGeometry(QtCore.QRect(270, 370, 71, 91))
        self.item_ten_pic.setText("")
        self.item_ten_pic.setPixmap(QtGui.QPixmap("C:/Users/RUIZHI/Desktop/mini_project/View/Pictures/McDonalds/Fries.png"))
        self.item_ten_pic.setScaledContents(True)
        self.item_ten_pic.setObjectName("item_ten_pic")
        self.BlueButton = QtWidgets.QPushButton(self)
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
        self.BlueButton_2 = QtWidgets.QPushButton(self)
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
        self.BlueButton_3 = QtWidgets.QPushButton(self)
        self.BlueButton_3.setGeometry(QtCore.QRect(460, 500, 72, 72))
        self.BlueButton_3.setStyleSheet("QPushButton {\n"
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
        self.BlueButton_3.setObjectName("BlueButton_3")
        self.BlueButton_3.raise_()
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
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Mcdonalds", "Form"))
        self.item_six_price.setText(_translate("Mcdonalds", "$3.5"))
        self.item_eight_text.setText(_translate("Mcdonalds", "Mc Coffee"))
        self.item_five_price.setText(_translate("Mcdonalds", "$5.2"))
        self.item_six_text.setText(_translate("Mcdonalds", "Mc Wings"))
        self.item_seven_price.setText(_translate("Mcdonalds", "$1.8"))
        self.item_five_text.setText(_translate("Mcdonalds", "Flit O Fish"))
        self.item_seven_text.setText(_translate("Mcdonalds", "Apple Pie"))
        self.item_eight_price.setText(_translate("Mcdonalds", "$1.5"))
        self.item_two_price.setText(_translate("Mcdonalds", "$3.2"))
        self.item_four_text.setText(_translate("Mcdonalds", "Corn Cup"))
        self.item_one_price.setText(_translate("Mcdonalds", "$3.5"))
        self.item_two_text.setText(_translate("Mcdonalds", "Sasuage Muffiin"))
        self.item_three_price.setText(_translate("Mcdonalds", "$1.8"))
        self.item_one_text.setText(_translate("Mcdonalds", "Chicken Muffin"))
        self.item_three_text.setText(_translate("Mcdonalds", "Hashbrown"))
        self.item_four_price.setText(_translate("Mcdonalds", "$4.7"))
        self.item_ten_price.setText(_translate("Mcdonalds", "$1.6"))
        self.item_nine_price.setText(_translate("Mcdonalds", "$8.2"))
        self.item_ten_text.setText(_translate("Mcdonalds", "Fries"))
        self.item_nine_text.setText(_translate("Mcdonalds", "Breakfast Platter"))
        self.BlueButton.setText(_translate("Mcdonalds", "Clear all"))
        self.BlueButton_2.setText(_translate("Mcdonalds", "Add to Cart"))
        self.BlueButton_3.setText(_translate("Mcdonalds", "Operate Hours"))

if __name__ == '__main__':
    import sys
    
    app =QtWidgets.QApplication(sys.argv)
    window = Lunch_Mcdonald()
    window.show()
    sys.exit(app.exec_())