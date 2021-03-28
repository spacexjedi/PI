from kivy. app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image

class Manager(ScreenManager):
	pass

class Menu(Screen):
	pass

class Game(Screen):
	pass

class Pet(Image):
	pass

class Tamagotchi(App):
	pass

'''
class Tamagotchi(App):
	def build(self):
		pet = Image(source='pet.png')
		layout = FloatLayout()
		layout.add_widget(pet)
		return layout
'''
Tamagotchi().run()
