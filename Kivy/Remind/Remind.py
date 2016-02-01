#!/usr/bin/python
# -*- coding: utf8 -*-

# Name    : CalDate.py
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

# Import Self-Coding
import CalendarScreen, NumOfDayScreen, CalDate, PictureGalleryScreen

Builder.load_string('''
<RemindScreen>:
	BoxLayout:
		canvas:
			Rectangle:
				pos: self.pos
				size: self.size
				source: 'Image/MainScreen//Background/background.jpg'
		RelativeLayout:
			AnchorLayout:
				anchor_x: 'left'
				anchor_y: 'top'
				Image:
					source: 'Image/MainScreen/3dLogo/Heart.zip'
					anim_delay: .015
					size_hint: .2,.2
		BoxLayout:
			size_hint: .4, 1
			orientation: 'vertical'
			Button:
				id: today_btn
				font_size: 15
				markup: True
				background_normal: 'Image/MainScreen/Button/buttonBG.png'
				valign: 'middle'
				halign: 'center'
				on_release: root.switchCalendarScreen()
			Button:
				id: dayOfLove_btn
				font_size: 15
				markup: True
				background_normal: 'Image/MainScreen/Button/buttonBG.png'
				valign: 'middle'
				halign: 'center'
				on_release: root.switchNumOfDayScreen()
			Button:
				id: remindDay_btn
				font_size: 15
				markup: True
				background_normal: 'Image/MainScreen/Button/buttonBG.png'
				valign: 'middle'
				halign: 'center'
				on_release: root.switchPictureGalleryScreen()
''')

class RemindScreen(Screen):
	def __init__(self, **kwargs):
		super(RemindScreen, self).__init__(**kwargs)
		self.today = self.ids['today_btn']
		self.dayOfLove = self.ids['dayOfLove_btn']
		self.remindDay = self.ids['remindDay_btn']
		self.day = CalDate.Day()
		self.today.text = '[color=f629e5][b]Hôm Nay Là %s' % self.day.today.strftime("%d/%m/%Y") + '[/b][/color]'
		self.dayOfLove.text = '[color=18b707][b]%s Ngày\n\n(Press To See Full Information)' % (self.day.numOfDay.days) + '[/b][/color]'
		self.remindDay.text = '[color=ff0000][b]Hôm Nay Là Ngày Đặc Biệt' if self.day.remind() else \
								'[color=ff0000][b]Còn %s Ngày Nữa -> Ngày Đặc Biệt' % self.day.dayLeft()  + '[/b][/color]'

	def switchNumOfDayScreen(self):
		if not hasattr(self, 'NumOfDayScreen'):
			self.NumOfDayScreen = NumOfDayScreen.NumOfDayScreen(name='NumOfDayScreen', sm=sm, mainScreen='RemindScreen')
			sm.add_widget(self.NumOfDayScreen)
		self.NumOfDayScreen.inform = self.day.yearOfLove()
		sm.current = 'NumOfDayScreen'

	def switchCalendarScreen(self):
		if not hasattr(self, 'CalendarScreen'):
			self.CalendarScreen = CalendarScreen.CalendarScreen(name='CalendarScreen', sm=sm, mainScreen='RemindScreen')
			sm.add_widget(self.CalendarScreen)
		sm.current = 'CalendarScreen'

	def switchPictureGalleryScreen(self):
		if not hasattr(self, 'PictureGalleryScreen'):
			self.PictureGalleryScreen = PictureGalleryScreen.PictureGalleryScreen(name='PictureGalleryScreen', sm=sm, mainScreen='RemindScreen')
			sm.add_widget(self.PictureGalleryScreen)
		sm.current = 'PictureGalleryScreen'

class RemindApp(App):
	def build(self):
		Window.size = (1024, 600)
		return sm

sm = ScreenManager()
sm.add_widget(RemindScreen(name='RemindScreen'))

if __name__ == '__main__':
	RemindApp(title='Remind').run()
