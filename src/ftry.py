# simple pyqt5 example with a lable and a button
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def clicked():
    print("clicked")


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100, 100, 500, 300)
    win.setWindowTitle('PyQt5 Example')
    label = QtWidgets.QLabel(win)
    label.setText('This is a PyQt5 Example')
    label.move(100, 70)
    button = QtWidgets.QPushButton(win)
    button.setText('Click Me')
    button.move(100, 100)

    # map the function to the button
    button.clicked.connect(clicked)
    win.show()
    sys.exit(app.exec_())


window()
