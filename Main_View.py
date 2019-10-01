#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QListWidget, QStackedWidget, QHBoxLayout,\
    QListWidgetItem, QLabel
from View import Main_Page1
from View import Main_Page

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
        self.listWidget.currentRowChanged.connect(
            self.stackedWidget.setCurrentIndex)

        self.listWidget.setFrameShape(QListWidget.NoFrame)

        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
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
        item = QListWidgetItem( str('See other days menu'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem( str('View Recipts'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)
        item = QListWidgetItem( str('Exit'), self.listWidget)
        item.setSizeHint(QSize(16777215, 80))
        item.setTextAlignment(Qt.AlignCenter)

        

        
        main_window=Main_Page1.SlippedImgWidget('View/Pictures/bg.jpg', 'View/Pictures/fg.PNG')
        self.stackedWidget.addWidget(main_window)
        first_window = QWidget()
        ui=Main_Page.Ui_Main_page()
        ui.setupUi(first_window)
        self.stackedWidget.addWidget(first_window)

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
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.setStyleSheet(Stylesheet)
    w = LeftTabWidget()
    w.show()
    sys.exit(app.exec_())
