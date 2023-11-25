import json
from PyQt6 import QtCore, QtWidgets
import random
from PyQt6.QtGui import QFont, QColor


class ChristmasCalendar(QtWidgets.QMainWindow):
    def __init__(self):
        super(ChristmasCalendar, self).__init__()

        # set window size and title
        self.setMinimumSize(QtCore.QSize(1000, 650))
        self.setWindowTitle('Christmas Calendar')
        # Set grid layout
        widget = QtWidgets.QWidget(self)
        self.setCentralWidget(widget)
        grid = QtWidgets.QGridLayout()
        widget.setLayout(grid)

        # create 24 buttons
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("1")
        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setText("2")
        self.button3 = QtWidgets.QPushButton(self)
        self.button3.setText("3")
        self.button4 = QtWidgets.QPushButton(self)
        self.button4.setText("4")
        self.button5 = QtWidgets.QPushButton(self)
        self.button5.setText("5")
        self.button6 = QtWidgets.QPushButton(self)
        self.button6.setText("6")
        self.button7 = QtWidgets.QPushButton(self)
        self.button7.setText("7")
        self.button8 = QtWidgets.QPushButton(self)
        self.button8.setText("8")
        self.button9 = QtWidgets.QPushButton(self)
        self.button9.setText("9")
        self.button10 = QtWidgets.QPushButton(self)
        self.button10.setText("10")
        self.button11 = QtWidgets.QPushButton(self)
        self.button11.setText("11")
        self.button12 = QtWidgets.QPushButton(self)
        self.button12.setText("12")
        self.button13 = QtWidgets.QPushButton(self)
        self.button13.setText("13")
        self.button14 = QtWidgets.QPushButton(self)
        self.button14.setText("14")
        self.button15 = QtWidgets.QPushButton(self)
        self.button15.setText("15")
        self.button16 = QtWidgets.QPushButton(self)
        self.button16.setText("16")
        self.button17 = QtWidgets.QPushButton(self)
        self.button17.setText("17")
        self.button18 = QtWidgets.QPushButton(self)
        self.button18.setText("18")
        self.button19 = QtWidgets.QPushButton(self)
        self.button19.setText("19")
        self.button20 = QtWidgets.QPushButton(self)
        self.button20.setText("20")
        self.button21 = QtWidgets.QPushButton(self)
        self.button21.setText("21")
        self.button22 = QtWidgets.QPushButton(self)
        self.button22.setText("22")
        self.button23 = QtWidgets.QPushButton(self)
        self.button23.setText("23")
        self.button24 = QtWidgets.QPushButton(self)
        self.button24.setText("24")
        # add buttons to a list
        self.buttons_list = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9, self.button10, self.button11, self.button12, self.button13, self.button14, self.button15, self.button16, self.button17, self.button18, self.button19, self.button20, self.button21, self.button22, self.button23, self.button24]
        # add button action to all buttons in the list
        [self.btn.clicked.connect(self.proceed) for self.btn in self.buttons_list]
        # shuffle list
        random.shuffle(self.buttons_list)

        # UI style adjustments: create 4 rows with buttons and set the button background and font
        for _ in [0, 1, 2, 3]:
            for self.bt in self.buttons_list:
                self.bt.setStyleSheet("border: 0; background: transparent;")
                if self.bt == self.button24:
                    # make font for number 24 bigger
                    self.bt.setFont(QFont('cursive', 56))
                else:
                    self.bt.setFont(font)
                grid.addWidget(self.bt)
            # adjust column stretch
            grid.setColumnStretch(0, 1)
            grid.setColumnStretch(1, 1)
            grid.setColumnStretch(2, 1)
            grid.setColumnStretch(3, 1)
            grid.setColumnStretch(4, 1)
            grid.setColumnStretch(5, 1)

    # button action
    def proceed(self):
        msg = QtWidgets.QMessageBox(self)
        # get text
        text = self.get_content()
        msg.setText(str(text))
        msg.setFont(QFont('times', 14))
        msg.exec()

    # get content from file
    def get_content(self):
        # read file
        with open("assets/contents/contents.json", "r", encoding="UTF-8") as file:
            all_content = json.load(file)
        # use random value from file
        todays_content = all_content["values"][random.randint(0, len(all_content["values"]) - 1)]
        # remove displayed item from file
        all_content["values"].remove(todays_content)
        with open("assets/contents/contents.json", "w", encoding="UTF-8") as file:
            file.write(json.dumps(all_content))

        return todays_content


# set style and image
stylesheet = """
    ChristmasCalendar {
        border-image: url("assets/background/bgpic.png"); 
        background-position: center;
    }
"""
font = QFont('cursive', 28)


# start application
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app.setStyleSheet(stylesheet)
    window = ChristmasCalendar()
    window.show()
    app.exec()
