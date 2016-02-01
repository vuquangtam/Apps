from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty,StringProperty
from kivy.core.window import Window
import random
class calculator(BoxLayout):
	Num = StringProperty()
	def answer(self):
		try:
			exec 'self.Num = str(' + self.Num + ')'
			self.Num = str(self.Num)
		except:
			self.Num = ''
	def calculation(self, *args):
		self.Num += args[0].text
	def clear(self):
		self.Num = ''
	def backspace(self):
		self.Num = self.Num[:-1]

class calculatorApp(App):
	def build(self):
		Window.size = (600,1024)
		return calculator()
if __name__ == '__main__':
	calculatorApp().run()