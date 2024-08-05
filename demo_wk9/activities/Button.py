"""Simple Button App
Add methods to make the button change colour when you press it,
it should change back to original colour on release of button press.
Button is created in the kv file and colour is changed in this py file
"""

from kivy.app import App
from kivy.lang import Builder


class Button(App):
    def build(self):
        self.root = Builder.load_file('Button.kv')
        return self.root

    def on_button_press(self, button_instance):
        """Change colour on button press."""



    def on_button_release(self, button_instance):
        """Change back to original colour on button press"""



Button().run()
