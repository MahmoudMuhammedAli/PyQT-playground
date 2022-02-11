from random import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
  def __init__(self):
    super(MyWindow, self).__init__()
    self.setGeometry(200, 200, 300, 300)
    self.setWindowTitle("catch the button")
    self.initUI()

  def initUI(self):
    self.label = QtWidgets.QLabel(self)
    self.label.setText("Wild button")
    self.label.move(50, 50)

    self.b1 = QtWidgets.QPushButton(self)
    self.b1.setText("catch me!")
    self.b1.clicked.connect(self.clicked)

  def clicked(self):
    self.b1.move(random()*100, random()*100)

def __init__():
  app = QApplication(sys.argv)
  win = MyWindow()
  win.show()
  sys.exit(app.exec_())

__init__()