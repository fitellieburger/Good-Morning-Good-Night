"""
Screen navigation - built with support from chatGPT, Jan xx version
                                (where xx is the date when each snippet of code was developed)

"""

# Screens and layout
import os
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

# Labels and Text
from kivy.uix.label import Label

# Images
from kivy.uix.image import Image

# Buttons
from kivy.uix.button import Button





class RoutineItem(BoxLayout):
    def __init__(self, left_image_source, label_text, right_image_source, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.spacing = 10

        # Center the layout

        self.size_hint_x = .3

        # Add left image
        self.left_image = Image(source=left_image_source, size_hint_x=None, width=50, size_hint_y=None, height=50)
        self.add_widget(self.left_image)

        # Add label
        self.label = Label(text=label_text, font_name="ItemFont",
                           size_hint_x=None, size_hint_y=None, width=100, height=50, text_size=(None, None),
                           halign='center')
        self.add_widget(self.label)

        # Add right image
        self.right_button = Button(background_normal=right_image_source, size_hint_x=None, width=50,
                                   size_hint_y=None, height=50)
        self.right_button.bind(on_press=self.update_right_image)
        self.add_widget(self.right_button)


    def update_right_image(self, instance):
        # Update the source of the right image
        if self.right_button.background_normal == "images/checkbox.png":
            self.right_button.background_normal = "images/checked.png"

        else:
            self.right_button.background_normal = "images/checkbox.png"

    def _update_size(self, instance, value):
        instance.height = 50
        instance.width = self.parent.width

    def _update_pos(self, instance, value):
        instance.x = self.parent.x
        instance.y = self.parent.y + (self.parent.height - instance.height) / 2

