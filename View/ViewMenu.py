from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget ,QMessageBox,QApplication,QStackedWidget ,QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, QTimer,QDate, QTime
import os
from datetime import datetime
import pytz

#Generate Class for Qlabel clickable events
class QLabelClickable(QtWidgets.QLabel):
    clicked = pyqtSignal(str)
    def __init__(self, parent=None):
        super(QLabelClickable, self).__init__(parent)
    def mousePressEvent(self, event):
        self.ultimo = "Clic"
    
    def mouseReleaseEvent(self, event):
        if self.ultimo == "Clic":
            QTimer.singleShot(QApplication.instance().doubleClickInterval(),
                              self.performSingleClickAction)
        else:
            # Realizar acción de doble clic.
            self.clicked.emit(self.ultimo)
    def mouseDoubleClickEvent(self, event):
        self.ultimo = "Doble Clic"
    def performSingleClickAction(self):
        if self.ultimo == "Clic":
            self.clicked.emit(self.ultimo)

class View_Menu_First_Page(QWidget):
    #initialize UI
    def __init__(self,parent=None):
        super(View_Menu_First_Page,self).__init__(parent)
        self.setup_Ui()
    def setup_Ui(self):
        self.setObjectName("ViewMenu_Select_Store")
        self.resize(800, 600)
        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(180, 40, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setLineWidth(1)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_mcdonalds = QLabelClickable(self)
        self.label_mcdonalds.setGeometry(QtCore.QRect(120, 140, 200, 200))
        self.label_mcdonalds.setText("")
        self.label_mcdonalds.setPixmap(QtGui.QPixmap("./Pictures/McDonald.png"))
        self.label_mcdonalds.setScaledContents(True)
        self.label_mcdonalds.setObjectName("label_mcdonalds")
        self.label_kfc = QLabelClickable(self)
        self.label_kfc.setGeometry(QtCore.QRect(470, 360, 200, 200))
        self.label_kfc.setText("")
        self.label_kfc.setPixmap(QtGui.QPixmap("./Pictures/590607570cbeef0acff9a641.png"))
        self.label_kfc.setScaledContents(True)
        self.label_kfc.setObjectName("label_kfc")
        self.label_subway = QLabelClickable(self)
        self.label_subway.setGeometry(QtCore.QRect(470, 140, 200, 200))
        self.label_subway.setText("")
        self.label_subway.setPixmap(QtGui.QPixmap("./Pictures/subway-logo.jpg"))
        self.label_subway.setScaledContents(True)
        self.label_subway.setObjectName("label_subway")
        self.label_malay = QLabelClickable(self)
        self.label_malay.setGeometry(QtCore.QRect(120, 360, 200, 200))
        self.label_malay.setText("")
        self.label_malay.setPixmap(QtGui.QPixmap("./Pictures/39840570-nasi-goreng-icon-indonesian-fried-rice.jpg"))
        self.label_malay.setScaledContents(True)
        self.label_malay.setObjectName("label_malay")
        QtCore.QMetaObject.connectSlotsByName(self)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ViewMenu_Select_Store", "Form"))
        self.label_title.setText(_translate("ViewMenu_Select_Store", "Select Store Menu"))
    def MC_link_click(self):
        print("haha")
        return "Mcdonalds" #return message for multipage interation
    def Subway_link_click(self):
        return "Subway"
    def Malay_link_click(self):
        return "Malay"
    def KFC_link_click(self):
        return "KFC"
    


#Response from first page click information to generate second page
class View_Menu_Second_Page(QWidget):
    def __init__(self,text,parent=None):
        super(View_Menu_Second_Page,self).__init__(parent)
        self.setup_Ui(text)
    def setup_Ui(self,text):
        self.setObjectName("View_Menu_Second_Page")
        self.resize(800, 600)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(230, 20, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.BlueButton = QtWidgets.QPushButton(self)
        self.BlueButton.setGeometry(QtCore.QRect(630, 180, 96, 96))
        self.BlueButton.setStyleSheet("#BlueButton {\n"
"    background-color: #303d5e;\n"
"    /*minimum size*/\n"
"    min-width: 96px;\n"
"    max-width: 96px;\n"
"    min-height: 96px;\n"
"    max-height: 96px;\n"
"    border-radius: 48px; /*Round*/\n"
"    color: #FFFFFF;\n"
"}\n"
"#BlueButton:hover {\n"
"    background-color: #516cb0;\n"
"}\n"
"#BlueButton:pressed {\n"
"    background-color: #04070f;\n"
"}")
        self.BlueButton.setObjectName("BlueButton")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(100, 300, 571, 291))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./Pictures/"+text+".png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(self)
        self.dateEdit.setGeometry(QtCore.QRect(120, 200, 241, 81))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self)
        self.timeEdit.setTime(QTime.currentTime())
        self.timeEdit.setGeometry(QtCore.QRect(360, 200, 241, 81))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", text))
        self.BlueButton.setText(_translate("Form", "Submit"))
        self.label_2.setText(_translate("Form", "Please Select The Date and Time You Would Like To View"))
    #To return the date and time from the selection on qtdateEdit and timeEdit
    def submit_click(self):
        print(self.dateEdit.date())
        date = self.dateEdit.date().toPyDate()
        time = self.timeEdit.time().toPyTime()
        datetime_str = str(date)+" "+str(time)[0:8]
        print(datetime_str)
        return datetime_str

#Response for the first page and second page information to get the menu to show
class View_Menu_Third_Page(QWidget):

    def __init__(self,store,dateandtime,parent=None):
        super(View_Menu_Third_Page,self).__init__(parent)
        if store == "Mcdonalds":
            if int(dateandtime[11:13]) >= 12:
                self.setup_Ui_Pm_Mcdonalds()
            else:
                self.setup_Ui_Am_Mcdonalds()
        if store == "Subway":
            pass
        if store == "Malay":
            pass
        if store == "KFC":
            pass
    #menu from the McDonalds.py where we remove all the counters and buttons
    def setup_Ui_Pm_Mcdonalds(self):
        self.setObjectName("Pm Mcdonald")
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
        self.item_seven_pic = QtWidgets.QLabel(self)
        self.item_seven_pic.setGeometry(QtCore.QRect(450, 229, 100, 71))
        self.item_seven_pic.setText("")
        self.item_seven_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Mc Nugguts.png"))
        self.item_seven_pic.setScaledContents(True)
        self.item_seven_pic.setObjectName("item_seven_pic")
        self.item_eight_pic = QtWidgets.QLabel(self)
        self.item_eight_pic.setGeometry(QtCore.QRect(660, 219, 91, 81))
        self.item_eight_pic.setText("")
        self.item_eight_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Coke.png"))
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
        self.item_five_price = QtWidgets.QLabel(self)
        self.item_five_price.setGeometry(QtCore.QRect(70, 310, 31, 16))
        self.item_five_price.setObjectName("item_five_price")
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
        self.item_five_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Mc Chicken.png"))
        self.item_five_pic.setScaledContents(True)
        self.item_five_pic.setObjectName("item_five_pic")
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
        self.item_six_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Mc Wrap.png"))
        self.item_six_pic.setScaledContents(True)
        self.item_six_pic.setObjectName("item_six_pic")
        self.item_eight_price = QtWidgets.QLabel(self)
        self.item_eight_price.setGeometry(QtCore.QRect(690, 310, 31, 16))
        self.item_eight_price.setObjectName("item_eight_price")
        self.item_two_price = QtWidgets.QLabel(self)
        self.item_two_price.setGeometry(QtCore.QRect(280, 130, 31, 16))
        self.item_two_price.setObjectName("item_two_price")
        self.item_three_pic = QtWidgets.QLabel(self)
        self.item_three_pic.setGeometry(QtCore.QRect(450, 20, 100, 100))
        self.item_three_pic.setText("")
        self.item_three_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Double Cheese Burger.png"))
        self.item_three_pic.setScaledContents(True)
        self.item_three_pic.setObjectName("item_three_pic")
        self.item_four_pic = QtWidgets.QLabel(self)
        self.item_four_pic.setGeometry(QtCore.QRect(670, 40, 71, 71))
        self.item_four_pic.setText("")
        self.item_four_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Filet O Fish.png"))
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
        self.item_one_price = QtWidgets.QLabel(self)
        self.item_one_price.setGeometry(QtCore.QRect(70, 130, 31, 16))
        self.item_one_price.setObjectName("item_one_price")
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
        self.item_one_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Double Mcspicy.png"))
        self.item_one_pic.setScaledContents(True)
        self.item_one_pic.setObjectName("item_one_pic")
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
        self.item_two_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Big Mac.png"))
        self.item_two_pic.setScaledContents(True)
        self.item_two_pic.setObjectName("item_two_pic")
        self.item_four_price = QtWidgets.QLabel(self)
        self.item_four_price.setGeometry(QtCore.QRect(680, 130, 31, 16))
        self.item_four_price.setObjectName("item_four_price")
        self.item_ten_price = QtWidgets.QLabel(self)
        self.item_ten_price.setGeometry(QtCore.QRect(290, 480, 31, 16))
        self.item_ten_price.setObjectName("item_ten_price")
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
        self.item_nine_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Apple Pie.png"))
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
        self.item_ten_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Fries.png"))
        self.item_ten_pic.setScaledContents(True)
        self.item_ten_pic.setObjectName("item_ten_pic")
        self.item_six_price.raise_()
        self.item_seven_pic.raise_()
        self.item_eight_pic.raise_()
        self.item_eight_text.raise_()
        self.item_five_price.raise_()
        self.item_six_text.raise_()
        self.item_seven_price.raise_()
        self.item_five_pic.raise_()
        self.item_five_text.raise_()
        self.item_seven_text.raise_()
        self.item_six_pic.raise_()
        self.item_eight_price.raise_()
        self.item_two_price.raise_()
        self.item_three_pic.raise_()
        self.item_four_pic.raise_()
        self.item_four_text.raise_()
        self.item_one_price.raise_()
        self.item_two_text.raise_()
        self.item_three_price.raise_()
        self.item_one_pic.raise_()
        self.item_one_text.raise_()
        self.item_three_text.raise_()
        self.item_two_pic.raise_()
        self.item_four_price.raise_()
        self.item_ten_price.raise_()
        self.item_nine_price.raise_()
        self.item_ten_text.raise_()
        self.item_nine_pic.raise_()
        self.item_nine_text.raise_()
        self.item_ten_pic.raise_()
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
        self.BlueButton_2.raise_()
        self.BlueButton_2.setText(_translate("Mcdonalds", "back"))


    def setup_Ui_Am_Mcdonalds(self):
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
        self.item_seven_pic = QtWidgets.QLabel(self)
        self.item_seven_pic.setGeometry(QtCore.QRect(450, 229, 100, 71))
        self.item_seven_pic.setText("")
        self.item_seven_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Apple Pie.png"))
        self.item_seven_pic.setScaledContents(True)
        self.item_seven_pic.setObjectName("item_seven_pic")
        self.item_eight_pic = QtWidgets.QLabel(self)
        self.item_eight_pic.setGeometry(QtCore.QRect(660, 219, 91, 81))
        self.item_eight_pic.setText("")
        self.item_eight_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Mc Coffee.png"))
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
        self.item_five_price = QtWidgets.QLabel(self)
        self.item_five_price.setGeometry(QtCore.QRect(70, 310, 31, 16))
        self.item_five_price.setObjectName("item_five_price")
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
        self.item_five_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Filet O Fish.png"))
        self.item_five_pic.setScaledContents(True)
        self.item_five_pic.setObjectName("item_five_pic")
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
        self.item_six_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Mcwings.png"))
        self.item_six_pic.setScaledContents(True)
        self.item_six_pic.setObjectName("item_six_pic")
        self.item_eight_price = QtWidgets.QLabel(self)
        self.item_eight_price.setGeometry(QtCore.QRect(690, 310, 31, 16))
        self.item_eight_price.setObjectName("item_eight_price")
        self.item_two_price = QtWidgets.QLabel(self)
        self.item_two_price.setGeometry(QtCore.QRect(280, 130, 31, 16))
        self.item_two_price.setObjectName("item_two_price")
        self.item_three_pic = QtWidgets.QLabel(self)
        self.item_three_pic.setGeometry(QtCore.QRect(450, 20, 100, 100))
        self.item_three_pic.setText("")
        self.item_three_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Hashbrown.png"))
        self.item_three_pic.setScaledContents(True)
        self.item_three_pic.setObjectName("item_three_pic")
        self.item_four_pic = QtWidgets.QLabel(self)
        self.item_four_pic.setGeometry(QtCore.QRect(670, 40, 71, 71))
        self.item_four_pic.setText("")
        self.item_four_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Corn Cup.png"))
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
        self.item_one_price = QtWidgets.QLabel(self)
        self.item_one_price.setGeometry(QtCore.QRect(70, 130, 31, 16))
        self.item_one_price.setObjectName("item_one_price")
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
        self.item_one_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Chicken Muffin.png"))
        self.item_one_pic.setScaledContents(True)
        self.item_one_pic.setObjectName("item_one_pic")
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
        self.item_two_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Mc Sausage Muffin.png"))
        self.item_two_pic.setScaledContents(True)
        self.item_two_pic.setObjectName("item_two_pic")
        self.item_four_price = QtWidgets.QLabel(self)
        self.item_four_price.setGeometry(QtCore.QRect(680, 130, 31, 16))
        self.item_four_price.setObjectName("item_four_price")
        self.item_ten_price = QtWidgets.QLabel(self)
        self.item_ten_price.setGeometry(QtCore.QRect(290, 480, 31, 16))
        self.item_ten_price.setObjectName("item_ten_price")
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
        self.item_nine_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Breakfast Platter.png"))
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
        self.item_ten_pic.setPixmap(QtGui.QPixmap("./Pictures/McDonalds/Fries.png"))
        self.item_ten_pic.setScaledContents(True)
        self.item_ten_pic.setObjectName("item_ten_pic")
        self.item_six_price.raise_()
        self.item_seven_pic.raise_()
        self.item_eight_pic.raise_()
        self.item_eight_text.raise_()
        self.item_five_price.raise_()
        self.item_six_text.raise_()
        self.item_seven_price.raise_()
        self.item_five_pic.raise_()
        self.item_five_text.raise_()
        self.item_seven_text.raise_()
        self.item_six_pic.raise_()
        self.item_eight_price.raise_()
        self.item_two_price.raise_()
        self.item_three_pic.raise_()
        self.item_four_pic.raise_()
        self.item_four_text.raise_()
        self.item_one_price.raise_()
        self.item_two_text.raise_()
        self.item_three_price.raise_()
        self.item_one_pic.raise_()
        self.item_one_text.raise_()
        self.item_three_text.raise_()
        self.item_two_pic.raise_()
        self.item_four_price.raise_()
        self.item_ten_price.raise_()
        self.item_nine_price.raise_()
        self.item_ten_text.raise_()
        self.item_nine_pic.raise_()
        self.item_nine_text.raise_()
        self.item_ten_pic.raise_()
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
        self.BlueButton_2.raise_()
        self.BlueButton_2.setText(_translate("Mcdonalds", "back"))

        
    
#Controller Class to control all the page interations
class View_Menu(QWidget):

    #Initialiaze the first page for class View_Menu_First_Page()
    def __init__(self,parent=None):
        super(View_Menu,self).__init__(parent)
        self.resize(800,600)
        self.stackedwidget = QStackedWidget(self)
        self.stackedwidget.setGeometry(QtCore.QRect(0,0 , 800, 600))
        self.stackedwidget.setObjectName("stackwidget")
        self.add_first_page()

    #function to show first page
    def add_first_page(self):
        self.first_page = View_Menu_First_Page()
        self.stackedwidget.addWidget(self.first_page)
        self.stackedwidget.setCurrentIndex(0)
        self.first_page.label_malay.clicked.connect(lambda:self.add_second_page(self.first_page.Malay_link_click())) #only can use lambda: to make use of return value form functions
        self.first_page.label_mcdonalds.clicked.connect(lambda:self.add_second_page(self.first_page.MC_link_click())) #only can use lambda: to make use of return value form functions
        self.first_page.label_kfc.clicked.connect(lambda:self.add_second_page(self.first_page.KFC_link_click())) #only can use lambda: to make use of return value form functions
        self.first_page.label_subway.clicked.connect(lambda:self.add_second_page(self.first_page.Subway_link_click())) #only can use lambda: to make use of return value form functions

    #function to show second page
    def add_second_page(self,store):
        self.second_page = View_Menu_Second_Page(store)
        self.stackedwidget.addWidget(self.second_page)
        self.stackedwidget.setCurrentIndex(1)
        if self.second_page.label.text() == "Mcdonalds":
            self.second_page.BlueButton.clicked.connect(lambda:self.add_third_page(self.first_page.MC_link_click(),self.second_page.submit_click()))

    #function to show third page
    def add_third_page(self,store,date_and_time):
        self.third_page = View_Menu_Third_Page(store,date_and_time)
        self.stackedwidget.addWidget(self.third_page)
        self.stackedwidget.setCurrentIndex(2)
        self.third_page.BlueButton_2.clicked.connect(self.go_back)

    def go_back(self):
        self.stackedwidget.setCurrentIndex(0)
        self.stackedwidget.removeWidget(self.second_page)
        self.stackedwidget.removeWidget(self.third_page)

if __name__ == '__main__':
    import sys
    
    app =QtWidgets.QApplication(sys.argv)
    w = View_Menu()
    w.show()
    sys.exit(app.exec_())