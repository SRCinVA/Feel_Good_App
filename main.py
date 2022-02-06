from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file('design.kv')

# now we create two empty classes with the same names (see below) 
class LoginScreen(Screen):  # under the RootWidget in the hierarchy
# will inherit from screen object
    def sign_up(self): # you can call these parameters anything; they are not related to the ids in the kivy file.
        self.manager.current = "sign_up_screen"
        # self refers to the instance of the LoginScreen object.
        # manager is a property of the parent 'screen'. Self (the instance) is able to access the 'manager' property
        # current is an attribute of manager, and it will get the name of the scrren you want to switch to (in this case, sign_up_screen)

class RootWidget(ScreenManager):  # the next in the hierarchy
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword): # this will send the user input to a json file and store then there.
        print(uname, pword)

class MainApp(App):   # the app object you haven't used yet (inherits from App above). It is the highest in the heirarchy.
    def build(self): # def build is from App.
        return RootWidget() # make sure it's the object and not the class (the brackets () initialize it.)

if __name__ == "__main__":
    MainApp().run() # this creates an instance of the Main App and applies its run() method.