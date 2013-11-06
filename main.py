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

from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import random

class Input_screen(GridLayout):
    pass;

class Output_screen(Widget):
    pass;

def hoi(a):
    print('hoi')

class ValkuilApp(App):

    def build(self):
        input_screen = Input_screen();
        input_screen.ok_button.bind(on_press=hoi)

        return input_screen

if __name__ == '__main__':
    ValkuilApp().run();
