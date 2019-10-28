#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize 
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QListWidget, QStackedWidget, QHBoxLayout, QListWidgetItem, QLabel , QMessageBox
from View import Main_Page1
from View import McDonalds
from View import ViewMenu
import sys
from PyQt5.QtWidgets import QApplication
from datetime import datetime
import pytz

class LeftTabWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(LeftTabWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self)
        layout.addWidget(self.listWidget)
        self.stackedWidget = QStackedWidget(self)
        layout.addWidget(self.stackedWidget)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Canteen")
        self.listWidget.currentRowChanged.connect(self.stackedWidget.setCurrentIndex)  #core feature, connect row change with the stack widget and display
        self.listWidget.setFrameShape(QListWidget.NoFrame)

        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #add left side list widgets
        item = QListWidgetItem(QIcon(''), str('Main Page'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem(QIcon('View/Logo/McDonald.ico'), str('McDonalds'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem(QIcon('View/Logo/Subway.ico'), str('Subway'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem(QIcon('View/Logo/Malay_food.ico'), str('Malay'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem(QIcon('View/Logo/kFC.ico'), str('KFC'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem( str('View menu'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem( str('Cart and pay'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        # item = QListWidgetItem( str('Exit'), self.listWidget)
        # item.setSizeHint(QSize(16777215, 80))
        # item.setTextAlignment(Qt.AlignCenter)

        
    #------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------
    #add right side stack widget

        
        # Main page
        main_window=Main_Page1.SlippedImgWidget('View/Pictures/bg.jpg', 'View/Pictures/fg.PNG')
        self.stackedWidget.addWidget(main_window)

        #Mcdonalds Page
        time_zone = pytz.timezone('Asia/Singapore') 
        current_time = datetime.now(time_zone)
        if current_time.hour <= 12:
            McDonalds_window = McDonalds.Breakfast_Mcdonald()
        elif current_time.hour >12:
            McDonalds_window = McDonalds.Lunch_Mcdonald()  
        self.stackedWidget.addWidget(McDonalds_window)

        #Subway Page
        label = QLabel('Dummy Page ', self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet('background: rgb(%d, %d, %d);margin: 50px;' % (randint(0, 255), randint(0, 255), randint(0, 255)))
        self.stackedWidget.addWidget(label)


        #Malay Page
        label = QLabel('Dummy Page ', self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet('background: rgb(%d, %d, %d);margin: 50px;' % (randint(0, 255), randint(0, 255), randint(0, 255)))
        self.stackedWidget.addWidget(label)


        
        #KFC Page
        label = QLabel('Dummy Page ', self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet('background: rgb(%d, %d, %d);margin: 50px;' % (randint(0, 255), randint(0, 255), randint(0, 255)))
        self.stackedWidget.addWidget(label)



        #view menu page
        view_menu_window = ViewMenu.View_Menu()
        self.stackedWidget.addWidget(view_menu_window)


        #pay and cart page






Stylesheet = """

QListWidget, QListView, QTreeWidget, QTreeView {
    outline: 0px;
}

QListWidget {
    min-width: 120px;
    max-width: 120px;
    color: white;
    background: black;
}

QListWidget::item:selected {
    background: rgb(52, 52, 52);
    border-left: 2px solid rgb(9, 187, 7);
}

HistoryPanel::item:hover {
    background: rgb(52, 52, 52);
}


QStackedWidget {
    background: rgb(30, 30, 30);
}

QLabel {
    color: white;
}
"""

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet(Stylesheet)
    w = LeftTabWidget()
    w.show()
    sys.exit(app.exec_())