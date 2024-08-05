"""Simple Button App"""
# TODO: Add code to make the button change colour when you press it

from kivy.app import App
from kivy.lang import Builder


class Button(App):
    def build(self):
        self.root = Builder.load_file('Button.kv')
        return self.root

    def on_button_press(self, button_instance):
        """Change colour on button press."""
        button_instance.background_color = 'green'  # New color when pressed

    def on_button_release(self, button_instance):
        """Change back to original colour on button press"""
        button_instance.background_color = "red"

Button().run()
