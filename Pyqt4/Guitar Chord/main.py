# -*- coding: utf-8 -*-

# >>EXPERIMENT<<
# SPECIAL NOTE: REQUESTS MODULE AUTOMATICALLY CONVERT RESPONE TO UTF-8.
# if response is UTF-8: requests will not encode the content. Ex: Xin Chào
# if response is not UTF-8 (ISO-8859-1...): requests will encode to UTF-8. Ex: Xin ChÃ o
#
# decode -> decode a unicode to str (to write in file....)
# encode -> encode a str(escape character) to unicode(the real character)
# to convert "the escape character" in unicode to "the real character" in unicode
# first : convert "the escape character" in unicode to "the escape character" in str
# then : convert normally (use decode('utf-8'))
# because : unicode.decode('utf-8') implicit cast the unicode to str for decoding like this:
# unicode.decode('utf-8') ~ str(unicode).decode('utf-8')
# Ex: lyric.getText().encode('raw_unicode_escape').decode('utf-8')
# Note : decode method is from unicode to str, not str to str
#        Ex: "Xin Chào".encode('utf-8') ~ "Xin Chào".decode().encode('utf-8') (convert str to unicode first)
#        encode method is from str to unicode, not unicode to unicode
# Source : http://stackoverflow.com/questions/1207457/convert-a-unicode-string-to-a-string-in-python-containing-extra-symbols
#          https://stackoverflow.com/questions/4267019/double-decoding-unicode-in-python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_chord
import qrc_resources
import sys
import os
import re
import requests
import bs4
import threading
import gc

def resource_path(relative):
	'''fix pyinstaller error path of cacert.pem(requests certificate)'''
	return os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")),
						relative)

cert_path = resource_path('cacert.pem')  # request certificate path

threading.Thread.daemon = True  # doesn't wait thread finish

CHORD_SOURCES = {'hopam.vn': {'url': r'http://hopam.vn/?s=%s&post_type=post',
								'song_list_select': '.entry a',
								'lyric_select': '.tb_ct',
							 },
				'hopamchuan.com': {'url': r'http://hopamchuan.com/search?q=%s',
								'song_list_select': '.search_result h2 a',
								'lyric_select': 'div#song_text pre',
								  },
				'hopamviet.com': {'url': r'http://hopamviet.com/chord/search.html?song=%s',
								'song_list_select': r'a[href*="chord/song"]',
								'lyric_select': 'div#lyric',
								  },
				}
# CHORD_SOURCES DATA STRUCTURE:
# SITE : (URL, SONG_LIST_SELECT, LYRIC_SELECT)
# URL : URL TO REQUEST SEARCH QUERY
# SONG_LIST_SELECT : A CSS SELECT TO FILTER ALL THE SONG IN SEARCH QUERY RESPONSE
# LYRIC_SELECT : A CSS SELECT TO FILTER THE LYRIC IN THE LYRIC PAGE

CHORD_LIST = 'G G# A A# B C C# D D# E F F#'.split(' ')
# CHORD_LIST TO TRANPOSE TONE
ENHARMONIC_LIST = {'Bb': 'A#', 'Db': 'C#', 'Eb': 'D#', 'Gb': 'F#', 'Ab': 'G#'}
# ENHARMONIC CHORD TO TRANPOSE TONE

def findAllChord(lyric):
	'''regex to filter all the chord with the structure : [chord] in the lyric'''
	reg_obj = re.compile(r'\[.+?\]')
	results = reg_obj.findall(lyric)
	all_chord = list(set(results))
	return all_chord

def easyChord(lyric):
	'''strip sus, dim, number chord'''
	all_chord = findAllChord(lyric)
	easy_chord_reg_obj = re.compile(r'(sus|dim|\d)')
	for chord in all_chord:
		new_chord = easy_chord_reg_obj.sub('', chord)
		lyric = lyric.replace(chord, new_chord)
	return lyric

def changeTone(chord, accidental):
	'''change tone b or #, the structure of the chord is [chord],
		only change the base chord.
		ex: Bmsus7 => only change B. Amsus7 blabla
	'''
	if accidental == 'b':
		sign = -1
	else:
		sign = 1
	flat_sharp = chord[2]  # b or #
	if flat_sharp.lower() in ['#', 'b']:
		base = chord[1:3]  # if flat or sharp, the chord is 2 char
	else:
		base = chord[1]
	if base not in CHORD_LIST:  # CHORD_LIST only contain sharp and nature, so if chord is flat => convert to sharp, if not, the index error will be raised
		new_base = CHORD_LIST[(CHORD_LIST.index(ENHARMONIC_LIST[base]) + sign) % len(CHORD_LIST)]
	else:
		new_base = CHORD_LIST[(CHORD_LIST.index(base) + sign) % len(CHORD_LIST)]
	chord = chord.replace(base, new_base)  # only replace the base
	return chord

def changeToneLyric(lyric, accidental):
	'''change all chord in lyric.
		adding the chunk '@@@@' to not replace together in loop
		ex: B C D E => C D E F in the lyric : E E D B C
		first it replace B to C, the lyric is E E D C C
		second it replace C to D, the lyric is E E D D(conflict in this, this must be C) D
	'''
	all_chord = findAllChord(lyric)
	for chord in all_chord:
		new_chord = changeTone(chord, accidental)
		new_strange_chord = new_chord[:2] + '@@@@' + new_chord[2:]
		lyric = lyric.replace(chord, new_strange_chord)
	return lyric.replace('@@@@', '')

def safeUnicodeDecode(str):  # for HopAmChuan, HopAmViet
	'''because the requests module, see the beginning of the file'''
	return str.encode('raw_unicode_escape').decode('utf-8')

def filterChordWithBracket(lyric):  # for HopAmChuan
	'''change <span>chord</span> element to [chord]'''
	reg_obj = re.compile(r'<span .*?>(.*?)</span>')
	new_lyric = reg_obj.sub(r'[\1]', lyric)  # \1 is the alias of group 1 in regex (.*?)
	return new_lyric

def boldTheChord(lyric):
	'''bold the chord with red color.
		because we use html, so \r\n must convert to <br>, and space must escape blabla
		we don't convert \r\n and space here because we use <pre> tag
	'''
	reg_bold_chord = re.compile(r'(\[.*?\])')
	new_lyric = reg_bold_chord.sub(r'<font color="red">\1</font>', lyric)
	return new_lyric

def getLyric(url, source, decode=False):
	'''get lyric(chord) from the url'''
	try:
		req = requests.get(url, verify=cert_path)
		req.raise_for_status()
		data = req.text
		if decode:  # decode for hopamchuan and hopamviet because they dont use UTF-8 encoding
			data = safeUnicodeDecode(req.text)
		soup = bs4.BeautifulSoup(data, "html.parser")
		select = CHORD_SOURCES[source]['lyric_select']
		lyric_temp = soup.select(select)
		lyric_tag = lyric_temp[0]
		if source == 'hopamchuan.com':  # hopamchuan chord not in form [chord], so convert to this form
			lyric = filterChordWithBracket(unicode(lyric_tag)).strip(r'<pre>').strip(r'</pre>')  # the response have pre tag, so strip it
		else:
			lyric = lyric_tag.getText()  # getText return the plain text from html (strip all tag)
		return boldTheChord(lyric.strip())
	except:
		return False

def getSearchResult(keyword, source, decode=False):
	'''get songs from keyword'''
	try:
		url = CHORD_SOURCES[source]['url'] % keyword
		req = requests.get(url, verify=cert_path)
		req.raise_for_status()
		#print req.encoding
		data = req.text
		if decode:
			data = safeUnicodeDecode(req.text)
		soup = bs4.BeautifulSoup(data, "html.parser")
		select = CHORD_SOURCES[source]['song_list_select']
		html_results = soup.select(select)
		results = []
		for result in html_results:
			name = result.getText().strip()
			url = result.get('href')
			results.append([name, url])  # return name and url to the lyric page of all songs
		#print url
		#print select
		return results
	except:
		return False

def saveLyric(filename, lyric):
	f = open(filename, 'w')
	try:
		lyric = lyric.encode('utf-8')  # must encode unicode to string
	except:
		pass
	f.write(lyric)
	f.close()

class MainWindow(QMainWindow, ui_chord.Ui_ChordWindow):  # use Qt Designer
	def __init__(self, **kwargs):
		super(QMainWindow, self).__init__(**kwargs)
		self.current_song = ''
		self.lock = threading.Lock()
		#  here we must use signal for all work in thread.
		#  dont change GUI in thread
		self.connect(self, SIGNAL('updateStatus'),
						lambda value, showTime=0: self.statusBar().showMessage(value, showTime))
		self.connect(self, SIGNAL('updateChordBox'), self.updateChordBoxSlot)
		self.connect(self, SIGNAL('clearChordBox'),
						lambda: self.song_list_box.clear())
		self.connect(self, SIGNAL('addSong'),
						lambda item: self.song_list_box.addItem(item))
		self.connect(self, SIGNAL('errorRequest'),
						lambda error: self.statusBar().showMessage(error, 10000))
		self.connect(self, SIGNAL('showChordDock'),
						lambda: self.chord_dock.show())
		self.setupUi(self)  # setupUI from Qt Designer file
		self.chord_box.setCurrentFont(QFont("Helvetica [Cronyx]"))

	def updateChordBoxSlot(self, value):
		'''update the chord box, add pre tag to have pretty look,
			after update, chage the font size in html return by chord_box
			we must do it instead of set font size in pre tag, because the
			html generate by chord_box is different from what we set for chord box
			Ex: we set '<pre> blabla </pre>'
				the chord box return : DOC !HTML blabla CSS blabla <pre style = 'blabla' size = 'blabla'></pre>
		'''
		self.chord_box.setText('<pre>' + value + '</pre>')
		lyric = self.changeFontSizeHTML(unicode(self.chord_box.toHtml()), int(self.font_size_box.value()))
		self.chord_box.setText(lyric)

	def searchThread(self):
		'''search in thread'''
		self.emit(SIGNAL("updateStatus"), u'Đang Tải Danh Sách Bài Hát...')
		self.emit(SIGNAL("clearChordBox"))
		keyword = unicode(self.search_box.text())  # must cast QString to unicode
		source = unicode(self.source_box.itemText(self.source_box.currentIndex()))
		decode = False
		if source in ['hopamviet.com', 'hopamchuan.com']:
			decode = True
		results = getSearchResult(keyword, source, decode)
		if results:
			for result in results:
				item = QListWidgetItem(result[0])
				item.url = result[1]
				item.source = source
				item.decode = decode
				self.emit(SIGNAL("addSong"), item)  # signal to main thread to add, not add there
			self.emit(SIGNAL("updateStatus"), u'Xong', 5000)  # show message in 5s
		else:
			self.emit(SIGNAL("errorRequest"),
						u'Không Thể Lấy Bài Hát Từ : "%s". Kiểm Tra Kết Nối Mạng Hoặc Thử Trang Khác' % source)

	def getLyricThread(self, url, source, decode):
		'''get lyric in thread'''
		self.emit(SIGNAL("updateStatus"), u'Đang Tải Lời Nhạc...')
		lyric = getLyric(url, source, decode)
		self.emit(SIGNAL("showChordDock"))
		if lyric:
			self.emit(SIGNAL("updateChordBox"), lyric)
			self.emit(SIGNAL("updateStatus"), u'Xong', 5000)
		else:
			self.emit(SIGNAL("errorRequest"),
						u'Không Thể Lấy Lời Nhạc Từ : "%s". Kiểm Tra Kết Nối Mạng Hoặc Thử Trang Khác' % source)

	@pyqtSignature("")  # because the returnPressed slot can have many overloading(has different arguments), this decorator chooses exactly slot
	def on_search_box_returnPressed(self):  # this method is set in self.setupUI() (call QtCore.blabla), to set slot in structure : on_obj_slot
		gc.collect()  # explicit call garbage collect after doing so much work
		with self.lock:
			threading.Thread(target=self.searchThread).start()

	@pyqtSignature("")
	def on_search_btn_clicked(self):
		gc.collect()
		with self.lock:
			threading.Thread(target=self.searchThread).start()

	@pyqtSignature("QListWidgetItem*")
	def on_song_list_box_itemPressed(self, item):
		'''call when click on the item in song list, show the lyric'''
		gc.collect()
		self.current_song = item.text()
		self.chord_dock.setWindowTitle(self.current_song)
		with self.lock:
			threading.Thread(target=self.getLyricThread,
								args=(item.url, item.source, item.decode)).start()

	def changeFontSizeHTML(self, content, size):
		'''tricky change font use regex, use html css attribute'''
		regex_font = re.compile(r'(font-size:.*?pt)')
		return regex_font.sub("font-size:%spt" % int(size), content)

	@pyqtSignature("double")
	def on_font_size_box_valueChanged(self, value):
		lyric = unicode(self.chord_box.toHtml())  # return the html of qtextedit
		lyric = self.changeFontSizeHTML(lyric, int(value))
		self.chord_box.setText(lyric)

	@pyqtSignature("")
	def on_flat_btn_clicked(self):
		'''tranpose b'''
		lyric = unicode(self.chord_box.toHtml())
		new_lyric = changeToneLyric(lyric, 'b')
		self.chord_box.setText(new_lyric)

	@pyqtSignature("")
	def on_sharp_btn_clicked(self):
		'''tranpose #'''
		lyric = unicode(self.chord_box.toHtml())
		new_lyric = changeToneLyric(lyric, '#')
		self.chord_box.setText(new_lyric)

	@pyqtSignature("")
	def on_easy_chord_btn_clicked(self):
		'''strip sus, dim, number chord'''
		lyric = unicode(self.chord_box.toHtml())
		new_lyric = easyChord(lyric)
		self.chord_box.setText(new_lyric)

	@pyqtSignature("")
	def on_save_btn_clicked(self):
		if not self.current_song:
			return
		filename = unicode(self.current_song)
		lyric = unicode(self.chord_box.toPlainText())  # return the plain text (strip html tag)
		filename = unicode(QFileDialog.getSaveFileName(self,
                			u"Hợp Âm - Lưu Hợp Âm", filename,
                			"Text Files (*.txt)\nAll Files (*.*)"))
		if filename:
			saveLyric(filename, lyric)
			self.emit(SIGNAL("updateStatus"), u'Đã Lưu', 5000)

if __name__ == '__main__':
#	print getLyric(r'http://hopamchuan.com/song/479/uoc-gi', 'hopamchuan.com')
#	print getSearchResult('uoc gi', 'hopam')
#	print getLyric(r'http://hopam.vn/uoc-gi-ver-3/', 'hopam')
	app = QApplication(sys.argv)
	main_window = MainWindow()
	main_window.setWindowIcon(QIcon(":/guitar.ico"))
	main_window.setWindowTitle(u'Hợp Âm')
	main_window.resize(600, 300)
	main_window.show()
	app.exec_()
