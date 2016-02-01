# -*- coding: utf8 -*-
import os
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scatterlayout import ScatterLayout
from kivy.lang import Builder
from kivy.app import App

Builder.load_string('''
#:set HEIGHT_MENU_BUTTON 200
#:set buttonBG 'Image/PictureGallery/Button/button_default.png'

<MenuButton>:
	size_hint: 1, None
	height: HEIGHT_MENU_BUTTON
	markup: True
	background_normal: buttonBG

<ScatterImage>:
	auto_bring_to_front: False
	do_rotation: False

<PictureGalleryScreen>:
	BoxLayout:
		BoxLayout:
			orientation: 'vertical'
			BoxLayout:
				id: _image_original_box
				ScatterImage:
					id: _image_scatter
					default_pos: self.parent.center
			BoxLayout:
				size_hint: 1, .1
				Button:
					size_hint: .1, 1
					markup: True
					background_normal: 'Image/PictureGallery/Button/button_rotate_left.png'
					on_release: _image_scatter.rotateLeft()
				Button:
					id: _image_name
					markup: True
					background_normal: buttonBG
					on_release: _image_scatter.setDefaultImageState()
				Button:
					size_hint: .1, 1
					markup: True
					background_normal: 'Image/PictureGallery/Button/button_rotate_right.png'
					on_release: _image_scatter.rotateRight()
		BoxLayout:
			size_hint: .3, 1
			orientation: 'vertical'
			canvas:
				Color:
					rgb: .1, .5, .5
				Rectangle:
					pos: self.pos
					size: self.size
			ScrollView:
				do_scroll_x: False
				BoxLayout:
					id: _menu
					orientation: 'vertical'
					size_hint: 1, None
					height: len(self.children) * HEIGHT_MENU_BUTTON
			Button:
				size_hint: 1, .1
				text: '[color=00ff00][b]Back[/b][/color]'
				markup: True
				background_normal: buttonBG
				on_release: root.back()
''')

PICTURE_DIR = os.getcwd() + os.sep + 'Image/PictureGallery/Gallery'
PICTURE_EXT = 'png jpeg jpg bmp gif'.split()
# PICTURE NAME MUST BE MM-YYYY.EXT

class MenuButton(Button):
	pass

class ScatterImage(ScatterLayout):
	def __init__(self, **kwargs):
		super(ScatterImage, self).__init__(**kwargs)
		self.default_pos = ()
		self.image_frame = Image()
		self.add_widget(self.image_frame)

	def setDefaultImagePos(self):
		'''Set Default Pos for Scatter Image'''
		self.center = self.default_pos

	def setDefaultImageState(self):
		'''Set Default State for Scatter Image'''
		self.rotation = 0
		self.scale = 1.0
		self.setDefaultImagePos()

	def rotateRight(self):
		self.rotation -= 90.0
		self.setDefaultImagePos()

	def rotateLeft(self):
		self.rotation += 90.0
		self.setDefaultImagePos()

class PictureGalleryScreen(Screen):
	def __init__(self, **kwargs):
		super(PictureGalleryScreen, self).__init__(**kwargs)
		self.sm = kwargs['sm']  # sm to back to mainScreen
		self.mainScreen = kwargs['mainScreen']  # mainScreen
		self.menu = self.ids['_menu']
		self.image_name = self.ids['_image_name']
		self.image_scatter = self.ids['_image_scatter']
		self.loadPictureMenu()

	def loadPictureMenu(self):
		'''Load Dir and Add Button to Menu'''
		last_dir = ''
		self.menu.clear_widgets()
		for dir in self.sortListDir():
			splitname = os.path.splitext(dir)
			if splitname[1].strip('.').lower() not in PICTURE_EXT:
				continue
			button_temp = MenuButton(text=splitname[0])
			button_temp.ext = splitname[1]
			button_temp.bind(on_release=self.loadPicture)
			self.menu.add_widget(button_temp)
			last_dir = dir
		self.image_name.text = '[color=ff0000][b]%s[/b][/color]' % os.path.splitext(last_dir)[0]
		self.image_scatter.image_frame.source = PICTURE_DIR + os.sep + last_dir

	def sortListDir(self, dir_list=os.listdir(PICTURE_DIR)):
		'''Sorting dir by comp function'''
		sorted_dir = []

		def comp(A, B):
			'''compare two day : MM-YYYY , if A > B return true'''
			A = os.path.splitext(A)[0]
			B = os.path.splitext(B)[0]
			monthA, yearA = [int(i) for i in A.split('-')]
			monthB, yearB = [int(i) for i in B.split('-')]
			if yearA > yearB:
				return 1
			elif yearB > yearA:
				return -1
			elif monthA > monthB:
				return 1
			else:
				return -1

		return sorted(dir_list, cmp=comp)

	def loadPicture(self, obj):
		'''Load Image into Frame'''
		dir = PICTURE_DIR + os.sep + obj.text + obj.ext
		self.image_name.text = '[color=00ff00][b]%s[/b][/color]' % obj.text
		self.image_scatter.image_frame.source = dir

	def back(self):
		self.sm.current = self.mainScreen

if __name__ == '__main__':
	sm = ScreenManager()
	pictureGalleryScreen = PictureGalleryScreen(name='PictureGalleryScreen', sm=sm, mainScreen='PictureGalleryScreen')
	sm.add_widget(pictureGalleryScreen)

	class PictureGalleryApp(App):
		def build(self):
			return sm

	if __name__ == '__main__':
		PictureGalleryApp().run()
