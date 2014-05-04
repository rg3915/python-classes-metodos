# -*- coding: utf-8 -*-
from base import *

class FrmGif(Widget):

	def __init__(self,parent=None):
		super(FrmGif,self).__init__()

		self.frmGif()

	def frmGif(self):
		self.resize(166,190)
		self.show_gif = QLabel(self)
		self.gif = QMovie("walking-man2.gif")
		self.show_gif.setMovie(self.gif)
		self.gif.start()

if __name__ == '__main__':
	import sys
	root = QApplication(sys.argv)
	app = FrmGif(None)
	app.show()
	root.exec_()