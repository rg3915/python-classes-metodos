# -*- coding: utf-8 -*-
import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# styleFile=os.path.join(os.path.split(__file__)[0],"style.stylesheet")
# with open(styleFile,'r') as fh:
# 	self.setStyleSheet(fh.read())

class TextBox(QLineEdit):

	def __init__(self, parent=None):
		super(TextBox, self).__init__(parent)

class Label(QLabel):

	def __init__(self, pText='', parent=None):
		super(Label, self).__init__(parent)

		self.setText(pText)

class CheckBox(QCheckBox):

	def __init__(self, pText='', parent=None):
		super(CheckBox, self).__init__(parent)

		self.setText(pText)

class Botao(QPushButton):

	def __init__(self, pText='', parent=None):
		super(Botao, self).__init__(parent)

		self.setText(pText)

class LayoutVertical(QVBoxLayout):

	def __init__(self):
		super(LayoutVertical, self).__init__()

class LayoutHorizontal(QHBoxLayout):

	def __init__(self):
		super(LayoutHorizontal, self).__init__()

class Widget(QWidget):

	def __init__(self, parent=None):
		super(Widget, self).__init__()


class FormLayout(QFormLayout):

	def __init__(self):
		super(FormLayout, self).__init__()


class Dialog(QDialog):

	def __init__(self, parent=None):
		super(Dialog, self).__init__(parent)

class Grid(QTableWidget):

	def __init__(self, parent=None, qtde_linhas=0, qtde_colunas=0):
		super(Grid,self).__init__(parent)

		self.setRowCount(qtde_linhas)
		self.setColumnCount(qtde_colunas)

		self.resizeRowsToContents()
		self.setAlternatingRowColors(True)
		self.setSortingEnabled(True)
