from PyQt4.QtCore import *
from PyQt4.QtGui import *

class main(QMainWindow):

	def __init__(self, parent = None):
		super(main, self).__init__(parent)

		txtNome = QLineEdit(self)
		btnBotao = QPushButton('OK',self)
		btnBotao.move(110,0)
		ckbCheck = QCheckBox('Marque',self)
		ckbCheck.move(0,50)
		
if __name__ == '__main__':
	import sys
	root = QApplication(sys.argv)
	app = main(None)
	app.show()
	root.exec_()