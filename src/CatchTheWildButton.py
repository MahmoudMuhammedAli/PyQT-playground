from random import random
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
  i=0
  def __init__(self):
    super(MyWindow, self).__init__()
    
    self.setGeometry(0, 0, 1920, 1080)
    self.setWindowTitle("catch the button")
    self.initUI()

  def initUI(self):
    self.label = QtWidgets.QLabel(self)
    self.label.setText("Wild button")
    self.label.setBaseSize(100, 100)

    self.b1 = QtWidgets.QPushButton(self)
    self.b1.setText("catch me!")
    self.b1.clicked.connect(self.clicked)

  def clicked(self):
    self.b1.move(random()*1000, random()*1000)
    self.i+= 1
    self.label.setText(str(self.i))

def __init__():
  app = QApplication(sys.argv)
  win = MyWindow()
  win.show()
  sys.exit(app.exec_())

__init__()