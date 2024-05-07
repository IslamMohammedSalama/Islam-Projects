from PyQt5 import QtCore , QtGui , QtWidgets 
from PyQt5.QtGui import QPixmap
import sys

root = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.resize(500,500)
w.move(50,100)
w.setWindowTitle('<i>my project</i>')
w.setWindowIcon(QtGui.QIcon('/home/shared/Islam-projects/Python/gui_apps/Qt5/chatgpt-icon.svg'))
l= QtWidgets.QLabel('<a href="https://www.youtube.com/watch?v=nj2cbHv7FMw&list=PLSiLeKadTQ7kaP11ZEN-w8wX3aGeDNSEW&index=24">you</a>')
l.move(100,100)
w.show()
root.exec_()