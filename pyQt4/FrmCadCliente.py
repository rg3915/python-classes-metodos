# -*- coding: utf-8 -*-
from FrmCadDefault import FrmCadDefault
from FrmPesquisaCliente import FrmPesquisaCliente
from PyQt4.QtGui import QApplication
from base import *
from Db import Db, ClientesDb

class FrmCadCliente(FrmCadDefault):

	def __init__(self,parent=None):
		super(FrmCadCliente,self).__init__(parent)

		self.frmCadClienteCreate()

		# abre o formulario FrmPesquisaCliente
		self.btnPesquisar.clicked.connect(self.AbrePesquisa)
		self.btnSalvar.clicked.connect(self.Salvar)
		self.btnExcluir.clicked.connect(self.__Excluir)

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

	def Salvar(self):
		try:
			#capturando os dados da tela
			Codigo = self.txtCodigo.text()
			Nome = self.txtNome.text()
			CPF = self.txtCPF.text()
			Email = self.txtEmail.text()
			Fone = self.txtFone.text()
			UF = str(self.txtUF.text()).upper()

			if Codigo == '':
				self.__inserir(Codigo, Nome, CPF, Email, Fone, UF)
				msg = MessageBox()
				msg.information(self, 'Cadastro de clientes', 'Cliente salvo com sucesso!', MessageBox.Ok)
			else:
				pass
		except Exception, e:
			msg = MessageBox()
			msg.critical(self, 'Cadastro de clientes', 	'Ocorreu o seguinte erro ao tentar inserir o cliente: \n ' + str(e), MessageBox.Ok)

	def __inserir(self, id, cpf, nome, email, fone, uf):
		'''Método cria um objeto cliente do modulo de acesso a dados, e inclui um novo cliente no banco'''
		self.clientedb.Salvar(id, cpf, nome, email, fone, uf)

	def __Excluir(self, pId):
		try:
			codigo = int(self.txtCodigo.text())
			self.clientedb.Excluir(codigo)
		except Exception, e:
			msg = MessageBox()
			msg.critical(self, 'Cadastro de clientes', 'Ocorreu o seguinte erro ao tentar excluir: \n ' + str(e).decode('utf8', MessageBox.Ok)

if __name__ == '__main__':
	import sys
	root = QApplication(sys.argv)
	app = FrmCadCliente(None)
	app.show()
	root.exec_()