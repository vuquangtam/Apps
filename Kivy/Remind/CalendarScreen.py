#!/usr/bin/python
# -*- coding: utf8 -*-

# Name    : calendarScreen.py
# Purpose : Calculate day, include calendar, some fun stuffs !
# Author  : Tam Vu Quang
# Revision: May 2015 - initial version
#
# This program require kivy module
# http://kivy.org/
#
# Put background in /Image/Calendar/Background/
# Put background of button in /Image/Calendar/Button/
#
# Enjoy :)

# Kivy Import
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window

# Python Import
import datetime, os, sys
sys.path.append(os.getcwd() + os.sep + 'Module')
import lunardate

LUNAR_EVENT = {(1, 1)  : 'Tết Nguyên Đán',
					(2, 1)  : 'Mồng 2 Tết Nguyên Đán',
					(3, 1)  : 'Mồng 3 Tết Nguyên Đán',
					(4, 1)  : 'Mồng 4 Tết Nguyên Đán',
					(15, 1) : 'Tết Nguyên tiêu',
					(10, 3) : 'Giỗ tổ Hùng Vương',
					(3, 3)  : 'Tết Hàn thực',
					(14, 4) : 'Tết Dân tộc Khmer - Lễ hội Chol Chnam Thmay',
					(15, 4) : 'Lễ Phật Đản',
					(5, 5)  : 'Tết Đoan Ngọ',
					(15, 7) : 'Lễ Vu Lan',
					(1, 8)  : 'Tết Katê',
					(15, 8) : 'Tết Trung Thu',
					(9, 9)  : 'Tết Trùng Cửu',
					(10, 10): 'Tết Trùng Thập',
					(23, 12): 'Ngày Ông Táo chầu trời'}

SOLAR_TRADITIONAL_EVENT = 	{(1, 3)  : 'Bắt Đầu Hội Phủ Dầy Tại Nam Định',
						    (10, 3) : 'Kết Thúc Hội Phủ Dầy Tại Nam Định',
						    (4, 3)  : 'Hội đền Hai Bà Trưng Tại Mê Linh, Hà Nội',
						    (4, 1)  : 'Hội Liễu Đôi Tại Nam Định',
						    (8, 1)  : 'Bắt Đầu Hội Chùa Đậu Tại Thường Tín, Hà Nội',
						    (10, 1) : 'Kết Thúc Hội Chùa Đậu Tại Thường Tín, Hà Nội',
						    (12, 12): 'Hội Đống Đa Tại Đống Đa, Hà Nội; Tây Sơn, Bình Định',
						    (1, 12) : 'Bắt Đầu Hội Chùa Hương Tại Mỹ Đức, Hà Nội',
						    (10, 1) : 'Lễ hội đua Voi Tại Buôn Ma Thuột, Đắk Lắk',
						    (13, 1) : 'Hội Lim Tại Tiên Du, Bắc Ninh',
						    (10, 12): 'Hội Côn Sơn Tại Hải Dương',
						    (15, 1) : 'Hội Xuân Núi Bà Tại Tây Ninh',
						    (6, 3)  : 'Hội Chùa Tây Phương Tại Thạch Thất Tại Hà Nội',
						    (14, 3) : 'Lễ Hội Gò Tháp  Tháp Mười Tại Đồng Tháp Diễn Ra Trong 3 Ngày : 14,15,16',
						    (14, 11): 'Lễ Hội Gò Tháp  Tháp Mười Tại Đồng Tháp Diễn Ra Trong 3 Ngày : 14,15,16',
						    (7, 3)  : 'Hội Chùa Thầy Tại Quốc Oai, Hà Nội',
						    (10, 3) : 'Giỗ Tổ Hùng Vương Tại Việt Trì, Phú Thọ',
						    (1, 3)  : 'Bắt Đầu Hội Đâm Trâu Tại Buôn Ma Thuột, Đắk Lắk',
						    (31, 3) : 'Kết Thúc Hội Đâm Trâu Tại Buôn Ma Thuột, Đắk Lắk\nKết Thúc Hội Chùa Hương Tại Mỹ Đức, Hà Nội',
						    (9, 4)  : 'Hội Gióng Tại Phù Đổng, Gia Lâm, Hà Nội',
						    (23, 4) : 'Hội Bà Chúa Xứ Tại Châu Đốc, An Giang',
						    (2, 8)  : 'Hội Lăng Lê Văn Duyệt Tại TP Hồ Chí Minh',
						    (9, 8)  : 'Hội Chọi Trâu Đồ Sơn Tại Hải Phòng',
						    (16, 8) : 'Hội Nghinh Ông Tại Tiền Giang, Bến Tre, TP. HCM, Bình Thuận',
						    (20, 8) : 'Hội Côn Sơn - Kiếp Bạc Tại Hải Dương'}

SOLAR_EVENT = {(1, 1) : 'Tết Dương Lịch',
					(9, 1)  : 'Ngày Sinh viên - Học sinh Việt Nam',
					(3, 2)  : 'Ngày thành lập Đảng Cộng sản Việt Nam',
					(27, 2) : 'Ngày Thầy thuốc Việt Nam',
					(8, 3)  : 'Ngày phụ nữ thế giới',
					(26, 3) : 'Ngày thành lập Đoàn Thanh niên Cộng sản Hồ Chí Minh',
					(27, 3) : 'Ngày Thể thao Việt Nam',
					(21, 4) : 'Ngày Sách Việt Nam',
					(30, 4) : 'Kết thúc Chiến tranh Việt Nam',
					(1, 5)  : 'Kỷ niệm ngày của người lao động toàn thế giới',
					(15, 5) : 'Ngày thành lập Đội Thiếu niên Tiền phong Hồ Chí Minh',
					(19, 5) : 'Ngày sinh của Chủ tịch Hồ Chí Minh',
					(5, 6)  : 'Ngày Bác Hồ ra đi tìm đường cứu nước',
					(27, 7) : 'Ngày Thương binh Liệt sĩ',
					(19, 8) : 'Ngày Cách mạng, Tám thành công',
					(2, 9)  : 'Kỷ niệm ngày Chủ tịch Hồ Chí Minh đọc tuyên ngôn độc lập',
					(13, 10): 'Ngày Doanh nhân Việt Nam',
					(20, 10): 'Ngày thành lập Hội Phụ nữ Việt Nam',
					(9, 11) : 'Ngày Pháp luật Việt Nam',
					(20, 11): 'Ngày Nhà giáo Việt Nam',
					(22, 12): 'Ngày thành lập Quân đội Nhân dân Việt Nam',
					(25, 12): 'Ngày Lễ Giáng Sinh'}

SOLAR_IMPORTANT_EVENT = [(1, 1), (10, 3), (30, 4), (1, 5), (2, 9)]

LUNAR_IMPORTANT_EVENT = [(29, 12), (30, 12), (1, 1), (2, 1), (3, 1), (4, 1)]

Builder.load_string('''
<CalendarScreen>:
	FloatLayout:
		Image:
			source: 'Image/Calendar/Background/background.jpg'
			allow_stretch: True
			keep_ratio: False
	BoxLayout:
		padding: 35, 15
		spacing: 10
		canvas:
			Color:
				rgba: 0, 0, 0, .5
			Rectangle:
				pos: self.pos
				size: self.size
		orientation: 'vertical'
		BoxLayout:
			spacing: 5
			size_hint: 1, .2
			Button:
				text: '-'
				size_hint: .5 , 1
				font_size: 25
				on_release: root.previousMonth()
				background_normal: 'Image/Calendar/Button/buttonAdjust.png'
			Label:
				text: '[b]Tháng[/b]'
				markup: True
				font_size: 25
			Button
				text: '+'
				size_hint: .5 , 1
				font_size: 25
				on_release: root.nextMonth()
				background_normal: 'Image/Calendar/Button/buttonAdjust.png'
			Button:
				text: '-'
				size_hint: .5 , 1
				font_size: 25
				on_release: root.previousYear()
				background_normal: 'Image/Calendar/Button/buttonAdjust.png'
			Label:
				text: '[b]Năm[/b]'
				markup: True
				font_size: 25
			Button
				text: '+'
				size_hint: .5 , 1
				font_size: 25
				on_release: root.nextYear()
				background_normal: 'Image/Calendar/Button/buttonAdjust.png'
		Label:
			canvas.before:
				Rectangle:
					pos: self.pos
					size: self.size
					source: 'Image/Calendar/Button/button_default.png'
			size_hint: 1, .2
			id: monthYear_lbl
			font_size: 50
		GridLayout:
			id: calendar
			cols: 7
			spacing: 5
		BoxLayout:
			size_hint: 1, .2
			spacing: 10
			Button:
				text: '[color=00ff00][b]Xem Ngày[/b][/color]'
				markup: True
				background_normal: 'Image/Calendar/Button/button_default.png'
				on_release: root.viewDay()
			Button:
				id: back_btn
				text: '[color=00ff00][b]Quay Lại[/b][/color]'
				markup: True
				background_normal: 'Image/Calendar/Button/button_default.png'
				on_release: root.back()

''')

class AutoLineBreakLabel(GridLayout):
	def __init__(self, text, width=300, markup=True, valign='top', halign='left', **kwargs):
		super(AutoLineBreakLabel, self).__init__(**kwargs)
		self.size_hint = (None, None)
		self.width = width
		self.cols = 1
		self.pos_hint = {'center_x': .5, 'center_y': .5}
		self.bind(minimum_height=self.setter('height'))
		self.label = Label(text=text, size_hint=(1, None), halign=halign, valign=valign, markup=markup)
		self.label.bind(width=lambda obj, value:
							self.label.setter('text_size')(obj, (value, None)))
		self.label.bind(texture_size=self.label.setter('size'))
		self.add_widget(self.label)

class ScrollViewLabel(ScrollView):
	def __init__(self, text, width=300, pos_hint={'center_x': .5, 'center_y': .5}, **kwargs):
		super(ScrollViewLabel, self).__init__(**kwargs)
		self.size_hint = (None, 1)
		self.width = width
		self.pos_hint = pos_hint
		self.do_scroll_x = False
		self.add_widget(AutoLineBreakLabel(text=text, width=width))

class CalendarScreen(Screen):
	def __init__(self, **kwargs):
		super(CalendarScreen, self).__init__(**kwargs)
		self.sm = kwargs['sm']
		self.mainScreen = kwargs['mainScreen']
		self.calendar = self.ids['calendar']
		self.monthYear_lbl = self.ids['monthYear_lbl']
		self.day = datetime.date.today()
		self.day_of_week = ['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ Nhật']
		self.cur_year = self.day.year
		self.cur_month = self.day.month
		self.addCalendar(self.cur_month, self.cur_year)

	def addCalendar(self, month, year):
		''' add Calendar widgets to Calendar Screen '''
		# Calculate days in month
		if month != 12:
			nextMonth = month + 1
			nextYear = year
		else:
			nextMonth = 1
			nextYear = year + 1
		now = datetime.date(year, month, 1)
		future = datetime.date(nextYear, nextMonth, 1)
		self.numOfDay = (future - now).days
		self.dayOffset = now.weekday()  # Return day in week

		self.calendar.clear_widgets()
		self.monthYear_lbl.text = '%s/%s' % (month, year)
		for i in range(7):  # add day label (Monday, Tuesday,...)
			self.calendar.add_widget(Button(text='[color=00ffff][i]%s[/i][/color]' % self.day_of_week[i],
											background_normal='Image/Calendar/Button/buttonMenu.png',
											background_down='Image/Calendar/Button/buttonMenu.png',
											size_hint=(1, 2), markup = True, font_size=20))
		for i in range(self.dayOffset):	 # add day offset
			self.calendar.add_widget(Label())
		for i in range(self.numOfDay):  # add day button
			background = 'Image/Calendar/Button/button_day.png'
			day = i + 1
			month = self.cur_month
			year = self.cur_year
			lunar_day = self.lunarDay(day, month, year)
			lunar_text = '%s/%s' % (lunar_day[0], lunar_day[1])
			color = self.getDayColor(day, month, year)
			text = (color, str(day), lunar_text)
			# check if day is today or not
			if i + 1 == self.day.day and self.cur_month == self.day.month and self.cur_year == self.day.year:
				background = 'Image/Calendar/Button/button_cur_day.png'
				day_btn = Button(text='[size=20][color=%s][b]%s[b][/color][/size]\n[size=10][i]%s[/i][/size]' % text,
								 background_normal=background, markup=True, valign='middle', halign='center')
			else:
				day_btn = Button(text='[size=20][color=%s][b]%s[/b][/color][/size]\n[size=10][i]%s[/i][/size]' % text,
								background_normal=background, markup=True, valign='middle', halign='center')
			day_btn.day = day  # day attribute for bind function
			self.calendar.add_widget(day_btn)
			day_btn.bind(on_release=self.dayDetail)

	def getDayColor(self, day, month, year):
		lunar_day, lunar_month, lunar_year = self.lunarDay(day, month, year)

		event_color = 'ffffff'

		for evt in LUNAR_EVENT:
			if (lunar_day, lunar_month) == evt:
				event_color = '00ff00'

		for evt in SOLAR_TRADITIONAL_EVENT:
			if (day, month) == evt:
				event_color = '00ff00'

		for evt in SOLAR_EVENT:
			if (day, month) == evt:
				event_color = '00ffff'

		if (lunar_day, lunar_month) in LUNAR_IMPORTANT_EVENT:
			event_color = 'ff0000'

		if (day, month) in SOLAR_IMPORTANT_EVENT:
			event_color = 'ff0000'

		return event_color

	def dayDetail(self, obj):
		''' Bind function '''
		popup = DateDetailPopup(size_hint=(.35, .9), day=obj.day, month=self.cur_month, year=self.cur_year)
		popup.open()

	def lunarDay(self, day, month, year):
		lunar_date = lunardate.LunarDate.fromSolarDate(year, month, day)
		return lunar_date.day, lunar_date.month, lunar_date.year

	def nextMonth(self):
		if self.cur_month == 12:
			self.cur_year += 1
		self.cur_month = (self.cur_month) % 12 + 1
		self.addCalendar(self.cur_month, self.cur_year)

	def previousMonth(self):
		if self.cur_month == 1:
			self.cur_year -= 1
		self.cur_month = (self.cur_month - 2) % 12 + 1
		self.addCalendar(self.cur_month, self.cur_year)

	def nextYear(self):
		self.cur_year += 1
		self.addCalendar(self.cur_month, self.cur_year)

	def previousYear(self):
		self.cur_year -= 1
		self.addCalendar(self.cur_month, self.cur_year)

	def viewDay(self):
		popup = viewDayPopup(size_hint=(.3, .23))
		popup.open()

	def back(self):
		self.sm.current = self.mainScreen

class DateDetailPopup(ModalView):
	def __init__(self, **kwargs):
		super(DateDetailPopup, self).__init__(**kwargs)
		self.day = kwargs['day']
		self.month = kwargs['month']
		self.year = kwargs['year']
		self.day_of_week = ['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ Nhật']

		self.can_year_list = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
		self.chi_year_list = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mảo', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']

		self.chi_month_list = ['Dần', 'Mảo', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu']
		self.can_month_list = {'Giáp Kỷ': 'Bính', 'Bính Tân': 'Canh', 'Đinh Nhâm': 'Nhâm', 'Mậu Quý' : 'Giáp', 'Ất Canh': 'Mậu'}

		self.all_can_chi_list = ['Giáp Tý', 'Ất Sửu', 'Bính Dần', 'Đinh Mão', 'Mậu Thìn', 'Kỷ Tỵ', 'Canh Ngọ',
								 'Tân Mùi', 'Nhâm Thân', 'Quý Dậu', 'Giáp Tuất', 'Ất Hợi', 'Bính Tý', 'Đinh Sửu',
								 'Mậu Dần', 'Kỷ Mão', 'Canh Thìn', 'Tân Tỵ', 'Nhâm Ngọ', 'Quý Mùi', 'Giáp Thân',
								 'Ất Dậu', 'Bính Tuất', 'Đinh Hợi', 'Mậu Tý', 'Kỷ Sửu', 'Canh Dần', 'Tân Mão',
								 'Nhâm Thìn', 'Quý Tỵ', 'Giáp Ngọ', 'Ất Mùi', 'Bính Thân', 'Đinh Dậu', 'Mậu Tuất',
								 'Kỷ Hợi', 'Canh Tý', 'Tân Sửu', 'Nhâm Dần', 'Quý Mão', 'Giáp Thìn', 'Ất Tỵ',
								 'Bính Ngọ', 'Đinh Mùi', 'Mậu Thân', 'Kỷ Dậu', 'Canh Tuất', 'Tân Hợi ', 'Nhâm Tý',
								 'Quý Sửu', 'Giáp Dần', 'Ất Mão', 'Bính Thìn', 'Đinh tỵ', 'Mậu Ngọ', 'Kỷ Mùi',
								 'Canh thân', 'Tân Dậu', 'Nhâm Tuất', 'Quý Hợi']

		self.can_chi_first_day = [datetime.date(1900, 1, 31), self.all_can_chi_list.index('Giáp Thìn')]

		self.can_first_hour = 'Giáp'  # first hour of 31/1/1900 ~ 1/1/1900 in lunar calendar

		self.can_chi_hour_list = [('Tý', 23, 0), ('Sửu', 1, 2), ('Dần', 3, 4), ('Mão', 5, 6), ('Thìn', 7 ,8), ('Tị', 9, 10),
								 ('Ngọ', 11, 12), ('Mùi', 13, 14), ('Thân', 15, 16), ('Dậu', 17, 18), ('Tuất', 19, 20), ('Hợi', 21, 22)]

		self.update(self.day, self.month, self.year)
		Clock.schedule_interval(self.update_time, 1)

	def update(self, day, month, year):
		lunar_day, lunar_month, lunar_year = self.lunarDay(day, month, year)
		solar_day = datetime.date(year, month, day)
		dayOfMonth = solar_day.day
		dayOfWeek = self.day_of_week[solar_day.weekday()]
		month = solar_day.month
		year = solar_day.year
		event_text = self.getEvent(day, month, year)
		self.layout = RelativeLayout()
		box = BoxLayout(orientation='vertical')

		solar_layout = RelativeLayout(size_hint=(1, 3))
		solar_box = BoxLayout(spacing=2, padding=2, orientation='vertical')
		solar_background_image = Image(source='Image/Calendar/Background/Calendar/snow.png', allow_stretch=True, keep_ratio=False)

		monthYear_lbl = Label(text='[color=ffffff][b]Tháng %s Năm %s[/b][/color]' % (month, year), size_hint=(1, .3),
								font_size=20, valign='top', halign='center', markup=True)
		day_lbl = Label(text='[color=000000][b][size=150]%s[/size]\n[size=35]%s[/size][/b][/color]' % (dayOfMonth, dayOfWeek),
						size_hint=(1, 3), valign='top', halign='center', markup=True)

		event_lbl = AutoLineBreakLabel(text='[color=%s][b][size=13]%s[/size][/b][/color]' % event_text,
										width=320, valign='middle', halign='center')
		solar_box.add_widget(Label(size_hint=(1, .2)))
		solar_box.add_widget(monthYear_lbl)
		solar_box.add_widget(day_lbl)
		solar_box.add_widget(event_lbl)

		solar_layout.add_widget(solar_background_image)
		solar_layout.add_widget(solar_box)

		lunar_canChi_layout = RelativeLayout(size_hint=(1, 1))
		lunar_canChi_box = GridLayout(spacing=2, padding=2, cols=4)

		lunar_lbl_background = 'Image/Calendar/Button/button_default.png'
		self.lunar_time_lbl = Button(text='[size=15][b]Giờ[/b][/size]\n[color=ff0000]%s[/color]' % self.get_time(), markup=True,
								background_normal=lunar_lbl_background, background_down=lunar_lbl_background,
								valign='middle', halign='center',)

		lunar_day_lbl = Button(text='[size=15][b]Ngày[/b][/size]\n[color=ff0000]%s[/color]' % lunar_day, markup=True,
								background_normal=lunar_lbl_background, background_down=lunar_lbl_background,
								valign='middle', halign='center',)

		lunar_month_lbl = Button(text='[size=15][b]Tháng[/b][/size]\n[color=ff0000]%s[/color]' % (lunar_month), markup=True,
								background_normal=lunar_lbl_background, background_down=lunar_lbl_background,
								valign='middle', halign='center')

		lunar_year_lbl = Button(text='[size=15][b]Năm[/b][/size]\n[color=ff0000]%s[/color]' % (lunar_year), markup=True,
								background_normal=lunar_lbl_background, background_down=lunar_lbl_background,
								valign='middle', halign='center')

		self.canChi_time_lbl = Button(text='[color=ff0000]%s[/color]' % self.get_canchi_time_by_day(), markup=True,
								background_normal=lunar_lbl_background, background_down=lunar_lbl_background,
								valign='middle', halign='center',)

		canChi_day_lbl = Button(text='[color=ff0000]%s[/color]' % self.getCanChiDay(solar_day), markup=True,
								background_normal=lunar_lbl_background, background_down=lunar_lbl_background,
								valign='middle', halign='center',)

		canChi_month_lbl = Button(text='[color=ff0000]%s %s[/color]' % (self.getCanChiMonth(lunar_month, lunar_year)), markup=True,
								background_normal=lunar_lbl_background, background_down=lunar_lbl_background,
								valign='middle', halign='center')

		canChi_year_lbl = Button(text='[color=ff0000]%s %s[/color]' % (self.getCanChiYear(lunar_year)), markup=True,
								background_normal=lunar_lbl_background, background_down=lunar_lbl_background,
								valign='middle', halign='center')

		lunar_canChi_box.add_widget(self.lunar_time_lbl)
		lunar_canChi_box.add_widget(lunar_day_lbl)
		lunar_canChi_box.add_widget(lunar_month_lbl)
		lunar_canChi_box.add_widget(lunar_year_lbl)
		lunar_canChi_box.add_widget(self.canChi_time_lbl)
		lunar_canChi_box.add_widget(canChi_day_lbl)
		lunar_canChi_box.add_widget(canChi_month_lbl)
		lunar_canChi_box.add_widget(canChi_year_lbl)
		lunar_canChi_box.add_widget(Label(size_hint=(1, .8)))

		lunar_canChi_layout.add_widget(lunar_canChi_box)

		box.add_widget(solar_layout)
		box.add_widget(lunar_canChi_layout)

		background_image = Image(source='Image/Calendar/Background/Calendar/background_lunar_calendar.png', allow_stretch=True, keep_ratio=False)

		self.layout.add_widget(background_image)
		self.layout.add_widget(box)
		self.add_widget(self.layout)
		self.getAllCanChiDay()

	def update_time(self, *args):
		now = self.get_time()
		self.lunar_time_lbl.text = '[size=15][b]Giờ[/b][/size]\n[color=ff0000]%s[/color]' % now
		self.canChi_time_lbl.text = '[color=ff0000]%s[/color]' % self.get_canchi_time_by_day()

	def get_time(self):
		''' Get time from now '''
		now = datetime.datetime.now().time()
		return str(now)[:8]

	def get_canchi_time_by_now(self, time):
		hour = int(time[:2])

		chi = ''
		chi_hour_offset = 0  # calculate 'can' in day
		for i in range(len(self.can_chi_hour_list)):
			if hour in self.can_chi_hour_list[i][1:3]:
				chi = self.can_chi_hour_list[i][0]
				chi_hour_offset = i

		dayRange = (datetime.date(self.year, self.month, self.day) - self.can_chi_first_day[0]).days
		hourRange = dayRange * 24
		hourOffset = (self.can_year_list.index(self.can_first_hour) + hourRange + chi_hour_offset) % len(self.can_year_list)
		can = self.can_year_list[hourOffset]
		return can + ' ' + chi

	def get_canchi_time_by_day(self):
		chi = 'Tý'
		dayRange = (datetime.date(self.year, self.month, self.day) - self.can_chi_first_day[0]).days
		hourRange = dayRange * 24
		hourOffset = (self.can_year_list.index(self.can_first_hour) + hourRange) % len(self.can_year_list)
		can = self.can_year_list[hourOffset]
		return can + ' ' + chi

	def getEvent(self, day, month, year):
		'''Return event and color of event'''
		event = ''
		event_color = 'ffffff'
		lunar_day, lunar_month, lunar_year = self.lunarDay(day, month, year)

		for evt in LUNAR_EVENT:
			if (lunar_day, lunar_month) == evt:
				event = event + LUNAR_EVENT[evt] + '\n'
				event_color = '00ff00'

		for evt in SOLAR_TRADITIONAL_EVENT:
			if (day, month) == evt:
				event = event + SOLAR_TRADITIONAL_EVENT[evt] + '\n'
				event_color = '00ff00'

		for evt in SOLAR_EVENT:
			if (day, month) == evt:
				event = event + SOLAR_EVENT[evt] + '\n'
				event_color = '00ffff'

		if (lunar_day, lunar_month) in LUNAR_IMPORTANT_EVENT:
			event_color = 'ff0000'

		if (day, month) in SOLAR_IMPORTANT_EVENT:
			event_color = 'ff0000'

		return event_color, event

	def getCanChiYear(self, year):
		''' Return Can Chi Year '''
		start = int(str(year)[:2])  # get first two number
		end = int(str(year)[-2:])  # get last two number
		can = int(str(year)[-1])
		chi = ((start % 3) * 4 + end) % 12  # Can Chi Year = Can + Chi
		return (self.can_year_list[can], self.chi_year_list[chi])

	def getCanChiMonth(self, month, year):
		''' Return Can Chi Month '''
		canYear = self.getCanChiYear(year)[0]
		chi = self.chi_month_list[month - 1]
		canOfJanuary = ''

		# Check if Can of Year in can_month_list or not
		for i in self.can_month_list:
			if canYear in i:
				canOfJanuary = self.can_month_list[i]
				break

		# Calculate current year from January
		can = self.can_year_list[(self.can_year_list.index(canOfJanuary) + month - 1) % 10]
		return can, chi

	def getCanChiDay(self, day):
		dayRange = day - self.can_chi_first_day[0]
		can_chi_day_offset = (self.can_chi_first_day[1] + dayRange.days) % len(self.all_can_chi_list)
		return self.all_can_chi_list[can_chi_day_offset]

	def getAllCanChiDay(self):
		allCanChiDay = {}
		curDay = datetime.date(1900, 1, 31)  # ~1/1/1990 in Lunar Calendar
		for year in range(1901, 2056):
			allCanChiDay[curDay.year, curDay.day, curDay.month] = "Giáp Thìn"
			offset = 360
			curDay = curDay + datetime.timedelta(days=offset)

	def isLeapSolarYear(self, year):
		return (((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0)

	def isLeapLunarYear(self, year):
		''' Check if lunar year is leap or not '''
		if (year % 19) in (0, 3, 6, 9, 11, 14, 17):
			return True
		return False

	def lunarDay(self, day, month, year):
		''' Return Lunar Day from Solar Day '''
		lunar_date = lunardate.LunarDate.fromSolarDate(year, month, day)
		return lunar_date.day, lunar_date.month, lunar_date.year

class viewDayPopup(ModalView):
	def __init__(self, **kwargs):
		super(viewDayPopup, self).__init__(**kwargs)

		box = BoxLayout(orientation='vertical', spacing=10)
		get_input_box = BoxLayout(size_hint=(1, None), height=30)
		self.day_input = TextInput(multiline=False)
		self.month_input = TextInput(multiline=False)
		self.year_input = TextInput(multiline=False)
		day_lbl = Label(text='Ngày')
		month_lbl = Label(text='Tháng')
		year_lbl = Label(text='Năm')

		submit_btn = Button(text='OK', size_hint=(.2, 1), halign='center')
		anchor_submit_layout = AnchorLayout(anchor_x='center')
		anchor_submit_layout.add_widget(submit_btn)

		get_input_box.add_widget(day_lbl)
		get_input_box.add_widget(self.day_input)
		get_input_box.add_widget(month_lbl)
		get_input_box.add_widget(self.month_input)
		get_input_box.add_widget(year_lbl)
		get_input_box.add_widget(self.year_input)

		box.add_widget(get_input_box)
		box.add_widget(anchor_submit_layout)

		self.add_widget(box)
		self.day_input.focus = True
		self.day_input.bind(on_text_validate=self.dayValidate)
		self.month_input.bind(on_text_validate=self.monthValidate)
		self.year_input.bind(on_text_validate=self.yearValidate)
		submit_btn.bind(on_release=self.update)

	def dayValidate(self, obj):
		self.month_input.focus = True

	def monthValidate(self, obj):
		self.year_input.focus = True

	def yearValidate(self, obj):
		self.update(obj)

	def update(self, obj):
		day = self.day_input.text
		month = self.month_input.text
		year = self.year_input.text
		if day and month and year:
			if self.checkValidDay(day, month, year) and 1900 <= int(year) <= 2055:
				self.dismiss()
				popup = DateDetailPopup(day=int(day), month=int(month), year=int(year), size_hint=(.35, .9))
				popup.open()
				return
			else:
				Popup(content=Label(text="Năm Phải Nằm Trong Khoảng 1900 - 2055"), size_hint=(.3, .2), title="Error").open()

		else:
			Popup(content=Label(text="Bạn Phải Nhập Đủ Ngày Tháng Năm"), size_hint=(.3, .2), title="Error").open()

	def checkValidDay(self, day, month, year):
		try:
			datetime.date(int(year), int(month), int(day))
			return True
		except:
			return False

if __name__ == '__main__':
	sm = ScreenManager()
	calendarScreen = CalendarScreen(name='CalendarScreen', sm=sm, mainScreen='CalendarScreen')
	sm.add_widget(calendarScreen)

	class CalendarScreenApp(App):
		def build(self):
			Window.size = (1024, 600)
			return sm
	CalendarScreenApp(title='Calendar Screen').run()
