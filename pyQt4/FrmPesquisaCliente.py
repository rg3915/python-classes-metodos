# -*- coding: utf-8 -*-
from base import *

class FrmPesquisaCliente(Dialog):

	def __init__(self,parent=None):
		super(FrmPesquisaCliente,self).__init__(parent)

		self.frmPesquisaClienteCreate()

	def frmPesquisaClienteCreate(self):
		self.setWindowTitle(u'Pesquisa de clientes')
		self.resize(450,300)

		self.layoutPrincipal=LayoutVertical()

		# criando campo de busca
		self.lblBusca=Label('Busca',self)
		self.txtBusca=TextBox(self)

		hboxBusca=LayoutHorizontal()
		hboxBusca.addWidget(self.lblBusca)
		hboxBusca.addWidget(self.txtBusca)

		self.layoutPrincipal.addLayout(hboxBusca)

		# criando o grid da pesquisa
		cabecalho_grid=[u'Código', 'Nome', 'email', 'UF']
		self.grdPesquisaCliente=Grid(self,1,len(cabecalho_grid))
		self.grdPesquisaCliente.setHorizontalHeaderLabels(cabecalho_grid)

		# botao fechar
		self.btnFechar=Botao('&Fechar',self)
		self.btnFechar.clicked.connect(self.close)

		self.layoutPrincipal.addWidget(self.grdPesquisaCliente)
		self.layoutPrincipal.addWidget(self.btnFechar)

		self.setLayout(self.layoutPrincipal)

if __name__ == '__main__':
	import sys
	root = QApplication(sys.argv)
	app = FrmPesquisaCliente(None)
	app.show()
	root.exec_()