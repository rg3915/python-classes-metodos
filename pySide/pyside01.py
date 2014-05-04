import sys
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication(sys.argv)

label = QLabel("Ola mundo!")
label.show()

app.exec_()
sys.exit()