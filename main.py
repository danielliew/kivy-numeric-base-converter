import binaryconverter.main
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App
import kivy
import binaryconverter.main as script
kivy.require('2.0.0')


Builder.load_file("components.kv")


class Main(BoxLayout):

    def compute(self):
        err = False

        for x in self.ids:
            if 'input' in x:
                req = self.ids[x].text
                if len(req) > 0:
                    try:
                        name = x.replace('input_', '')
                        func = getattr(script, name)
                        self.ids['label_' +
                                 name].text = str(func(req))
                    except:
                        err = True
        if (err):
            Popup(title='Warning!', content=Label(
                text='Errors detected'), size_hint=(.3, .3)).open()

    def clear(self):
        for x in self.ids:
            self.ids[x].text = ''


class App(App):

    def build(self):
        return Main()


if __name__ == '__main__':
    App().run()
