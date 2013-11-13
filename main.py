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

from kivy.config import Config
Config.set('graphics', 'width', '475')
Config.set('graphics', 'height', '675')

class Input_screen(Screen):
    pass;

class Output_screen(Screen):

    found_errors = [('eigelijk','eigenlijk'),('onmiddelijk','onmiddellijk'),
        ('vind','vindt')]
    n = 0;

    def previous_error(self):
        if self.n > 0:
            self.n -= 1;

        self.update_error(self.n);

    def next_error(self):
        if self.n < len(self.found_errors) -1:
            self.n += 1;

        self.update_error(self.n);

    def update_error(self,error):
        self.mistake_box.mistake_text.text = self.found_errors[self.n][0];
        self.correction_box.correction_text.text = self.found_errors[self.n][1];

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
