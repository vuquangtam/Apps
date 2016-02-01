# -*- coding: utf8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_youtubeDownloadWindow
import youtubeItemWidget
import videoPlayerWidget
import sys
import os
import requests
import bs4
import json
import threading
import pafy

def resource_path(relative):
	'''fix pyinstaller error path of cacert.pem(requests certificate)'''
	return os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")),
						relative)

cert_path = resource_path('cacert.pem')  # request certificate path

threading.Thread.daemon = True  # doesn't wait thread finish

def getYoutubeObject(url):
	'''Main function to get data'''
	#url = "https://www.youtube.com/watch?v=JOX-krmWf8Q"
	try:
		url = url.strip()
		if url:
			all_videos = []

			if 'watch?v' in url.lower() or 'playlist?list' in url.lower():  # if url is video(playlist) youtube links
				all_videos = getYoutubeVideo(url)
			elif url.lower().startswith('u:'):  # if url is keyword search for user
				url = url.lstrip('u:')
				all_videos = getYoutubeVideoBySearchQuery(url, 5, 'user')
			elif 'watch?v' not in url.lower():  # if url is keyword search for video
				all_videos = getYoutubeVideoBySearchQuery(url, 5, 'video')
			else:  # if url is other youtube link
				all_videos = getYoutubeVideoBySearchQuery(url, 5)
		else:
			return False
		return all_videos
	except:
		print sys.exc_info()

def getAjaxVideoData(url):
	'''get ajax data in user video url, the ajax response contains two keys :
		content_html: include all video html obj to parse
		load_more_widget_html: contain the url to request next ajax data
	'''
	data = requests.get(url, verify=cert_path)  # cert_path in the beginning
	data.raise_for_status()
	ajax_json_data = json.loads(data.text)  # because the response is json, load from text to object

	content_soup = bs4.BeautifulSoup(ajax_json_data['content_html'], "html.parser")  # create the bs4(to select html object), html.parser is optional arg of bs4 (dont print result to console)
	ajax_content_elements = content_soup.select('.yt-lockup-title a')  # .yt-lockup-title class is the video html class
	ajax_content_urls = []
	for element in ajax_content_elements:
		ajax_content_urls.append(element.get('href'))  # get href attr of html object

	ajax_request_soup = bs4.BeautifulSoup(ajax_json_data['load_more_widget_html'], "html.parser")
	ajax_request_elements = ajax_request_soup.select('button[data-uix-load-more-href]')  # select by attr data-uix-load-more-href of button html object
	try:
		ajax_request_url = ajax_request_elements[0].get('data-uix-load-more-href')  # data-uix-load-more-href contain the next ajax url request
	except:
		ajax_request_url = ''

	return [ajax_content_urls, ajax_request_url]

def getYoutubeVideoBySearchQuery(url, max_videos=5, mode=None):
	if mode == 'video':  # search keyword for videos
		url = r'https://www.youtube.com/results?search_query=' + url
	if mode == 'user':  # search keyword for video in users
		url = r'https://www.youtube.com/user/' + url + '/videos'
	data = requests.get(url, verify=cert_path)
	data.raise_for_status()
	soup = bs4.BeautifulSoup(data.text, "html.parser")
	link_elements = soup.select('.yt-lockup-title a')

	all_links = []
	count = 0
	for elements in link_elements:
		if 'watch' in elements.get('href'):  # if url is youtube video (contains watch blabla)
			all_links.append(elements.get('href'))
			count += 1
		if max_videos == u'Tất Cả':
			continue
		elif count == int(max_videos):
			break

	if r'/user' in url and max_videos == u'Tất Cả':  # get all video in user videos page (recursive "load more" button)
		ajax_video_urls = soup.select('button[data-uix-load-more-href]')
		link = ajax_video_urls[0].get('data-uix-load-more-href')
		while link:  # recursive "load more" button
			link = 'https://www.youtube.com' + link
			video_urls, link = getAjaxVideoData(link)
			all_links += video_urls

	return getYoutubeVideo('\n'.join(all_links))

def getYoutubeVideo(url):
	'''get data from video urls
		url format : 'link' or 'link\nlink\nlink blabla'
	'''
	all_videos = []
	for link in url.split('\n'):
		if 'playlist?list' in link.lower():
			all_videos += getYoutubePlaylist(link)
		elif 'watch?v' in link.lower():
			video = pafy.new(link)
			all_videos.append(video)
		else:
			continue
	return all_videos

def getYoutubePlaylist(plurl):
	'''get data from playlist url'''
	all_videos = []
	playlist = pafy.get_playlist(plurl)
	for video in playlist['items']:
		all_videos.append(video['pafy'])
	return all_videos

class MainWindow(QMainWindow, ui_youtubeDownloadWindow.Ui_YoutubeDownloadWindow):
	def __init__(self, **kwargs):
		super(QMainWindow, self).__init__(**kwargs)
		self.setupUi(self)
		self.video = videoPlayerWidget.VideoPlayer(parent=self.videoDockWidget)
		self.videoDockWidget.setWidget(self.video)
		#self.videoDockWidget.hide()

	def search(self):
		self.clearListWidget(self.video_list)
		keyword = unicode(self.search_box.text())
		all_videos = getYoutubeObject(keyword)
		if all_videos:
			for video in all_videos:
				item = QListWidgetItem(parent=self.video_list)
				item.setSizeHint(QSize(0, 65))
				item.source = video.streams

				realItem = youtubeItemWidget.YoutubeItem(parent=self)
				#print realItem.parent
				realItem.setThumbnail(video.thumb)
				realItem.setTitle(video.title)
				realItem.setView(video.viewcount)
				realItem.setLength(video.duration)
				realItem.setAuthor(video.username)

				action = QAction('ok', self)
				realItem.setContextMenuPolicy(Qt.ActionsContextMenu)
				realItem.addAction(action)
				self.video_list.addItem(item)
				self.video_list.setItemWidget(item, realItem)

	def clearListWidget(self, listwidget):
		while listwidget.count() > 0:
			listwidget.takeItem(0)  # handle the item if you don't have a pointer to it elsewhere

	@pyqtSignature("")
	def on_search_btn_clicked(self):
		self.search()

	@pyqtSignature("")
	def on_search_box_returnPressed(self):
		self.search()

	@pyqtSignature("QListWidgetItem*")
	def on_video_list_itemDoubleClicked(self, item):
		for s in item.source:  # get url stream video
			if s.resolution == '640x360':
				url = s.url
		print url
		print self.video
		if self.videoDockWidget.isHidden():
			self.videoDockWidget.show()
		self.video.changeUrl(url)
		self.video.playClicked()

if __name__ == '__main__':
	#print getYoutubeVideoBySearchQuery(u'sungha jung', 5,'video')
	app = QApplication(sys.argv)
	main_window = MainWindow()
	main_window.resize(400, 360)
	main_window.show()
	app.exec_()
