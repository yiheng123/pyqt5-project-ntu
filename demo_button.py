import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QApplication

StyleSheet = '''

QPushButton {
    border: none; 
}
/*

*/
QPushButton#RedButton {
    background-color: #f44336; /*BGCOLOR*/
}
#RedButton:hover {
    background-color: #e57373; /*BGCOLOR_ONBLUR*/
}

#RedButton:pressed {
    background-color: #ffcdd2; /*On_press color*/
}
#GreenButton {
    background-color: #4caf50;
    border-radius: 5px; /*Round angle*/
}
#GreenButton:hover {
    background-color: #81c784;
}
#GreenButton:pressed {
    background-color: #c8e6c9;
}
#BlueButton {
    background-color: #2196f3;
    /*minimum size*/
    min-width: 96px;
    max-width: 96px;
    min-height: 96px;
    max-height: 96px;
    border-radius: 48px; /*Round*/
}
#BlueButton:hover {
    background-color: #64b5f6;
}
#BlueButton:pressed {
    background-color: #bbdefb;
}
#OrangeButton {
    max-height: 48px;
    border-top-right-radius: 20px; /*right top round angel*/
    border-bottom-left-radius: 20px; /*left bottom round angel*/
    background-color: #ff9800;
}
#OrangeButton:hover {
    background-color: #ffb74d;
}
#OrangeButton:pressed {
    background-color: #ffe0b2;
}
/*sort by contents or other attributes*/
QPushButton[text="purple button"] {
    color: white; /*text color*/
    background-color: #9c27b0;
}
'''


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        layout.addWidget(QPushButton("red button", self,
                                     objectName="RedButton", minimumHeight=48))
        layout.addWidget(QPushButton("green button", self,
                                     objectName="GreenButton", minimumHeight=48))
        layout.addWidget(QPushButton("blue button", self,
                                     objectName="BlueButton", minimumHeight=48))
        layout.addWidget(QPushButton("orange button", self,
                                     objectName="OrangeButton", minimumHeight=48))
        layout.addWidget(QPushButton("purple button", self,
                                     objectName="PurpleButton", minimumHeight=48))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(StyleSheet)
    w = Window()
    w.show()
    sys.exit(app.exec_())
