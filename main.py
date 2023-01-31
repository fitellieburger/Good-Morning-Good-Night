# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# required for app building
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang.builder import Builder

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

# Lists
from kivymd.uix.list import MDList, OneLineListItem, OneLineIconListItem, IconLeftWidget
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.scrollview import ScrollView

# custom
from helpers import task1_helper
from screen_nav import *


# create the app
class GoodApp(MDApp):
    def build(self):
        # theme customization
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style = "Dark"

        sm = ScreenManager()

        sm.add_widget(GreetingScreen(name='greeting'))
        sm.add_widget(RoutineScreen(name='routine'))
        sm.add_widget(DoneScreen(name='done'))



        # task1 = MDTextField(text='First Thing',
        #                   pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                  size_hint_x=None, width=300)
        # self.task1 = Builder.load_string(task1_helper)


        #screen.add_widget(btn_flat)
        # label = MDLabel(text='Hello World', halign='center')
        # screen = Builder.load_string(screen_helper)
        return sm

    # create the interaction(s)
    def show_data(self, obj):
        if self.task1.text is "":
            check_string = "You didn't type anything!"
        else:
            check_string = "Let's " + self.task1.text + " today!"
        close_button = MDFlatButton(text='Yay!', on_release=self.close_dialog)
        more_button = MDFlatButton(text='Again!')
        self.dialog = MDDialog(title="New task!", text=check_string,
                               size_hint=(0.7, 1),
                               buttons=[close_button, more_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()





# build the interactions

# run app
GoodApp().run()
