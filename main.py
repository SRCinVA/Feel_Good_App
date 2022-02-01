from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file('design.kv')

# now we create two empty classes with the same names (see below) 
class LoginScreen(Screen):
# will inherit from screen object
    pass
class RootWidget(ScreenManager):
    pass