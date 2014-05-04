# -*- coding: utf-8 -*-
from base import *

class FrmCadDefault(Widget):

	def __init__(self,parent=None):
		super(FrmCadDefault,self).__init__(parent)

		self.frmCadDefaultCreate()

	def frmCadDefaultCreate(self):
		self.setWindowTitle(u'Cadastro padrão')
		# self.center()
		self.layoutPrincipal=LayoutVertical()

		self.txtCodigo=TextBox(self)
		self.txtCodigo.setFixedWidth(200)
		self.ckAtivo=CheckBox('Ativo',self)
		self.ckAtivo.setChecked(True)

		hboxcodigo=LayoutHorizontal()
		hboxcodigo.addWidget(self.txtCodigo)
		hboxcodigo.addWidget(self.ckAtivo)
		hboxcodigo.addStretch(2)

		self.fLayout=FormLayout()
		self.fLayout.addRow(u'Código',hboxcodigo)

		# Adicionando form layout layout principal
		self.layoutPrincipal.addLayout(self.fLayout)

		# Botoes
		self.btnNovo=Botao('&Novo',self)
		self.btnSalvar=Botao('&Salvar',self)
		self.btnPesquisar=Botao('&Pesquisar',self)
		self.btnImprimir=Botao('&Imprimir',self)

		hboxBotoes=LayoutHorizontal()
		hboxBotoes.addStretch(2)
		hboxBotoes.addWidget(self.btnNovo)
		hboxBotoes.addWidget(self.btnSalvar)
		hboxBotoes.addWidget(self.btnPesquisar)
		hboxBotoes.addWidget(self.btnImprimir)

		self.layoutPrincipal.addLayout(hboxBotoes)

		self.setLayout(self.layoutPrincipal)

	# def center(self):
	# 	qr=self.frameGeometry()
	# 	cp=QtGui.QDesktopWidget().availableGeometry().center()
	# 	qr.moveCenter(cp)
	# 	self.move(qr.topLeft())

if __name__ == '__main__':
	import sys
	root = QApplication(sys.argv)
	app = FrmCadDefault(None)
	app.show()
	root.exec_()