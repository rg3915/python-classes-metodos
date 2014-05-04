from PyQt4.QtCore import *
from PyQt4.QtGui import *

class main(QWidget):

	def __init__(self, parent = None):
		super(main, self).__init__(parent)

		txtNome = QLineEdit(self)
		txtSobrenome = QLineEdit(self)
		txtIdade = QLineEdit(self)

		flayout = QFormLayout()
		flayout.addRow('Nome:',txtNome)
		flayout.addRow('Sobrenome:',txtSobrenome)
		flayout.addRow('Idade:',txtIdade)

		self.setLayout(flayout)
		
if __name__ == '__main__':
	import sys
	root = QApplication(sys.argv)
	app = main(None)
	app.show()
	root.exec_()