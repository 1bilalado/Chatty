# python3 version 3.7.9
# pip3 version 20.1.1
# interpreter python 3.7
# kivy => pip install kivy
# click run button

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
kivy.require("2.0.0")


class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text='IP:'))
        self.ip = TextInput(multiline=False)
        self.add_widget(self.ip)

        self.add_widget(Label(text='Port:'))
        self.port = TextInput(multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.join = Button(text='Join')
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button(self, instance):

        port = self.port.text
        ip = self.ip.text
        username = self.username.text

        # update terminal
        print(f'{ip}:{port} joining as {username}')

        # message to be displayed.
        info = f'{ip}:{port} joining as {username}'
        # tell the app to add the message to info page.
        chatty.info_page.update_info(info)
        # tell the app to move to required screen.
        chatty.screen_manager.current = "info"


class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1

        # specs of message to be displayed.
        self.message = Label(halign="center", valign="middle", font_size=20)

        # bind listens for and updates width of message to be added
        self.message.bind(width=self.update_text_width)
        # add message to info page.
        self.add_widget(self.message)

    # update the text for the label
    def update_info(self, message):
        self.message.text = message

    # update the width of the text for the label.
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.8, None)


class Chatty(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # step 1: instance of screenManger
        self.screen_manager = ScreenManager()
        # step 2: instance of pages to be added
        self.info_page = InfoPage()
        self.connect_page = ConnectPage()

    def build(self):
        # step 3: create and name screen instance accordingly
        screen = Screen(name='Connect')
        # step 4: add the page instance to the named screen
        screen.add_widget(self.connect_page)
        # step 5: add named screen to screen manager
        self.screen_manager.add_widget(screen)

        screen = Screen(name='info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        # step 6: return screen manager
        return self.screen_manager


if __name__ == '__main__':
    # chatty gives us access to apps instance.
    chatty = Chatty()
    chatty.run()
