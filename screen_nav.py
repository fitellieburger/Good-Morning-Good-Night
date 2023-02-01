"""
Screen navigation - built with support from chatGPT, Jan xx version
                                (where xx is the date when each snippet of code was developed)

"""

# Custom
from RoutineList import *

# Screens and layout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.screen import Screen


# Labels and Text
from kivy.uix.label import Label
from kivy.uix.image import Image

# Buttons
from kivy.uix.button import Button


class GreetingScreen(Screen):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        layout = FloatLayout()

        # screen title
        title = Label(text='Good Night', font_name="TitleFont",
                      font_size='40sp', size_hint=(.3,.3), pos_hint={'center_x': 0.5, 'y': 0.7})

        # method to open checklist on button press
        def start(obj):
            self.manager.current = 'routine'

        # button
        btn_flat = Button(background_normal="images/blueButtonRight.png", text="Start", font_name="ButtonFont",
                          size_hint_x=None, width=200,
                                   size_hint_y=None, height=50,
                                         pos_hint={'center_x': 0.5, 'y': 0.15},
                                         on_press=start)

        # add widgets
        layout.add_widget(Image(source="images/GoodNightBkgnd.png", allow_stretch=True, keep_ratio=False))
        layout.add_widget(title)
        layout.add_widget(btn_flat)

        # add layout
        self.add_widget(layout)


class RoutineScreen(Screen):
     def __init__(self, **kwargs):

        super().__init__(**kwargs)

        # set layout for screen
        layout = FloatLayout()

        # screen title
        title = Label(text='Good Night', font_name="TitleFont",
                      font_size='40sp', size_hint=(.3,.3), pos_hint={'center_x': 0.5, 'y': 0.7})

        # item list widgets in middle
        item1 = RoutineItem("images/potty.png", "Go Potty", "images/checkbox.png", size_hint=(.25, None), height=50,
                            pos_hint={'center_x': 0.5, 'y': 0.65})
        item2 = RoutineItem("images/toothbrush.png", "Brush Teeth", "images/checkbox.png", size_hint=(.25,None), height=50,
                            pos_hint={'center_x': 0.5, 'y': 0.55})
        item3 = RoutineItem("images/pjs.png", "PJs On", "images/checkbox.png", size_hint=(.25,None),height=50,
                            pos_hint={'center_x': 0.5, 'y': 0.45})
        item4 = RoutineItem("images/book.png", "Story Time", "images/checkbox.png", size_hint=(.25,None), height=50,
                            pos_hint={'center_x': 0.5, 'y': 0.35})
        item5 = RoutineItem("images/stars.png", "Off to Bed!", "images/checkbox.png", size_hint=(.25,None), height=50,
                            pos_hint={'center_x': 0.5, 'y': 0.25})

        # method for button to complete routine
        def done(obj):
            self.manager.current = 'done'

        # buttons to finish and return
        btn_flat = Button(background_normal="images/blueButtonRight.png",
                                         text="Done!", font_name="ButtonFont",
                                         size_hint_x=None, width=200,
                                         size_hint_y=None, height=50,
                                         pos_hint={'center_x': 0.5, 'y': 0.15},
                                         on_press=done)

        # add widgets
        layout.add_widget(Image(source="images/GoodNightBkgnd.png", allow_stretch=True, keep_ratio=False))
        layout.add_widget(title)

        layout.add_widget(item1)
        layout.add_widget(item2)
        layout.add_widget(item3)
        layout.add_widget(item4)
        layout.add_widget(item5)
        layout.add_widget(btn_flat)

        # add layout
        self.add_widget(layout)

class DoneScreen(Screen):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        layout = FloatLayout()

        # screen title
        title = Label(text='Good Night', font_name="TitleFont",
                      font_size='40sp', size_hint=(.3,.3), pos_hint={'center_x': 0.5, 'y': 0.7})

        # big sticker
        reward = Image(source="stickers/koalatyWork.png", size_hint_x=None, width=300, size_hint_y=None,
                       height=300, pos_hint={'center_x':.5, 'center_y':.65})

        # Congrats text
        congrats = Label(text='Great Job\nOn Your Routine!', font_name="ItemFont",
                      font_size='60sp', halign='center',
                      size_hint=(.3,.3), pos_hint={'center_x': 0.5, 'center_y': 0.4})

        # method to change screen on press
        def finish(obj):
            self.manager.current = 'greeting'

        # button
        btn_flat = Button(background_normal="images/blueButtonRight.png",
                                         text="Yay!", font_name="ButtonFont",
                                         size_hint_x=None, width=200,
                                         size_hint_y=None, height=50,
                                         pos_hint={'center_x': 0.5, 'y': 0.15},
                                         on_press=finish)

        # add widgets
        layout.add_widget(Image(source="images/GoodNightBkgnd.png", allow_stretch=True, keep_ratio=False))
        layout.add_widget(title)
        layout.add_widget(reward)
        layout.add_widget(congrats)
        layout.add_widget(btn_flat)

        # add layout
        self.add_widget(layout)
