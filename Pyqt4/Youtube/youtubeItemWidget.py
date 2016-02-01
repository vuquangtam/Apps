# -*- coding: utf8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_youtubeItemWidget
import sys
import os
import requests

def resource_path(relative):
	'''fix pyinstaller error path of cacert.pem(requests certificate)'''
	return os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")),
						relative)

cert_path = resource_path('cacert.pem')  # request certificate path
print cert_path

class YoutubeItem(QWidget, ui_youtubeItemWidget.Ui_YoutubeItemWidget):
	def __init__(self, **kwargs):
		super(QWidget, self).__init__(**kwargs)
		self.setupUi(self)

	def setThumbnail(self, url, internet=True):
		if internet:
			req = requests.get(url, verify=cert_path)
			try:
				req.raise_for_status()
				data = req.content
				print data
				image = QImage()
				image.loadFromData(data)
				scaledPixmap = image.scaled(self.thumbnail.size(), Qt.KeepAspectRatio)

				self.thumbnail.setPixmap(QPixmap(scaledPixmap))
			except:
				pass
		else:
			self.thumbnail.setPixmap(QPixmap(url))

	def setTitle(self, value):
		self.title.setText(unicode(value))

	def setAuthor(self, value):
		self.author.setText(unicode(value))

	def setLength(self, value):
		self.length.setText(unicode(value))

	def setView(self, value):
		self.view.setText(unicode(value))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	main_window = YoutubeItem()
	main_window.resize(400, 300)
	main_window.setThumbnail(r'http://maton.com.au/assets/images/acoustic_product_TE_3.jpg', True)
	main_window.show()
	app.exec_()