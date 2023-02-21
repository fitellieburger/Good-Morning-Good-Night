"""
GoodRoutines Screens and Navigation
Screen navigation - built with support from chatGPT, Feb 20 version

"""

# Custom
from RoutineList import *
from listModule import _getRoutine
from listModule import _fetchStickers
from listModule import _buildList
from listModule import _setPhrases

# required for the app
from kivymd.app import MDApp

# Screens and layout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager

# Labels and Text
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.text import LabelBase


# Buttons
from kivy.uix.button import Button


"""

App Class

"""


# create the app
class GoodApp(MDApp):

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
        sm = MyScreenManager()

        return sm


"""

Screen Manager Class

"""


class MyScreenManager(ScreenManager):

    # Screens
    routine = None
    greeting = None
    done = None

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)

        # screens
        self.greeting = GreetingScreen(name='greeting')
        self.routine = RoutineScreen(name='routine')
        self.done = DoneScreen(name='done')

        # add screens
        self.add_widget(self.greeting)
        self.add_widget(self.routine)
        self.add_widget(self.done)

##
# Getters
##

    def get_pause(self):
        return self.pause

    def get_routine(self):
        return self.routine

    def get_done(self):
        return self.done

##
# Re-Setters
##

    # resets the greeting screen
    def create_newGreeting(self, **kwargs):

        if self.greeting is not None:
            self.remove_widget(self.greeting)

        self.greeting = GreetingScreen(**kwargs)
        self.add_widget(self.greeting)

    def remove_greeting(self):
        if self.greeting is not None:
            self.remove_widget(self.greeting)
            self.greeting = None

    # resets the routine list
    def create_newRoutine(self, **kwargs):

        if self.routine is not None:
            self.remove_widget(self.routine)

        self.routine = RoutineScreen(**kwargs)
        self.add_widget(self.routine)

    def remove_routine(self):
        if self.routine is not None:
            self.remove_widget(self.routine)
            self.routine = None

    # resets the Done Screen
    def create_newDone(self, **kwargs):

        if self.done is not None:
            self.remove_widget(self.done)

        self.done = DoneScreen(**kwargs)
        self.add_widget(self.done)

    def remove_done(self):
        if self.done is not None:
            self.remove_widget(self.done)
            self.done = None


"""

Screen on app open

"""


class GreetingScreen(Screen):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        # set layout
        layout = FloatLayout()

        routineSet = _getRoutine()

        # screen title
        title = Label(text=routineSet["Title"], font_name="TitleFont",
                      font_size='40sp', size_hint=(.3, .3),
                      pos_hint={'center_x': 0.5, 'y': 0.7})

        # method to open checklist on button press
        def start(obj):
            self.manager.current = 'routine'

        # button to start new routine
        btnStart = Button(background_normal=routineSet["rightButton"],
                          text="Let's Go!", font_name="ButtonFont",
                          size_hint_x=None, width=200,
                          size_hint_y=None, height=50,
                          pos_hint={'center_x': 0.5, 'y': 0.15},
                          on_press=start)

        # add widget - image, title, and button(s)
        layout.add_widget(Image(source=routineSet["Background"],
                                allow_stretch=True, keep_ratio=False))
        layout.add_widget(title)
        layout.add_widget(btnStart)

        # add layout
        self.add_widget(layout)


"""

Screen with routine list - user can check off tasks as accomplished and receive a sticker

"""


class RoutineScreen(Screen):

    __allPhraseList = ["animal", "good", "pun", "nature", "space", "magic", "dino", "food", "other", "sport"]
                                        # all phrases used in the sticker directory
    listDirectory = "newStickers"          # directory where phrases can be found
    numImages = 5                       # number of tasks in a routine

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        # get task list
        routineSet = _getRoutine()

        self.numImages = routineSet["numberTasks"]

        # assign list
        stickers = self._getNewStickers(self.listDirectory)

        # set layout for screen
        layout = FloatLayout()

        # screen title
        title = Label(text=routineSet["Title"], font_name="TitleFont",
                      font_size='40sp', size_hint=(.3, .3),
                      pos_hint={'center_x': 0.5, 'y': 0.7})

        # item list widgets in middle
        tasks = []
        yAxis = .65

        for i in range(self.numImages):

            currentTask = "task" + str(i+1)

            # 4 arguments : line image, line title, checkbox image, and sticker image list
            tasks.append(RoutineItem(routineSet[currentTask]["image"], routineSet[currentTask]["Title"],
                            "images/checkbox.png", stickers[i],
                            size_hint=(.25, None), height=50,
                            pos_hint={'center_x': 0.5, 'y': yAxis}))
            # adjust next list item so it appears lower on screen
            yAxis = yAxis - .1

        # method to return to greeting screen
        def greeting(obj):
            self.manager.current = 'greeting'

        # method for button to complete routine
        def done(obj):
            self.manager.current = 'done'

        # buttons to finish and return
        btnDone = Button(background_normal=routineSet["rightButton"],
                        text="Done!",
                        font_name="ButtonFont",
                        size_hint_x=None, width=200,
                        size_hint_y=None, height=50,
                        pos_hint={'center_x': 0.5, 'y': 0.15},
                        on_press=done)
        btnPause = Button(background_normal=routineSet["leftButton"],
                          text="Pause",
                          font_name="ButtonFont",
                          size_hint_x=None, width=200,
                        size_hint_y=None, height=50,
                        pos_hint={'center_x': 0.5, 'y': 0.05},
                        on_press=greeting)

        # add all widgets
        layout.add_widget(Image(source=routineSet["Background"],
                                allow_stretch=True, keep_ratio=False))
        layout.add_widget(title)

        for j in range(len(tasks)):
            layout.add_widget(tasks[j])

        layout.add_widget(btnDone)
        layout.add_widget(btnPause)

        # add layout
        self.add_widget(layout)

    # When the done screen is opened, create a new routine for the next iteration
    def on_enter(self):

        if self.manager.get_done() is not None:
            self.manager.remove_done()
        self.manager.create_newDone(name='done')

    def _getNewStickers(self, directory):

        # build list of images in a directory
        imageList = _buildList(directory)

        # build list of phrases
        phraseList = _setPhrases(self.__allPhraseList, self.numImages)

        # returns list of images matching phrases
        return _fetchStickers(directory, imageList, phraseList, self.numImages)


"""

Screen with summary of completed routine

"""


class DoneScreen(Screen):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        layout = FloatLayout()

        routineSet = _getRoutine()

        # screen title
        title = Label(text=routineSet["Title"], font_name="TitleFont",
                      font_size='40sp', size_hint=(.3, .3),
                      pos_hint={'center_x': 0.5, 'y': 0.7})

        # big sticker
        sticker = self._getSticker()[0]
        reward = Image(source=sticker,
                       size_hint_x=None, width=450, size_hint_y=None,
                       height=450, pos_hint={'center_x': .5, 'center_y': .65})

        # Congrats text
        congrats = Label(text='Great Job\nOn Your Routine!',
                         font_name="ItemFont",
                         font_size='60sp', halign='center',
                         size_hint=(.3, .3),
                         pos_hint={'center_x': 0.5, 'center_y': 0.4})

        # method to change screen on press
        def finish(screen):

            self.manager.current = 'greeting'

        # button
        btn_flat = Button(background_normal=routineSet["rightButton"],
                        text="Yay!", font_name="ButtonFont",
                        size_hint_x=None, width=200,
                        size_hint_y=None, height=50,
                        pos_hint={'center_x': 0.5, 'y': 0.15},
                        on_press=finish)

        # add widgets to layout
        layout.add_widget(Image(source=routineSet["Background"],
                                allow_stretch=True, keep_ratio=False))
        layout.add_widget(title)
        layout.add_widget(reward)
        layout.add_widget(congrats)
        layout.add_widget(btn_flat)

        # add layout
        self.add_widget(layout)

    # When the done screen is opened, create a new routine for the next iteration
    def on_enter(self):

        if self.manager.get_routine() is not None:
            self.manager.remove_routine()
        self.manager.create_newRoutine(name='routine')

    # Retrieve sticker for award screen
    def _getSticker(self):
        sticker = _fetchStickers("stickers", _buildList("stickers"), ["good"], 1)

        return sticker
