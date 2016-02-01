#!/usr/bin/python
# -*- coding: utf8 -*-

# Name    : numOfDayScreen.py
# Purpose : Calculate day, include calendar, some fun stuffs !
# Author  : Tam Vu Quang
# Revision: May 2015 - initial version
#
# This program require kivy module
# http://kivy.org/
# Enjoy :)


# Kivy Import
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ListProperty

# Python Import
import os

Builder.load_string('''
<NumOfDayScreen>:
	FloatLayout:
		Image:
			id: bg_obj
			allow_stretch: True
	BoxLayout:
		orientation: 'vertical'
		BoxLayout:
			orientation: 'vertical'
			canvas:
				Color:
					rgba: 0, 0, 0, .5
				Rectangle:
					pos: self.pos
					size: self.size
			Image:
				source: 'Image/NumOfDay/3dLogo/Minion.zip'
				anim_delay: .015
			Label:
				id: inform_lbl
				font_size: 40
				valign: 'middle'
				halign: 'center'
				markup: True
			Label:
			Label:
		Button:
			id: back_btn
			size_hint: 1, .2
			text: '[color=00ff00][b]Back[/b][/color]'
			markup: True
			background_normal: 'Image/NumOfDay/Button/button_default.png'
			on_release: root.back()
''')
class NumOfDayScreen(Screen):
	inform = ListProperty()

	def __init__(self, **kwargs):
		super(NumOfDayScreen, self).__init__(**kwargs)
		self.sm = kwargs['sm']
		self.mainScreen = kwargs['mainScreen']
		self.inform_lbl = self.ids['inform_lbl']
		self.back_btn = self.ids['back_btn']
		self.bg_obj = self.ids['bg_obj']
		self.path = 'Image' + os.sep + 'NumOfDay' + os.sep + 'Background'
		self.bg_list = [self.path + os.sep + bg for bg in os.listdir(os.getcwd() + os.sep + self.path)]
		self.bg_index = 0
		self.bg_obj.source = self.bg_list[self.bg_index]

	def back(self):
		self.sm.current = self.mainScreen

	def on_inform(self, obj, value):
		value = tuple(value)
		self.inform_lbl.text = '[color=18b707][i]%s Năm %s Tháng %s Ngày[/i][/color]' % value

	def on_touch_down(self, touch):
		if touch.pos[1] > self.back_btn.height:
			self.bg_index = (self.bg_index + 1) % len(self.bg_list)
			self.bg_obj.source = self.bg_list[self.bg_index]
			return True
		return super(NumOfDayScreen, self).on_touch_down(touch)

if __name__ == '__main__':
	sm = ScreenManager()
	numOfDayScreen = NumOfDayScreen(name='NumOfDayScreen', sm=sm, mainScreen='NumOfDayScreen')
	sm.add_widget(numOfDayScreen)

	class NumOfDayScreenApp(App):
		def build(self):
			Window.size = (1024, 600)
			return sm
	NumOfDayScreenApp(title='NumOfDay Screen').run()
