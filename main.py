from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class 

class MainWindowRight(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindowRight, self).__init__(**kwargs)

class MainWindowLeft(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindowLeft, self).__init__(**kwargs)

class MainWindow(Screen):
    pass

class SettingsWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class PompetteApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    PompetteApp().run()