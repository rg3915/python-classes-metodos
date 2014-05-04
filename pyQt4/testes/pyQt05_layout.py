from PyQt4.QtCore import *
from PyQt4.QtGui import *

class main(QWidget):

	def __init__(self, parent = None):
		super(main, self).__init__(parent)

		layoutPrincipal = QVBoxLayout()

		self.setMinimumSize(400,250)
		self.setWindowTitle('Layout')
		txtNome = QLineEdit(self)
		txtSobrenome = QLineEdit(self)
		txtIdade = QLineEdit(self)

		flayout = QFormLayout()
		flayout.addRow('Nome:',txtNome)
		flayout.addRow('Sobrenome:',txtSobrenome)
		flayout.addRow('Idade:',txtIdade)

		layoutPrincipal.addLayout(flayout)

		btnOK = QPushButton('OK', self)
		btnCancelar = QPushButton('Cancelar', self)

		hboxBotoes = QHBoxLayout()
		hboxBotoes.addStretch(2) # se quiser do lado esquerdo coloque este comando depois das duas linhas abaixo
		hboxBotoes.addWidget(btnOK)
		hboxBotoes.addWidget(btnCancelar)

		layoutPrincipal.addLayout(hboxBotoes)

		self.setLayout(layoutPrincipal)
		
if __name__ == '__main__':
	import sys
	root = QApplication(sys.argv)
	app = main(None)
	app.show()
	root.exec_()