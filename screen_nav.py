
# Custom
from RoutineList import *

# Screens and layout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivymd.uix.dialog import MDDialog
from kivy.uix.layout import Layout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import Screen


# Labels and Text
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField


# Buttons
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton

class GreetingScreen(Screen):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        # screen title
        title = Label(text='Good Night', font_size='40sp',
                        size_hint=(1.0, 0.1), pos_hint={'top': 0.9, 'center_x': 0.5})

        def start(obj):
            self.manager.current = 'routine'

        btn_flat = MDRectangleFlatButton(text="Start",
                                         pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                         on_press=start)
        self.add_widget(title)
        self.add_widget(btn_flat)


class RoutineScreen(Screen):
     def __init__(self, **kwargs):

        super().__init__(**kwargs)

        # set layout for screen
        layout = BoxLayout(orientation='vertical')

        # screen title
        title = Label(text='Good Night', font_size='40sp',
                        size_hint=(1.0, 0.1), pos_hint={'top': 0.9, 'center_x': 0.5})

        # list widget in middle
        self.routines = RoutineList()

        # method for button return
        def done(obj):
            self.manager.current = 'done'

        # buttons to finish and return
        btn_flat = MDRectangleFlatButton(text="Done!",
                                         pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                         on_press=done)

        # add widgets
        layout.add_widget(title)
        layout.add_widget(self.routines)
        layout.add_widget(btn_flat)

        self.add_widget(layout)

class DoneScreen(Screen):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        # screen title
        title = Label(text='Good Night', font_size='40sp',
                        size_hint=(1.0, 0.1), pos_hint={'top': 0.9, 'center_x': 0.5})

        def finish(obj):
            self.manager.current = 'greeting'

        btn_flat = MDRectangleFlatButton(text="Yay!",
                                         pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                         on_press=finish)
        self.add_widget(title)
        self.add_widget(btn_flat)
