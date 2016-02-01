import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'libs')
from gesture_box import GestureBox

from controller import _2048Controller
from splashscreen import SplashScreen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.graphics import Rectangle, Color
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.animation import Animation

Builder.load_string('''
<_2048MainBoard>:
	padding: 3
	spacing: 3
<_2048Tile>:
	markup: True
	font_size: 25
	font_name: 'assets/font/2048.ttf'
<_2048Game>:
	BoxLayout:
		orientation: 'vertical'
		BoxLayout:
			size_hint: 1, .2
			Button:
				markup: True
				text: '[color=ffff00]New Game[/color]'
				on_release: root.newGame()
				background_normal: 'assets/image/bg_btn.png'
			Button:
				id: _undo_btn
				markup: True
				text: '[color=ffff00]Undo : 2[/color]'
				on_release: root.undo()
				background_normal: 'assets/image/bg_btn.png'
		BoxLayout:
			size_hint: 1, .3
			Label:
				id: _score_lbl
				font_size: 20
				text_size: self.size
				halign: 'center'
    			valign: 'middle'
			Label:
				id: _best_score_lbl
				font_size: 20
				text_size: self.size
				halign: 'center'
    			valign: 'middle'
		BoxLayout:
			id: _main_board_box
		TimerLabel:
			id: _timer
			size_hint: 1, .2
''')

GAME_CONTROLLER = _2048Controller()  # main processor

class _2048MainBoard(GridLayout):
	def __init__(self, **kwargs):
		super(_2048MainBoard, self).__init__(**kwargs)
		self.game_width = kwargs['game_width']
		self.game_height = kwargs['game_height']
		self.cols = self.game_width
		for count in range(self.game_height * self.game_width):
			self.add_widget(_2048Tile())
		self.all_game_button = self.generateAllGameButton()
		self.all_color = self.generateAllColor()  # generate color for display background
		self.rect_array = self.generateRectArray()
		self.drawBackground()
		self.bind(pos=self.update_rects, size=self.update_rects)

	def generateRectArray(self):
		array = []
		for y in range(self.game_height):
			rows = []
			for x in range(self.game_width):
				rows.append(0)
			array.append(rows)
		return array

	def drawBackground(self):
		button_size = (self.width / self.game_width, \
						self.height / self.game_height)
		with self.canvas.before:
			for x in range(self.game_width):
				for y in range(self.game_height):
					button_pos = (self.x + x * button_size[0], \
									self.y + y * button_size[1])
					rect = Rectangle(size=button_size, pos=button_pos, source='assets/image/bg_tile2.png')
					self.rect_array[y][x] = rect

	def update_rects(self, *args):
		button_size = (self.width / self.game_width, \
						self.height / self.game_height)
		for y in range(len(self.rect_array)):
			for x in range(len(self.rect_array[0])):
				button_pos = (self.x + x * button_size[0], \
									self.y + y * button_size[1])
				self.rect_array[y][x].pos = button_pos
				self.rect_array[y][x].size = button_size

	def generateAllColor(self):
		all_color = []
		for i in range(0, 18):
			# red = 1
			# green = (1/6.0) * (6 - i % 6)
			# blue = (1/6.0) * (6 - i % 6)
			# if (i / 6.0) % 2 >= 1:
			# 	red = 0.95
			# 	green = 0.95
			# 	blue = (1/6.0) * (6 - i % 6) * 1 / 2
			division = 3.0 * (i / 6 + 1)  # generate random, dont need to understand this part
			red = (1 / 3.0) * (3 - i % 3 * (i / 12))
			green = (1/6.0) * (6 - i % 6) + (i / 6)
			blue = (1 / division) * (division - i % division) / ((i / division) + 1)
			alpha = 255
			print red, green, blue
			all_color.append([pow(2, i + 1), [red, green, blue, alpha]])  # ex: [(2, (1, 1, 1)), (4, (1, 2, 1) .... (2048, (1, 2, 2)))]
		return all_color

	def generateAllGameButton(self):
		all_game_button = []
		all_child = self.children[:]
		for y in range(self.game_height):
			rows = []
			for x in range(self.game_width):
				rows.append(all_child.pop())
			all_game_button.append(rows)
		return all_game_button

	def draw(self, animation_way):
		if not animation_way:
			self.drawTile(GAME_CONTROLLER.game_array, GAME_CONTROLLER.new_number_array)
		else:
			for way in animation_way:
				current_x, current_y = way[0]
				target_x, target_y = way[1]
				current_object = self.all_game_button[current_y][current_x]
				target_object = self.all_game_button[target_y][target_x]
				current_object.doSlide(target_object.pos[:])

	def drawTile(self, game_array, new_number_array):
		for y in range(self.game_height):
			for x in range(self.game_width):
				number = game_array[y][x]
				color = (1, 1, 1, 0)  # default color for 0
				if number == 0:  # dont draw 0
					self.all_game_button[y][x].text = ''
					self.all_game_button[y][x].changeBackground(color)
					continue
				for color_temp in self.all_color:  # get color from generated list
					if number == color_temp[0]:
						color = color_temp[1]
				template = '[color=888888]%s[/color]'  # template to display
				if number > 4:
					template = '[color=ffffff]%s[/color]'  # template to display
				self.all_game_button[y][x].text = template % (number)
				self.all_game_button[y][x].changeBackground(color)
				if (x, y) in new_number_array:  # only animate new number
					new_number_array.remove((x, y))
					self.all_game_button[y][x].doAnimation()

class _2048Tile(Label):
	def __init__(self, **kwargs):
		super(_2048Tile, self).__init__(**kwargs)
		self.rect = Rectangle(pos=self.pos, size=self.size, source='assets/image/bg_tile.png')
		self._background_color = Color(rgba=(1, 1, 1, 0))
		self.bind(pos=self.update_rect, size=self.update_rect)  # bind rect in canvas to button
		self.mutexAnimation = False  # only one animation do at same time
		self.canvas.before.add(self._background_color)
		self.canvas.before.add(self.rect)

	def update_rect(self, *args):
		self.rect.pos = self.pos
		self.rect.size = self.size

	def changeBackground(self, background=(1, 1, 1, 1)):
		self._background_color.rgba = background

	def doAnimation(self):
		if not self.mutexAnimation:
			anim = Animation(pos=(self.x + 10, self.y + 10), duration=.05) + \
					Animation(pos=(self.x, self.y), duration=.05)
			anim.bind(on_start=self.on_start_animation)
			anim.bind(on_complete=self.on_complete_animation)
			anim.start(self)

	def on_start_animation(self, *args):
		self.mutexAnimation = True

	def on_complete_animation(self, *args):
		self.mutexAnimation = False

	def doSlide(self, pos):
		if not self.mutexAnimation:
			self.old_pos = self.pos[:]
			anim = Animation(pos=pos, duration=0.1)
			anim.bind(on_start=self.on_start_slide)
			anim.bind(on_complete=self.on_complete_slide)
			anim.start(self)

	def on_start_slide(self, *args):
		self.mutexAnimation = True

	def on_complete_slide(self, *args):
		self.parent.drawTile(GAME_CONTROLLER.game_array, GAME_CONTROLLER.new_number_array)
		self.mutexAnimation = False
		self.pos = self.old_pos

class TimerLabel(Label):
	time = NumericProperty(0)

	def __init__(self, **kwargs):
		super(TimerLabel, self).__init__(**kwargs)
		self.markup = True
		self.text = "[b]Playing Time: 00:00[/b]"

	def on_time(self, obj, val):
		self.text = "[b][color=ff0000]" + "Playing Time: " + self.convertSecondToMinute(val) + "[/color][/b]"

	def convertSecondToMinute(self, second):
		minute = 0
		while second > 59:
			minute += 1
			second -= 60
		return "%02d:%02d" % (minute, second)

	def update_timer(self, dt):
		self.time += 1

	def resetTimer(self):
		self.text = "[b]Playing Time: 00:00[/b]"
		self.time = 0

	def scheduleTimer(self):
		Clock.schedule_interval(self.update_timer, 1)

	def unscheduleTimer(self):
		Clock.unschedule(self.update_timer)

class WinGamePopup(ModalView):
	def __init__(self, **kwargs):
		super(WinGamePopup, self).__init__(**kwargs)
		self.auto_dismiss = False
		self.on_new_game = kwargs['on_new_game']  # callback when click new game
		self.on_continue = kwargs['on_continue']  # callback when click continue
		self.container = BoxLayout(orientation='vertical')
		self.status_lbl = Label(halign='center', valign='middle', \
								text='You Win', font_size=25)
		self.continue_btn = Button(text="Keep Going", on_release=self.continue_callback)
		self.new_game_btn = Button(text="New Game", on_release=self.new_game_callback)
		self.container.add_widget(self.status_lbl)
		self.container.add_widget(self.continue_btn)
		self.container.add_widget(self.new_game_btn)
		self.content = self.container

	def new_game_callback(self, *args):
		self.on_new_game()
		self.dismiss()

	def continue_callback(self, *args):
		self.on_continue()
		self.dismiss()

class EndGamePopup(ModalView):
	def __init__(self, **kwargs):
		super(EndGamePopup, self).__init__(**kwargs)
		self.auto_dismiss = False
		self.on_new_game = kwargs['on_new_game']  # callback when click new game
		self.container = BoxLayout(orientation='vertical')
		self.status_lbl = Label(halign='center', valign='middle')
		self.new_game_btn = Button(text="New Game", on_release=self.new_game_callback)
		self.exit_btn = Button(text="Exit Game", on_release=App.get_running_app().stop)
		self.container.add_widget(self.status_lbl)
		self.container.add_widget(self.new_game_btn)
		self.container.add_widget(self.exit_btn)
		self.add_widget(self.container)

	def new_game_callback(self, *args):
		self.on_new_game()
		self.dismiss()

	def update_status(self, value):
		self.status_lbl.text = value

class _2048Game(GestureBox):
	def __init__(self, **kwargs):
		super(_2048Game, self).__init__(**kwargs)
		self.main_board_box = self.ids['_main_board_box']  # main game box
		self.main_board = _2048MainBoard(game_width=GAME_CONTROLLER.width, game_height=GAME_CONTROLLER.height)
		self.main_board_box.add_widget(self.main_board)
		self.undo_btn = self.ids['_undo_btn']
		self.score_lbl = self.ids['_score_lbl']
		self.best_score_lbl = self.ids['_best_score_lbl']
		self.timer = self.ids['_timer']
		self.end_popup = EndGamePopup(size_hint=(.8, .8), on_new_game=self.newGame)
		self.win_popup = WinGamePopup(size_hint=(.8, .4), on_new_game=self.newGame, on_continue=self.continueGame)
		self.play_game = False
		self.continue_play_after_win_game = False
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
		if self._keyboard.widget:
			#  If it exists, this widget is a VKeyboard object which you can use
			#  to change the keyboard layout.
			pass
		self._keyboard.bind(on_key_down=self._on_keyboard_down)

	def drawGame(self, animation_way=None):
		self.main_board.draw(animation_way)
		self.undo_btn.text = '[color=ffff00]Undo : [b]%s[/b][/color]' % GAME_CONTROLLER.undo_left
		self.score_lbl.text = 'SCORE\n' + str(GAME_CONTROLLER.score)
		self.best_score_lbl.text = 'BEST\n' + str(GAME_CONTROLLER.best_score)

	def checkForWin(self):
		if not self.continue_play_after_win_game:
			if GAME_CONTROLLER.checkForWin():
				self.play_game = False  # pause game
				self.continue_play_after_win_game = True
				self.timer.unscheduleTimer()
				self.win_popup.open()

	def up(self):
		if self.play_game:
			self.animation_way = GAME_CONTROLLER.up()
			if GAME_CONTROLLER.end_game:
				self.endGame()
			self.drawGame(self.animation_way)
			self.checkForWin()

	def down(self):
		if self.play_game:
			self.animation_way = GAME_CONTROLLER.down()
			if GAME_CONTROLLER.end_game:
				self.endGame()
			self.drawGame(self.animation_way)
			self.checkForWin()

	def left(self):
		if self.play_game:
			self.animation_way = GAME_CONTROLLER.left()
			if GAME_CONTROLLER.end_game:
				self.endGame()
			self.drawGame(self.animation_way)
			self.checkForWin()

	def right(self):
		if self.play_game:
			self.animation_way = GAME_CONTROLLER.right()
			if GAME_CONTROLLER.end_game:
				self.endGame()
			self.drawGame(self.animation_way)
			self.checkForWin()

	def undo(self):
		if self.play_game:
			GAME_CONTROLLER.undo()
			self.drawGame()

	def continueGame(self, *args):
		self.play_game = True
		self.timer.scheduleTimer()

	def newGame(self, *args):
		self.play_game = True
		self.animation_way = []
		self.continue_play_after_win_game = False
		self.timer.resetTimer()
		self.timer.unscheduleTimer()
		self.timer.scheduleTimer()
		GAME_CONTROLLER.initGame()
		self.drawGame()

	def endGame(self):
		self.play_game = False
		self.timer.unscheduleTimer()
		self.end_popup.update_status("You Lost\nYour Score: %s" % GAME_CONTROLLER.score)
		self.end_popup.open()

	def on_left_to_right_line(self):
		self.right()

	def on_right_to_left_line(self):
		self.left()

	def on_bottom_to_top_line(self):
		self.up()

	def on_top_to_bottom_line(self):
		self.down()

	def on_enter(self, *args):
		self.newGame()

	def _keyboard_closed(self):
		print('My keyboard have been closed!')
		self._keyboard.unbind(on_key_down=self._on_keyboard_down)
		self._keyboard = None

	def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
		# Keycode is composed of an integer + a string
		# If we hit escape, release the keyboard
		if keycode[1] == 'escape':
			keyboard.release()
			return True
		elif keycode[1] in ('up', 'w'):
			self.up()
			return True
		elif keycode[1] in ('down', 's'):
			self.down()
			return True
		elif keycode[1] in ('left', 'a'):
			self.left()
			return True
		elif keycode[1] in ('right', 'd'):
			self.right()
			return True
		elif keycode[1] == 'n':
			self.newGame()
			return True
		# Return True to accept the key. Otherwise, it will be used by
		# the system.
		return False

class _2048App(App):
	def build(self):
		Window.size = (320, 480)
		sm = ScreenManager()
		sm.add_widget(SplashScreen(name='SplashScreen', sm=sm, switchTo='_2048Game'))
		sm.add_widget(_2048Game(name='_2048Game'))
		sm.current = 'SplashScreen'
		#sm.current = '_2048Game'
		return sm

	def on_stop(self, *args):
		GAME_CONTROLLER.saveData()

if __name__ == '__main__':
	_2048App().run()
