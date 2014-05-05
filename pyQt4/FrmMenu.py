# -*- coding: utf-8 -*-
from FrmCadDefault import FrmCadDefault
from FrmCadCliente import FrmCadCliente
from FrmPesquisaCliente import FrmPesquisaCliente
from FrmGif import FrmGif
from base import *

class FrmMenu(Widget):

	def __init__(self,parent=None):
		super(FrmMenu,self).__init__(parent)

		self.frmMenu()

	def frmMenu(self):
		self.setWindowTitle('Menu principal')
		#self.centerOnScreen()
		self.resize(400,300)		
		self.layoutPrincipal=LayoutVertical()

		# Botoes
		self.btnCadCliente=Botao('&Cadastro de Cliente',self)
		self.btnCadCliente.clicked.connect(self.AbreCadastro)
		self.btnPesquisaCliente=Botao('&Pesquisa Cliente',self)
		self.btnPesquisaCliente.clicked.connect(self.AbrePesquisa)
		self.btnGif=Botao('&Gif animado',self)
		self.btnGif.clicked.connect(self.AbreGif)
		self.btnFechar=Botao('&Fechar',self)
		self.btnFechar.clicked.connect(self.close)

		self.show_gif=QLabel(self)
		self.show_gif.resize(166,190)
		self.gif=QMovie("walking-man2.gif")
		self.show_gif.setMovie(self.gif)
		self.gif.start()

		hboxBotoes=LayoutHorizontal()
		hboxBotoes.addWidget(self.btnCadCliente)
		hboxBotoes.addWidget(self.btnPesquisaCliente)
		hboxBotoes.addWidget(self.btnGif)
		hboxBotoes.addWidget(self.btnFechar)
		hboxBotoes.addStretch(2)

		self.layoutPrincipal.addLayout(hboxBotoes)
		self.layoutPrincipal.addWidget(self.show_gif)
		self.setLayout(self.layoutPrincipal)

	def AbreCadastro(self):
		frmCadastro=FrmCadCliente(self)
		#frmCadastro.setModal(True)
		frmCadastro.show()
		frmCadastro.exec_()

	def AbrePesquisa(self):
		frmPesquisa=FrmPesquisaCliente(self)
		frmPesquisa.setModal(True) #tela em primeiro plano
		frmPesquisa.show()
		frmPesquisa.exec_()

	def AbreGif(self):
		frmGif=FrmGif(self)
		frmGif.show()
		frmGif.exec_()

if __name__ == '__main__':
	import sys
	root = QApplication(sys.argv)
	app = FrmMenu(None)
	app.show()
	root.exec_()