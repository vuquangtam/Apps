# -*- coding: utf-8 -*-
# Author : Tam Vu Quang
# Description:
#  a GUI wrapper of Youtube download
#  using pafy module, which can get metadata and download youtube
#  from video url or playlist url
#  This code uses thread and callback technique (which is new to me)

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.progressbar import ProgressBar
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
import pafy, requests, bs4, json
import threading, os, sys, subprocess, gc

#from guppy import hpy; h=hpy()
import pprint

def resource_path(relative):
	'''fix pyinstaller error path of cacert.pem(requests certificate)'''
	return os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")),
						relative)

cert_path = resource_path('cacert.pem')  # request certificate path

threading.Thread.daemon = True  # doesn't wait thread finish

class SETTINGS():
	'''All Settings'''
	PLAYER = 'MPC'
	PLAYER_PATH = r'C:\Program Files\K-Lite Codec Pack\MPC-HC\mpc-hc.exe'
	SAVE_PATH = os.getcwd()  # path to store downloaded files
	MAX_VIDEO_DISPLAY = 5
	VIDEO_PLAYING_QUALITY = '640x360'

class MyButton(Button):
	pass

class YoutubeDisplayLayout(BoxLayout):
	''' layout display the infomation of video'''
	def __init__(self, title='', duration='', author='', view_count='',
				 thumbnail='', source_videos=None, source_audios=None, **kwargs):
		super(YoutubeDisplayLayout, self).__init__(**kwargs)
		self.source_videos = source_videos  # contain all source pafy video
		self.source_audios = source_audios  # contain all source pafy audio
		self.title = Label(text=title)
		self.duration = Label(text=u'Độ Dài : ' + str(duration))
		self.author = Label(text=u'Người Đăng : ' + author)
		self.view_count = Label(text=u'Lượt Xem : ' + str(view_count))

		other_info_box = BoxLayout()
		other_info_box.add_widget(self.duration)
		other_info_box.add_widget(self.author)
		other_info_box.add_widget(self.view_count)

		info_box = BoxLayout(orientation='vertical')
		info_box.add_widget(self.title)
		info_box.add_widget(other_info_box)

		self.thumbnail = AsyncImage(source=thumbnail, size_hint=(.2, 1))
		self.add_widget(self.thumbnail)
		self.add_widget(info_box)

		self.register_event_type('on_click')  # register an event for the layout
		self.register_event_type('on_db_click')  # register an event for the layout

		with self.canvas.before:  # define the selection animation
			self.color = Color(rgba=(0, 0, 0, 0))
			self.rect = Rectangle(size=self.size, pos=self.pos)
		self.bind(pos=self.updateRect, size=self.updateRect)

	def select(self):
		self.unselectAll
		self.color.rgba = (1, 0, 0, .2)

	def unselect(self):
		self.color.rgba = (0, 0, 0, 0)

	def unselectAll(self):  # unselect all the layout in video box
		for child in self.parent.children:
			child.unselect()

	def updateRect(self, *args):  # bind rect to self
		self.rect.pos = self.pos
		self.rect.size = self.size

	def on_click(self):  # an event is registered
		pass

	def on_db_click(self):
		pass

	def on_touch_down(self, touch):  # define for the on_click event
		if self.collide_point(*touch.pos):
			if touch.is_double_tap:
				self.dispatch('on_db_click')
			else:
				self.dispatch('on_click')
			return True
		return super(YoutubeDisplayLayout, self).on_touch_down(touch)

	def getTitle(self):  # implicit method
		return self.title.text

	def setTitle(self, value):  # implicit method
		self.title.text = value

class YoutubeInfoDownload(BoxLayout):
	'''layout display all infomation about download progression'''
	def __init__(self, **kwargs):
		super(YoutubeInfoDownload, self).__init__(**kwargs)
		self.padding = 5
		self.name = Label()
		self.progress_status_lbl = Label()
		self.progress_bar = ProgressBar(max=100)
		self.delete_button = MyButton(text='Xóa', size_hint=(.5, 1))
		download_box = BoxLayout(orientation='vertical')
		download_box.add_widget(self.name)
		download_box.add_widget(self.progress_status_lbl)
		download_box.add_widget(self.progress_bar)
		self.add_widget(download_box)
		self.add_widget(self.delete_button)

	def setFontSize(self, size):  # implicit method
		self.name.font_size = size
		self.progress_status_lbl.font_size = size

	def setName(self, name=''):  # implicit method
		self.name.text = name

	def setProgressStatus(self, progress_status=''):  # implicit method
		self.progress_status_lbl.text = progress_status

	def setProgressPercent(self, progress_percent=''):  # implicit method
		self.progress_bar.value = progress_percent

	def setDeleteButtonCallback(self, func):  # implicit method
		self.delete_button.bind(on_release=func)

class ChangeNameBar(BoxLayout):
	'''for word processing, change name ....'''
	def __init__(self, **kwargs):
		super(ChangeNameBar, self).__init__(**kwargs)
		self.input = TextInput()
		to_ascii_btn = MyButton(text='Không Dấu', font_size=14)
		to_ascii_btn.bind(on_release=self.toAscii)
		to_upper_btn = MyButton(text='Chữ Hoa', font_size=14)
		to_upper_btn.bind(on_release=self.toUpper)
		to_lower_btn = MyButton(text='Chữ Thường', font_size=14)
		to_lower_btn.bind(on_release=self.toLower)
		to_title_form_btn = MyButton(text='Chữ Đầu In Hoa', font_size=14)
		to_title_form_btn.bind(on_release=self.toTitleForm)
		button_box = GridLayout(cols=2, size_hint=(.4, 1))
		button_box.add_widget(to_ascii_btn)
		button_box.add_widget(to_title_form_btn)
		button_box.add_widget(to_upper_btn)
		button_box.add_widget(to_lower_btn)
		self.add_widget(self.input)
		self.add_widget(button_box)

	def setText(self, value):  # implicit method
		self.input.text = value

	def getText(self):  # implicit method
		return self.input.text

	def setInputTextCallback(self, func):  # implicit method
		self.input.bind(text=func)

	def toAscii(self, *args):
		'''from vietnamese char to ascci char'''
		translateDict = {'ă ắ ằ ẳ ẵ ặ â ấ ầ ẳ ẵ ặ á à ả ã ạ': 'a',
						 'é è ẻ ẽ ẹ ê ế ề ể ễ ệ': 'e',
						 'í ì ỉ ĩ ị': 'i',
						 'ó ò ỏ õ ọ ô ố ồ ổ ỗ ộ ơ ớ ờ ở ỡ ợ': 'o',
						 'ú ù ủ ũ ụ ư ứ ừ ử ữ ự': 'u',
						 'ý ỳ ỷ ỹ ỵ': 'y'}
		for set_of_char in translateDict:
			for char in set_of_char.split(' '):
				if char in self.input.text:
					self.input.text = self.input.text.replace(char, translateDict[set_of_char])

	def toUpper(self, *args):
		self.input.text = self.input.text.upper()

	def toLower(self, *args):
		self.input.text = self.input.text.lower()

	def toTitleForm(self, *args):
		self.input.text = self.input.text.title()

# class InputPopup(Popup):
# 	'''a popup with the ok button'''
# 	def __init__(self, **kwargs):
# 		super(InputPopup, self).__init__(**kwargs)
# 		box = BoxLayout(orientation='vertical')
# 		self.text_input = TextInput()
# 		self.submit_btn = Button(text='OK')
# 		self.submit_btn.bind(on_release=self.dismiss)
# 		box.add_widget(self.text_input)
# 		box.add_widget(self.submit_btn)
# 		self.content = box

# 	def getText(self):
# 		return self.text_input.text

# 	def setText(self, text):
# 		self.text_input.text = text


class Root(BoxLayout):
	'''main layout'''
	def __init__(self, **kwargs):
		super(Root, self).__init__(**kwargs)
		self.cur_youtube_obj = None  # to store the current download object for display download and blabla
		self.text_input = self.ids['_text_input']  # input url
		self.text_input.bind(text=self.onChangeLink)
		self.change_video_name_input = self.ids['_change_video_name_input']  # the change name bar
		self.change_video_name_input.setInputTextCallback(self.onChangeName)
		self.status_lbl = self.ids['_status_lbl']  # the status label
		self.all_videos_box = self.ids['_all_videos_box']  # box contain all YoutubeDisplayLayout obj
		self.audio_download_box = self.ids['_audio_download_box']  # the box contain all audio download button
		self.video_download_box = self.ids['_video_download_box']  # the box contain all video download button
		self.queue_download_box = self.ids['_queue_download_box']  # the box contain all download process
		self.all_thread_download = {}  # list to detect which data belongs to which thread... blabla
		self.lock = threading.Lock()  # mutex thread

	def onChangeLink(self, obj, val):
		'''display the number of link in the url to the status label'''
		count = 0
		for link in val.split('\n'):
			if link:
				count += 1
		if count:
			self.status_lbl.text = 'Số Link Video : %s' % count
		else:
			self.status_lbl.text = 'Nhập Link Youtube Vào Ô Bên Dưới'

	def onChangeName(self, obj, val):
		'''bind the text in current select download object(YoutubeDisplayLayout) to the text in the change name bar '''
		if self.cur_youtube_obj:
			self.cur_youtube_obj.setTitle(val)

	def pasteClipboard(self):
		self.text_input.paste()
		self.text_input.text += '\n'

	def clearAll(self):
		'''clear all box and input'''
		self.text_input.text = ''
		self.change_video_name_input.setText('')
		self.cur_youtube_obj = None
		self.all_videos_box.clear_widgets()
		self.audio_download_box.clear_widgets()
		self.video_download_box.clear_widgets()
		gc.collect()

	def getLink(self):
		'''get link bind to the button'''
		with self.lock:
			self.all_videos_box.clear_widgets()
			gc.collect()  # garbage collection for every getLink request
			#print len(threading.enumerate())
			#print h.heap()
			threading.Thread(target=self.getYoutubeObjectThread,
								args=(self.text_input.text, self.getLinkCallback)
							).start()  # call thread to prevent block when getting data

	def getYoutubeObjectThread(self, url, callback):
		'''Main function to get data'''
		#url = "https://www.youtube.com/watch?v=JOX-krmWf8Q"
		try:
			url = url.strip()
			if url:
				self.status_lbl.text = u'Đang Lấy Dữ Liệu (0%)...'
				all_videos = []

				if 'watch?v' in url.lower() or 'playlist?list' in url.lower():  # if url is video(playlist) youtube links
					all_videos = self.getYoutubeVideo(url)
				elif url.lower().startswith('u:'):  # if url is keyword search for user
					url = url.lstrip('u:')
					all_videos = self.getYoutubeVideoBySearchQuery(url, SETTINGS.MAX_VIDEO_DISPLAY, 'user')
				elif 'watch?v' not in url.lower():  # if url is keyword search for video
					all_videos = self.getYoutubeVideoBySearchQuery(url, SETTINGS.MAX_VIDEO_DISPLAY, 'video')
				else:  # if url is other youtube link
					all_videos = self.getYoutubeVideoBySearchQuery(url, SETTINGS.MAX_VIDEO_DISPLAY)
				self.status_lbl.text = u'Đang Lấy Dữ Liệu (50%)...'
				print url
			else:
				return
			if callback:
				callback(all_videos)
				self.status_lbl.text = u'Xong'
		except:
			pprint.pprint (sys.exc_info())
			self.status_lbl.text = u'Lỗi...'

	def getAjaxVideoData(self, url):
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

	def getYoutubeVideoBySearchQuery(self, url, max_videos, mode=None):
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
				video_urls, link = self.getAjaxVideoData(link)
				all_links += video_urls

		return self.getYoutubeVideo('\n'.join(all_links))

	def getYoutubeVideo(self, url):
		'''get data from video urls
			url format : 'link' or 'link\nlink\nlink blabla'
		'''
		all_videos = []
		for link in url.split('\n'):
			if 'playlist?list' in link.lower():
				all_videos += self.getYoutubePlaylist(link)
			elif 'watch?v' in link.lower():
				video = pafy.new(link)
				all_videos.append(video)
			else:
				continue
		return all_videos

	def getYoutubePlaylist(self, plurl):
		'''get data from playlist url'''
		all_videos = []
		playlist = pafy.get_playlist(plurl)
		for video in playlist['items']:
			all_videos.append(video['pafy'])
		return all_videos

	def getLinkCallback(self, all_videos):
		'''Adding YoutubeDisplayLayouts to the all_videos_box'''
		for video in all_videos:  # assign the source_videos, sources audio to use later
			obj = YoutubeDisplayLayout(title=video.title, duration=video.duration,
										thumbnail=video.thumb, view_count=video.viewcount,
										author=video.username if len(video.username) < 20 else video.username[:20] + '...',
										source_videos=video.streams, source_audios=video.audiostreams)
			obj.bind(on_click=self.showDownload)  # when click, show all available video and audio download button
			obj.bind(on_db_click=self.openVideo)  # double click to play video
			self.all_videos_box.add_widget(obj)
		#tracker.print_diff()

	def openVideo(self, obj):
		url = ''
		args = ()
		for s in obj.source_videos:  # get url stream video
			if s.resolution == SETTINGS.VIDEO_PLAYING_QUALITY:
				url = s.url
				break
		if SETTINGS.PLAYER == 'MPC':  # because MPC and VLC has different call
			url = '"' + s.url + '"'  # put in "" to prevent escape value
			args = ([SETTINGS.PLAYER_PATH, url], )
		else:
			args = ([SETTINGS.PLAYER_PATH, '--play-and-stop', url], )
		threading.Thread(target=subprocess.call, args=args).start()  # run in thread so it wont block main process

	def showDownload(self, obj):
		'''show all available download button of video object'''
		gc.collect()
		self.cur_youtube_obj = obj  # store in self to use later
		self.cur_youtube_obj.unselectAll()  # select animation
		self.cur_youtube_obj.select()
		self.status_lbl.text = obj.getTitle()  # set the status label
		self.video_download_box.clear_widgets()
		self.audio_download_box.clear_widgets()
		gc.collect()
		for s in obj.source_videos:  # add download button to video download box
			b = MyButton(text=s.resolution + '\n' + s.extension)
			b.halign = 'center'
			b.valign = 'middle'
			b.font_size = 12
			b.stream = s  # stream to use later
			b.video_pafy_obj = obj  # video obj to use later
			b.bind(on_release=self.download)  # when click, implement download process
			self.video_download_box.add_widget(b)
		for s in obj.source_audios:  # add download button to audio download box
			b = MyButton(text=s.quality + '\n' + s.extension)
			b.halign = 'center'
			b.valign = 'middle'
			b.font_size = 12
			b.stream = s   # stream to use later
			b.video_pafy_obj = obj  # video obj to use later
			b.bind(on_release=self.download)  # when click, implement download process
			self.audio_download_box.add_widget(b)
		self.change_video_name_input.setText(obj.getTitle())  # set the change name bar (user friendly)

	def downloadAll(self, kind, quality):
		'''download all video or audio have defined kind and quality'''
		for video_obj in self.all_videos_box.children[::-1]:  # iterate all YoutubeDisplayLayout object to download
			stream = None
			if kind == 'video':
				streams = video_obj.source_videos
			elif kind == 'audio':
				streams = video_obj.source_audios
			else:
				return
			for s in streams:
				if s.quality == quality:  # in pafy, the quality of audio is always 0x0
					stream = s
				elif s.bitrate == quality:  # in pafy, the bitrate of video is always None
					stream = s
			title = video_obj.getTitle()  # getTitle for naming the path to store, and display the name of download widget
			threading.Thread(target=self.downloadThread, args=(stream, title)).start()  # start thread to prevent blocking

	def download(self, obj):
		'''download one video'''
		stream = obj.stream
		filename = obj.video_pafy_obj.getTitle().decode('utf-8')  # decode to prevent unicode error (try it and fix it)
		threading.Thread(target=self.downloadThread, args=(stream, filename)).start()

	def stripStringToWindowsFormat(self, string):
		for char in ': / \ : * ? " < > | '.split(' '):
			if char in string:
				string = string.replace(char, '')
		return string

	def downloadThread(self, stream, filename):
		'''function define the download (which is called in thread by download and downloadAll)'''
		with self.lock:  # because downloadAll call continously in loop, so need to be mutex
			filepath = SETTINGS.SAVE_PATH + os.sep + self.stripStringToWindowsFormat(filename) + '.' + stream.extension
			id = threading.current_thread().ident  # id for identity the thread for store in self to use later (in downloadCallback)
			download_info_btn = YoutubeInfoDownload()
			download_info_btn.setName(filename[:6] + '...' + filename[-6:])
			download_info_btn.setFontSize(12)
			self.all_thread_download[id] = [False, download_info_btn]
			# the first is END thread boolean, 2nd is button to downloadCallback change the info
			# you can't call the sys.exit in the callback of download_info_btn
			# because download_info_btn belongs to the another thread, it fire the callback
			# in the another control widget thread, if you call, it will crash the GUI and don't
			# close the current download thread

			def callback(*arg):
				self.all_thread_download[id][0] = True
				self.queue_download_box.remove_widget(download_info_btn)
			download_info_btn.setDeleteButtonCallback(callback)  # the implicit method to set the callback to the delete button
			self.queue_download_box.add_widget(download_info_btn)  # display it in the box
		try:
			stream.download(filepath=filepath,
								quiet=True, callback=self.downloadCallback)
			self.queue_download_box.remove_widget(download_info_btn)  # when finish, clean it
		except:
			download_info_btn.setProgressStatus('Lỗi')  # display error and dont remove (user friendly)

	def downloadCallback(self, *args):
		download_info_btn = self.all_thread_download[threading.current_thread().ident][1]
		# dont mutex because this item is only accessed by this thread (by thread id)
		# (in the same list, but it is seperate item, and it is immutable, dont need to mutex at all)
		if self.all_thread_download[threading.current_thread().ident][0]:
			sys.exit()
		percent = int(args[2] * 100)
		total_size = args[0]/(1024.0*1024)
		cur_size = args[1]/(1024.0*1024)
		progress_mbyte = '%.2fMB/%.2fMB' % (cur_size, total_size)
		download_info_btn.setProgressStatus(progress_mbyte)  # that why you must store the button in self
		download_info_btn.setProgressPercent(percent)

class YoutubeDownloaderApp(App):
	'''
		first : build_config
		then : build
		build_settings : call when first go to settings
	'''
	def build(self):
		for key in SETTINGS.__dict__:  # init all the value in the SETTINGS class from config file
			if not key.startswith('__'):  # tricky naming : variable and config key has same name so use for to assign
				value = self.config.get("Path", key)
				SETTINGS.__dict__[key] = value
		Window.size = (1024, 500)
		self.icon = 'youtube.ico'
		self.title = 'Youtube Downloader'
		self.root_layout = Root()
		return self.root_layout

	def build_config(self, config):
		config_dict = {}
		for key in SETTINGS.__dict__:
			if not key.startswith('__'):
				config_dict[key] = SETTINGS.__dict__[key]
		config.setdefaults('Path', config_dict)

	def build_settings(self, settings):
		# in json data, quote must be "", '' will raise an error
		settings.add_json_panel("Youtube Downloader Settings", self.config, data="""
		[
			{
				"type": "title",
				"title": "Video"
			},
			{
				"type": "options",
				"title": "Công Cụ Phát Video",
				"section": "Path",
				"options": ["MPC", "VLC"],
				"key": "PLAYER"
			},
			{
				"type": "string",
				"title": "Đường Dẫn Công Cụ Phát Video",
				"section": "Path",
				"key": "PLAYER_PATH"
			},
			{
				"type": "options",
				"title": "Chất Lượng Hiển Thị Video",
				"section": "Path",
				"options": ["320x240", "640x360", "1280x720"],
				"key": "VIDEO_PLAYING_QUALITY"
			},
			{
				"type": "options",
				"title": "Video Hiển Thị Tối Đa Khi Tìm Kiếm Bằng Từ Khóa",
				"section": "Path",
				"options": ["5", "10", "15", "20", "Tất Cả"],
				"key": "MAX_VIDEO_DISPLAY"
			},
			{
				"type": "title",
				"title": "Tải Xuống"
			},
			{
				"type": "string",
				"title": "Đường Dẫn Nơi Lưu Video",
				"section": "Path",
				"key": "SAVE_PATH"
			}
		]"""
		)

	def on_config_change(self, config, section, key, value):
		if config is self.config:
			if key == "SAVE_PATH":
				if os.path.isdir(value):  # check for exists
					SETTINGS.SAVE_PATH = value
				else:
					self.root_layout.status_lbl.text = 'Đường Dẫn Nơi Lưu Video Không Hợp Lệ'
			elif key == "PLAYER_PATH":
				if os.path.isfile(value):  # check for exists
					SETTINGS.PLAYER_PATH = value
				else:
					self.root_layout.status_lbl.text = 'Đường Dẫn MPC/VLC Không Hợp Lệ'
			elif key == "MAX_VIDEO_DISPLAY":
					SETTINGS.MAX_VIDEO_DISPLAY = value
			elif key == "VIDEO_PLAYING_QUALITY":
				SETTINGS.VIDEO_PLAYING_QUALITY = value
			elif key == "PLAYER":
				SETTINGS.PLAYER = value

if __name__ == '__main__':
	YoutubeDownloaderApp().run()
