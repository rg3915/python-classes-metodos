import sys
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication(sys.argv)

class main(QWidget):

	def __init__(self):
		QWidget.__init__(self)
		self.setMinimumSize(400,185)
		self.setWindowTitle('Meu programa')
		self.lbl_nome = QLabel('Nome:',self)
		self.lbl_nome.move(10,10)
		self.txt_nome = QLineEdit(self)
		self.txt_nome.setMinimumWidth(285)
		self.txt_nome.move(60,10)
		self.lbl_sauda = QLabel('Esperando para saudar...',self)
		self.lbl_sauda.move(200,100)
		self.btn_saudar = QPushButton('Saudar',self)
		self.btn_saudar.setMinimumWidth(145)
		self.btn_saudar.move(250,150)
		self.btn_saudar.clicked.connect(self.clicked_btn_saudar)

	def clicked_btn_saudar(self):
		sauda = 'Ola %s!!!'%self.txt_nome.text()
		self.lbl_sauda.setText(sauda)

	def run(self):
		self.show()
		app.exec_()

app_main = main()
app_main.run()