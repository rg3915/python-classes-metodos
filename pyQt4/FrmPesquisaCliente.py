# -*- coding: utf-8 -*-
from base import *
from Db import ClientesDb

class FrmPesquisaCliente(Dialog):

	def __init__(self,parent=None):
		super(FrmPesquisaCliente,self).__init__(parent)

		self.frmPesquisaClienteCreate()
		self.btnBuscar.clicked.connect(self.PesquisarCliente)

		#criando um objeto cliente DB para que fique disponível para interagir c/ o módulo de acesso a dados
		self.clientedb = ClientesDb()

		self.CenterOnScreen()

	def frmPesquisaClienteCreate(self):
		self.setWindowTitle(u'Pesquisa de clientes')
		self.resize(450,300)

		self.layoutPrincipal=LayoutVertical()

		# criando campo de busca
		self.lblBusca=Label('Busca',self)
		self.txtBusca=TextBox(self)
		self.btnBuscar = Botao('&Buscar', self)

		hboxBusca=LayoutHorizontal()
		hboxBusca.addWidget(self.lblBusca)
		hboxBusca.addWidget(self.txtBusca)
		hboxBusca.addWidget(self.btnBuscar)

		self.layoutPrincipal.addLayout(hboxBusca)

		# criando o grid da pesquisa
		cabecalho_grid=[u'Código', 'Nome', 'email', 'UF']
		self.grdPesquisaCliente=Grid(self,0,len(cabecalho_grid))
		self.grdPesquisaCliente.setHorizontalHeaderLabels(cabecalho_grid)

		# desativando edição do grid de pesquisa
		self.grdPesquisaCliente.setEditTriggers(QAbstractItemView.NoEditTriggers)

		# redimensionando as colunas do grid
		self.grdPesquisaCliente.setColumnWidth(1,300)
		self.grdPesquisaCliente.setColumnWidth(2,200)


		# botao fechar
		self.btnFechar=Botao('&Fechar',self)
		self.btnFechar.clicked.connect(self.close)

		self.layoutPrincipal.addWidget(self.grdPesquisaCliente)
		self.layoutPrincipal.addWidget(self.btnFechar)

		self.setLayout(self.layoutPrincipal)

	def PesquisarCliente(self, e):
		'''Método faz uma busca de clientes no banco de dados, e cria uma lista de tuplas'''
		# faz a consulta no banco e recebe uma lista de tuplas
		texto_busca = str(self.txtBusca.text())
		lista_dados_cliente = self.clientedb.ConsultaClientesPorNome(texto_busca)

		# setando no grid a quant de linhas, com a mesma quant de registros da lista
		quant_registros = len(lista_dados_cliente)
		self.grdPesquisaCliente.setRowCount(quant_registros)

		linha = 0
		for cliente in lista_dados_cliente:
			# capturando os dados da tupla
			id_cliente = cliente[0]
			Nome_cliente = cliente[1]
			Email_cliente = cliente[2]
			UF_cliente = cliente[3]

			# preenche o grid de pesquisa
			self.grdPesquisaCliente.setItem(linha, 0, QTableWidgetItem(id_cliente))
			self.grdPesquisaCliente.setItem(linha, 1, QTableWidgetItem(Nome_cliente))
			self.grdPesquisaCliente.setItem(linha, 2, QTableWidgetItem(Email_cliente))
			self.grdPesquisaCliente.setItem(linha, 3, QTableWidgetItem(UF_cliente))

			linha += 1

	def centerOnScreen(self):
		resolucao = QDesktopWidget().screenGeometry()
		self.move((resolucao.width()/2) - (self.frameSize().width()/2),
				   (resolucao.height()/2) - (self.frameSize().height()/2))

if __name__ == '__main__':
	import sys
	root = QApplication(sys.argv)
	app = FrmPesquisaCliente(None)
	app.show()
	root.exec_()