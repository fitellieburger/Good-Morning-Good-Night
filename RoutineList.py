
# Screens and layout
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

# Lists
from kivymd.uix.list import MDList, OneLineListItem, OneLineIconListItem, IconLeftWidget
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recyclelayout import RecycleLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.scrollview import ScrollView

# Buttons
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton


class RoutineList(RecycleLayout):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.data = []
        for i in range(5):
            self.data.append({'text': f'Item {i}', 'image': 'path/to/image'})

        self.viewclass = 'RoutineListItem'
        self.layout = BoxLayout(orientation='vertical', size_hint=(.8, 0.66), height=.5)
        self.item_strings = [{'text': d['text'], 'image': d['image']} for d in self.data]

class RoutineListItem(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.image = Image(source=kwargs['data']['image'])
        self.label = Label(text=kwargs['data']['text'])
        #self.add_widget(self.image)
        self.add_widget(self.label)
        #self.add_widget(Button(text='Button'))



