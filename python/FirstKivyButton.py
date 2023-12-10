from kivy.app import App
from kivy.uix.button import Button
from functools import partial

class FirstKivy(App):
    def disable(self, instance, *args):
        instance.disabled = True
    def update(self, instance, *args):
        instance.text = "I am Disabled!"
        instance.background_color = (0,0,255,100)
        instance.pos = (0,0)
        instance.size_hint = (1,1)
    def build(self):
        mybtn = Button(text = "Click me to disable", background_color = (0,255,0,100), pos = (300,350), size_hint = (.25,.18))
        mybtn.bind(on_press = partial(self.disable, mybtn))
        mybtn.bind(on_press = partial(self.update, mybtn))
        return mybtn

FirstKivy().run()