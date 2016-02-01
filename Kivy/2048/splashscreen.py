from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
Builder.load_string('''
<WidgetAnimation>:
	# canvas.before:
	# 	Rectangle:
	# 		pos: self.pos
	# 		size: self.size
	# 		source: 'assets/image/splash.png'
<SplashScreen>:
	canvas:
		Rectangle:
			pos: self.pos
			size: self.size
			source: 'assets/image/bg_splashscreen.jpg'
''')
class WidgetAnimation(Label):
	def __init__(self, **kwargs):
		super(WidgetAnimation, self).__init__(**kwargs)
		self.size_hint = (None, None)
		self.font_size = Window.height / 10
		self.font_name = 'assets/font/2048.ttf'

	def start_anim(self, endX, endY):
		Animation.cancel_all(self)
		anim = Animation(pos=(endX, endY), t='out_bounce', d=3)
		anim.bind(on_complete=self.on_complete)
		anim.start(self)

	def on_complete(self, *args):
		self.parent.add_widget(Label(text="TOUCH ANYWHERE TO START", size_hint=(1, .2), pos=(0, Window.height / 3)))
		self.parent.ready = True

class SplashScreen(Screen):
	def __init__(self, sm=None, switchTo=None, **kwargs):
		super(SplashScreen, self).__init__(**kwargs)
		self.sm = sm
		self.switchTo = switchTo
		self.ready = False
		self.text_image_array = '2 0 4 8'.split()
		self.image_size = Window.width / (len(self.text_image_array)), (Window.width / len(self.text_image_array))
		self.image_margin = 20
		self.image_space = (Window.width) / len(self.text_image_array)
		for (index, text) in enumerate(self.text_image_array[::-1]):
			image = WidgetAnimation(pos=(self.image_space * index, 100), size=self.image_size, text=text)
			self.add_widget(image)
		for (index, image) in enumerate(self.children):
			image.start_anim(self.image_space * index, Window.height - self.image_size[1] * 2)

	def on_touch_down(self, touch):
		if self.sm and self.switchTo and self.ready:
			self.sm.current = self.switchTo
			return True
		return False

if __name__ == '__main__':
	class splashScreen(App):
		def build(self):
			Window.size = (320, 480)
			sm = ScreenManager()
			sm.add_widget(SplashScreen())
			return sm

	if __name__ == '__main__':
		splashScreen().run()
