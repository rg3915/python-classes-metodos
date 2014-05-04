# -*- coding: utf-8 -*-
from FrmCadDefault import FrmCadDefault
from FrmPesquisaCliente import FrmPesquisaCliente
from PyQt4.QtGui import QApplication
from base import *

class FrmCadCliente(FrmCadDefault):

	def __init__(self,parent=None):
		super(FrmCadCliente,self).__init__(parent)

		self.frmCadClienteCreate()

		# abre o formulario FrmPesquisaCliente
		self.btnPesquisar.clicked.connect(self.AbrePesquisa)

		# imprimir
		self.btnImprimir.clicked.connect(self.Imprimir)

	def frmCadClienteCreate(self):
		self.setWindowTitle('Cadastro de clientes')

		#criando os campos de cadastro
		self.txtNome=TextBox(self)
		self.txtCPF=TextBox(self)
		self.txtCPF.setFixedWidth(170)
		self.txtCPF.setMaxLength(11)
		self.txtEmail=TextBox(self)
		self.txtFone=TextBox(self)
		self.txtUF=TextBox(self)
		self.txtUF.setFixedWidth(40)
		self.txtUF.setMaxLength(2)

		#adicionando os campos no form layout da base de cadastro
		self.fLayout.addRow('Nome',self.txtNome)
		self.fLayout.addRow('CPF',self.txtCPF)
		self.fLayout.addRow('e-mail',self.txtEmail)
		self.fLayout.addRow('Fone',self.txtFone)
		self.fLayout.addRow('UF',self.txtUF)

	def AbrePesquisa(self):
		frmPesquisa=FrmPesquisaCliente(self)
		frmPesquisa.setModal(True) #tela em primeiro plano
		frmPesquisa.show()
		frmPesquisa.exec_()

	def Imprimir(self):
		print self.txtNome.text()
		print self.txtCPF.text()

if __name__ == '__main__':
	import sys
	root = QApplication(sys.argv)
	app = FrmCadCliente(None)
	app.show()
	root.exec_()