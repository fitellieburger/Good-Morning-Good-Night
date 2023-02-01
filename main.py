"""
Main App for Good Routines
by Elle Burger

Code structure inspired by Attreya Bhatt
at https://github.com/attreyabhatt/KivyMD-Basics
last updated Jul 7, 2020

"""

# required for app building
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang.builder import Builder

# Screens and layout
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen, ScreenManager

# Labels and Text
from kivy.core.text import LabelBase

# Buttons
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton

# Custom
from screen_nav import *


# create the app
class GoodApp(MDApp):

    # variables to make the app work
    checkedCount = 0

    def build(self):
        # theme customization
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style = "Dark"

        # fonts
        LabelBase.register(name="TitleFont", fn_regular="fonts/Strawberry Cheesecake.otf")
        LabelBase.register(name="ItemFont", fn_regular="fonts/TommySoftBlack.otf")
        LabelBase.register(name="ButtonFont", fn_regular="fonts/TommySoftBold.otf")

        # screen management
        sm = ScreenManager()

        sm.add_widget(GreetingScreen(name='greeting'))
        sm.add_widget(RoutineScreen(name='routine'))
        sm.add_widget(DoneScreen(name='done'))

        return sm

# run app
GoodApp().run()
