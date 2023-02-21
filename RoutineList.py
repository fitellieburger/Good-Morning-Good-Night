"""
GoodRoutines Routine List Task Layout
- built with support from chatGPT, Fed 20 version

"""

# Screens and layout
import ast
import json

# Layout
from kivy.uix.boxlayout import BoxLayout

# Labels and Text
from kivy.uix.label import Label

# Images
from kivy.uix.image import Image

# Buttons
from kivy.uix.button import Button


class RoutineItem(BoxLayout):

    def __init__(self, left_image_source, label_text, right_image_source,
                 right_image_update_source, **kwargs):
        super().__init__(**kwargs)

        # create layout
        self.orientation = "horizontal"
        self.spacing = 10

        self.size_hint_x = .3

        # Add left image
        self.left_image = Image(source=left_image_source, size_hint_x=None,
                                width=50, size_hint_y=None, height=50)
        self.add_widget(self.left_image)

        # Add label
        self.label = Label(text=label_text, font_name="ItemFont",
                           size_hint_x=None, size_hint_y=None,
                           width=100, height=50, text_size=(None, None),
                           halign='center')
        self.add_widget(self.label)

        # Add right image
        self.right_button = Button(background_normal=right_image_source,
                                   size_hint_x=None, width=50,
                                   size_hint_y=None, height=50)
        self.right_button.bind(on_press=lambda instance: self.update_right_image(right_image_update_source))
        self.add_widget(self.right_button)

    """
    
    Setters
    
    """

    def update_right_image(self, update_source):

        update_image = Image(source=update_source, size_hint=(None, None),
                         size=(60, 60), allow_stretch=False)

        # Update the source of the right image
        # odd presses
        if self.right_button.background_normal == "images/checkbox.png":
            self.right_button.background_normal = update_image.source
            self.right_button.background_disabled_normal = update_image.source
            self.right_button.background_down = update_image.source
            self.right_button.size = update_image.size
        # even presses
        else:
            self.right_button.background_normal = "images/checkbox.png"
            self.right_button.background_disabled_normal = "images/checkbox.png"
            self.right_button.background_down = "images/checkbox.png"
            self.right_button.size = (50, 50)

    # updates line size based on parent screen
    def _update_size(self, instance, value):
        instance.height = 50
        instance.width = self.parent.width

    # updates position of line based on parent screen
    def _update_pos(self, instance, value):
        instance.x = self.parent.x
        instance.y = self.parent.y + (self.parent.height - instance.height) / 2

