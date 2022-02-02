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

class MainApp(App):   # the app object you haven't used yet (inherits from App above)
    def build(self): # def build is from App.
        return RootWidget() # make sure it's the object and not the class (the brackets () initialize it.)

if __name__ == "__main__":
    MainApp().run() # this creates an instance of the Main App and applies its run() method.