from datetime import datetime
from fileinput import filename
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import json
from datetime import datetime
import json, glob
from pathlib import Path

Builder.load_file('design.kv')

# now we create two empty classes with the same names (see below) 
class LoginScreen(Screen):  # under the RootWidget in the hierarchy
# will inherit from screen object
    def sign_up(self): # you can call these parameters anything; they are not related to the ids in the kivy file.
        self.manager.current = "sign_up_screen"
        # 'self' refers to the instance of the LoginScreen object.
        # 'manager' is a property of the parent 'screen'. Self (the instance) is able to access the 'manager' property.
        # 'current' is an attribute of 'manager', and it will get the name of the scrren you want to switch to (in this case, sign_up_screen)

    def login(self, uname, pword):  # can use whatever variable names you want here. The 'on_press' element tells the function to look for two things.
        with open("users.json",'r') as file:
            users = json.load(file) # this will create a dictionary for us containing all the info of the .json file
        if uname in users and users[uname]['password'] == pword:   # to check if the name is there and that the password is correct ...
            self.manager.current = 'login_screen_success'
        else:
            self.ids.login_wrong.text = "Wrong username or password!"  # we look for the Label object and the text attached to it.

class RootWidget(ScreenManager):  # the next in the hierarchy
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword): # this will send the user input to a json file and store then there.
        with open("users.json") as file:
            users=json.load(file)

        # to add another user to the database:
        users['uname'] = {'username': uname,  # meaning that username will be whatever we pass in for the uname variable
                        'password': pword, 
                        'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}  # need to get the current time as a string
        #print(users)  # as a testing step
        with open("users.json","w") as file:
            json.dump(users, file)  # we "dump" the users in the dictionary (or list?) to the .json file
                                    # it will overwrite the last dictionary but not "wipe" the content. (you can see the updated .json file)
        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen): # it inherits from 'screen'

    def back_to_login(self):
        self.manager.transition.direction = 'right' # to change the transition direction from teh left to the right.
        self.manager.current = "login_screen" # it goes to the name in teh RootWidget, NOT the class in the Python code

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feel):  # we can call this input whatever we want; it isn't literally 'feeling' from the kivy file
        feel = feel.lower()
        # print(feel)
        available_feelings = glob.glob("quotes/*txt")        # the 'glob' module :)

        # now, we'd like to just pul out the available stem names using a list comprehension
        # not sure why we want to do this ...
        available_feelings = [Path(filename).stem for filename in 
                                available_feelings]  # in square brackets, these can be split.
        # print(available_feelings) test it through the terminal 
        if feel in available_feelings:
            with open (f"quotes/{feel}.txt") as file:    # open the suitable file containing that feeling in the name.
                quotes = file.readlines()  # this will produce a list of all the quotes
            print(quotes)

class MainApp(App):   # the app object you haven't used yet (inherits from App above). It is the highest in the heirarchy.
    def build(self): # def build is from App.
        return RootWidget() # make sure it's the object and not the class (the brackets () initialize it.)

if __name__ == "__main__":
    MainApp().run() # this creates an instance of the Main App and applies its run() method.


# note about json:
# shift-alt-f to "prettify". Amazing.
# downside to json--it doesn't support comments.
