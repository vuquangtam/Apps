from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.core.window import Window
from fractions import Fraction
from sys import exc_info

def TichChap(lenX,lenH,posX,posH,*args):
	''' TichChap(lenX,lenH,startPosX,startPosH,XVars,HVars)'''
	lenX = int(lenX)
	lenH = int(lenH)
	posX = int(posX)
	posH = int(posH)
	assert len(args) == (lenX) + (lenH), 'len(XVars + HVars) == lenX + lenH'
	args = [str(arg) for arg in args]
	X = [Fraction(x) for x in args[:lenX]]
	H = [Fraction(x) for x in args[lenX:]]
	start = posX + posH
	end = lenX + lenH -1
	ans = ''
	temp = []
	i = lenH - 1
	while i > -1:
		temp.append(H[i])
		i -= 1
	for i in range (0, end - start):
		output = "y(" + str(start+i) + ") = "
		sum = 0
		for j in range (0, lenX):
			output += str(X[j]) + "*"
			if ((lenH - 1 - i + j) > -1) & ((lenH - 1 - i + j) < lenH):
				output += str(temp[lenH - 1 - i + j])
				sum += X[j] * temp[lenH - 1 - i + j]
			else:
				output += str(0)
			if len(output) < 8 + 8*(j+1):
				output += " "*(8 + 8*(j+1) - len(output))
		output += " = " + str(sum)
		ans += output + '\n'
	return ans

class OutputPopup(Popup):
	output = StringProperty()
class TichChapGUI(BoxLayout):
	output = StringProperty()
	lenX = ObjectProperty()
	lenH = ObjectProperty()
	posX = ObjectProperty()
	posH = ObjectProperty()
	varX1 = ObjectProperty()
	varX2 = ObjectProperty()
	varX3 = ObjectProperty()
	varX4 = ObjectProperty()
	varX5 = ObjectProperty()
	varX6 = ObjectProperty()
	varX7 = ObjectProperty()
	varH1 = ObjectProperty()
	varH2 = ObjectProperty()
	varH3 = ObjectProperty()
	varH4 = ObjectProperty()
	varH5 = ObjectProperty()
	varH6 = ObjectProperty()
	varH7 = ObjectProperty()

	def _show_output(self):
		self._execute()
		OutputPopup(output = self.output).open()
	def _execute(self):
		try:
			Vars1 = [self.varX1.textInput,self.varX2.textInput,self.varX3.textInput,self.varX4.textInput,self.varX5.textInput,
					self.varX6.textInput,self.varX7.textInput]
			Vars2 = [self.varH1.textInput,self.varH2.textInput,self.varH3.textInput,self.varH4.textInput,self.varH5.textInput,
					self.varH6.textInput,self.varH7.textInput]
			Vars = Vars1[:int(self.lenX.textInput)] + Vars2[:int(self.lenH.textInput)]
			self.output = TichChap(self.lenX.textInput,self.lenH.textInput,self.posX.textInput,self.posH.textInput,*Vars)
		except: 
			self.output = str(exc_info()[1])
	def _reset(self):
		try:
			Vars = [self.varX1,self.varX2,self.varX3,self.varX4,self.varX5,
					self.varX6,self.varX7,
					self.varH1,self.varH2,self.varH3,self.varH4,self.varH5,
					self.varH6,self.varH7,
					self.lenX, self.lenH]
			for var in Vars:
				var.textInput_id.text = ''
			for var in (self.posX,self.posH):
				var.textInput_id.text = '0'
			self.output = 'Reset'
		except:
			self.output = 'Reset Error'
class TichChapApp(App):
	def build(self):
		Window.size = (320,480)
		tichChapGUI = TichChapGUI()
		tichChapGUI._reset()
		return tichChapGUI
if __name__ == '__main__':
	TichChapApp().run()