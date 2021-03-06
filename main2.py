# python3 version 3.7.9
# pip3 version 20.1.1
# interpreter python 3.7
# kivy => pip install kivy
# kivyMD => pip install kivy
# run

import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from explore import explore_KV

kivy.require("2.0.0")

# bottom navigation
screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            halign: 'center'
            title: 'Chatty'
            md_bg_color: .2, .2, .2, 1
            specific_text_color: 1, 1, 1, 1
            
        MDBottomNavigation:
            panel_color: .2, .2, .2, 1
            
            MDBottomNavigationItem:
                id: explore
                name: 'screen 1'
                text: 'explore'
    
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'chat'
                MDLabel:
                    text: 'Chat'
                    halign: 'center'
    
            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'profile'
                MDLabel:
                    text: 'profile'
                    halign: 'center'

"""


class Chatty(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)

        # to fill in the explore screen
        explore = Builder.load_string(explore_KV)
        for i in range(20):
            userbox = UserBox()
            userbox.ids.username.text = f'username {i}'
            explore.ids.layout.add_widget(userbox)

        screen.ids.explore.add_widget(explore)

        return screen


if __name__ == '__main__':
    Chatty().run()
