from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.app import App
from scapy.all import *
from subprocess import check_output
from threading import Thread
import socket
import time
import os
Builder.load_string('''
<MITMs1>:
	BoxLayout:
		canvas:
			Rectangle:
				pos: self.pos
				size: self.size
				source: 'Image/kapy-bg.jpg'
		BoxLayout:
			id: client_box
			orientation: 'vertical'
			size_hint: .5, 1
			spacing: 10
			Image:
				source: 'Image/3dLogo/pyspin.zip'
				anim_delay: 1/80
				allow_stretch: False
				pos_hint: {'x': -.4}
				size_hint: 1, .2
			Label:
				size_hint: 1, 1
				id: device_lbl
				markup: True
				text: 'Interface Infomation'
			TextInput:
				id: iface_name
				size_hint: 1, .2
				text: 'wlan0'
				multiline: False
			BoxLayout:
				size_hint: 1,.5
				Button:
					size_hint: .5, .4
					text: '[color=00ff00]Run IFCONFIG[/color]'
					markup: True
					background_normal: 'Image/buttonBG.png'
					on_release: root.run_ifconfig()
				Button:
					id: scan_arp_btn
					size_hint: .5, .4
					text: '[color=00ff00]ARP Scan[/color]'
					markup: True
					background_normal: 'Image/buttonBG.png'
					disabled: True
					on_release: root.ARP_scan()
				Button:
					id: save_results_btn
					size_hint: .5, .4
					text: '[color=00ff00]Save[/color]'
					markup: True
					background_normal: 'Image/buttonBG.png'
					on_release: root.save_results()
		ScrollView:
			size_hint: .5, 1
			do_scroll_x: False
			BoxLayout:
				id: nodes
				orientation: 'vertical'
				size_hint: 1, None

<MITMs2>:
	BoxLayout:
		spacing: 5
		canvas:
			Rectangle:
				pos: self.pos
				size: self.size
				source: 'Image/kapy-bg2.jpg'
		BoxLayout:
			orientation: 'vertical'
			BoxLayout:
				id: itf_box
				orientation: 'vertical'
			BoxLayout:
				size_hint: 1, .1
				Button:
					markup: True
					text:'[color=00ff00]Back[/color]'
					on_release: root.mainMenu()
					background_normal: 'Image/buttonBG.png'
				Button:
					markup: True
					text:'[color=00ff00]Port Scan[/color]'
					on_release: root.mainMenu()
					background_normal: 'Image/buttonBG.png'
				Button:
					markup: True
					text:'[color=00ff00]Save Results[/color]'
					on_release: root.mainMenu()
					background_normal: 'Image/buttonBG.png'
		BoxLayout:
			orientation: 'vertical'
			Label:
				text: 'Infomation'
			Button:
				size_hint: 1, .1
				markup: True
				text:'[color=00ff00]Back[/color]'
				on_release: root.mainMenu()
				background_normal: 'Image/buttonBG.png'
''')

class MITMs1(Screen):
	def __init__(self,**kwargs):
		super(MITMs1,self).__init__(**kwargs)
		self.iface_name = self.ids['iface_name']
		self.device_lbl = self.ids['device_lbl']
		self.client_box = self.ids['client_box']
		self.nodes = self.ids['nodes']
		self.scan_arp_btn = self.ids['scan_arp_btn']
		self.save_results_btn = self.ids['save_results_btn']
		self.arps = [] #contain ARP's responses

	def run_ifconfig(self):
		try:
			self.scan_arp_btn.disabled = False
			self.ifconfig = check_output(['ifconfig', self.iface_name.text])
			self.iface, self.IP, self.MAC, self.Bcast, self.Nmask, self.IPv6 = \
			(self.ifconfig.split()[i] for i in (0,6,4,7,8,11))

			self.device_lbl.text = '[color=00ff00][i][b]My Device[/b][/i][/color] \n\n' +\
			'Interface: [color=00ff00][i]{0}[/i][/color] \n\n'.format(self.iface) +\
			'IP: [color=00ff00][i]{0}[/i][/color] \n\n'.format(self.IP[5:]) +\
			'IPv6: [color=00ff00][i]{0}[/i][/color] \n\n'.format(self.IPv6) +\
			'Bcast: [color=00ff00][i]{0}[/i][/color] \n\n'.format(self.Bcast[6:]) +\
			'Nmask: [color=00ff00][i]{0}[/i][/color] \n\n'.format(self.Nmask[5:]) +\
			'MAC: [color=00ff00][i]{0}[/i][/color] \n\n'.format(self.MAC)
		except:
			pass

	def ARP_scan(self):
		network_ip = '192.168.40.'
		self.nodes.clear_widgets()
		self.arps = []
		for i in range(1,255):
			scanNode = ArpScan(self.arps, self.nodes , network_ip + str(i) , self.iface)
			scanNode.start()
			print 'Thread %s'%i

	def now(self):
		now = time.localtime(time.time())
		return time.asctime(now)

	def save_results(self):
		self.box = BoxLayout(orientation = 'vertical')
		self.input_lb = TextInput(text = 'Untitled', multiline = False, on_text_validate = self.save_file)
		self.btn_lb = Button(text = 'Save Results', size_hint = (1, None), height = 50, on_release = self.save_file)

		self.box.add_widget(self.input_lb)
		self.box.add_widget(self.btn_lb)

		self.popup = Popup(content = self.box, title = 'Save Scan Results', size_hint = (.7, .7))
		self.popup.open()

	def save_file(self,obj):
		filename = self.input_lb.text
		if filename == None: return
		f = open(filename,'w')
		content = '[*] Lan Scan \n\n' + self.now() + '\n\n%s Hosts Up!'%len(self.arps) + '\n\n'
		for arp in self.arps:
			content += 'IP : %s\nMAC:%s\n\n'%(arp.psrc,arp.hwsrc)
		self.box.clear_widgets()
		try:
			f.write(content)
			self.box.add_widget(Label(text = 'File saved in : %s'%(os.getcwd() + '/' + filename)))
			self.box.add_widget(Button(text = 'Close', size_hint = (1, None), height = 50, on_release = self.popup.dismiss))
		except:
			self.box.add_widget(Label(text = 'Error while writting file : %s'%filename))
			self.box.add_widget(Button(text = 'Close', size_hint = (1, None), height = 50, on_release = self.popup.dismiss))
	@staticmethod
	def change_screen(obj):
		sm.current = 'MITMs2'
		MITMs1.itf_inform = obj.text
		MITMs1.logo = obj.background_normal
	@staticmethod
	def load_string(obj):
		obj.itf_box.clear_widgets()
		logo_3d_file = {'Image/Node/gatewayNode.png' : 'Image/3dLogo/gateSpin.zip',
				        'Image/Node/windowsNode.png' : 'Image/3dLogo/winSpin.zip',
				  		'Image/Node/appleNode.png'   : 'Image/3dLogo/appleSpin.zip',
				  		'Image/Node/androidNode.png' : 'Image/3dLogo/andSpin.zip',
				  		'Image/Node/linuxNode.png'   : 'Image/3dLogo/linuxSpin.zip',
				  		'Image/Node/unknownNode.png' : 'Image/3dLogo/unkSpin.zip'}
		logo_3d = logo_3d_file[MITMs1.logo]
		obj.itf_box.add_widget(Image(source = logo_3d, anim_delay = 1/80, pos_hint = {'x': -.4}, size_hint = (1, .2)))
		obj.itf_box.add_widget(Label(text = MITMs1.itf_inform, markup = True))



class ArpScan(Thread):
	def __init__(self,arpContain,nodes,ip,iface,**kwargs):
		super(ArpScan,self).__init__(**kwargs)
		self.nodes = nodes
		self.ip = ip
		self.iface = iface
		self.arpContain = arpContain
		self.logos = [['Gateway','192.168.1.1','192.168.40.30'],
					  ['Windows','xp','vista','google'],
					  ['Apple','iphone','mac','ipad'],
					  ['Android','nexus','samsung','htc','lg'],
					  ['Linux','ubuntu','kali','debian','arch','mint','apache']]
		self.logo_file = {'Gateway' : 'Image/Node/gatewayNode.png',
						  'Windows' : 'Image/Node/windowsNode.png',
						  'Apple'   : 'Image/Node/appleNode.png',
						  'Android' : 'Image/Node/androidNode.png',
						  'Linux'   : 'Image/Node/linuxNode.png'}
	def run(self):
		arpRequest = Ether(dst = 'ff:ff:ff:ff:ff:ff') / ARP(pdst = self.ip, hwdst = 'ff:ff:ff:ff:ff:ff')
		arpResponse = srp1(arpRequest , verbose = False , timeout = 1 , iface = self.iface)
		if arpResponse:
			self.arpContain.append(arpResponse)
			self.nodes.size = (0, 150 * len(self.arpContain))

			result = '[color=00ff00][i]Host is up[/i][/color]\n' +\
				   '[color=00ff00][i]IP : {0}[/i][/color]\n'.format(arpResponse.psrc) +\
		 		   '[color=00ff00][i]MAC : {0}[/i][/color]\n'.format(arpResponse.hwsrc) 
			self.node = Button(text = result, markup = True, font_size = '15sp', background_normal = 'Image/Node/unknownNode.png', on_release = MITMs1.change_screen)
			self.nodes.add_widget(self.node)

			def getHost():
				try:
					hostBanner = socket.gethostbyaddr(arpResponse.psrc)[0].lower()
				except:
					hostBanner = ''
				for name in self.logos:
					for banner in name:
						if banner.lower() in hostBanner or \
						   banner.lower() in arpResponse.psrc:
							self.node.background_normal = self.logo_file[name[0]]
			Thread(target = getHost).start()

class MITMs2(Screen):
	def __init__(self,**kwargs):
		super(MITMs2,self).__init__(**kwargs)
		self.itf_box = self.ids['itf_box']
		self.bind(on_enter = MITMs1.load_string)
	def mainMenu(self):
		sm.current = 'MITMs1'
class MITMtool(App):
	def build(self):
		return sm

sm = ScreenManager()
sm.add_widget(MITMs1(name = 'MITMs1'))
sm.add_widget(MITMs2(name = 'MITMs2'))

if __name__ == '__main__':
	MITMtool().run()
