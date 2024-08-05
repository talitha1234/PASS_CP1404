"""
Build an app that creates buttons for each item in a list. Create each button dynamically.
When a button is pressed, a label updates to display which button was pressed.
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

class MoreButtons(App):
    def __init__(self, **kwargs):
        """Initialize the app and the list of items."""
        # call the parent class's initializer in a way that passes any additional keyword arguments (**kwargs)
        super().__init__(**kwargs)
        self.items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

    def build(self):
        """Build the Kivy GUI from the kivy file 'MoreButtons.kv' and create buttons."""

    def create_buttons(self):
        """Create buttons for each item and add them to the layout."""

    def press_item(self, button):
        """Update the label with the button's text when pressed."""


if __name__ == '__main__':
    MoreButtons().run()
