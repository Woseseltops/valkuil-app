import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color

from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
import random

from kivy.uix.screenmanager import ScreenManager, Screen

class Input_screen(Screen):
    pass;

class Output_screen(Screen):

    def change_error(self):
#        self.mistake_text.text = 'hoi'
        self.mistake_box.mistake_text.text = 'Nieuwe fout'

class ValkuilApp(App):

    def build(self):
        sm = ScreenManager()
        i = Input_screen(name='input');
        o = Output_screen(name='output');
        sm.add_widget(i)
        sm.add_widget(o)

#        self.input_screen = Input_screen()
#        self.input_screen.ok_button.bind(on_press=self.switch_screen)

        return sm

if __name__ == '__main__':
    ValkuilApp().run()
