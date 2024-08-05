from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class MoreButtons(App):
    def __init__(self, **kwargs):
        """Initialize the app and the list of items."""
        super().__init__(**kwargs)
        self.items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

    def build(self):
        """Build the Kivy GUI from the kivy file 'MoreButtons.kv' and create buttons."""
        self.root = Builder.load_file('MoreButtons.kv')
        self.create_buttons()
        return self.root

    def create_buttons(self):
        """Create buttons for each item and add them to the layout."""
        for item in self.items:
            # Create a new Button widget with the text set to the current item
            temp_button = Button(text=item)
            # Bind the button's on_release event to the press_item method
            temp_button.bind(on_release=self.press_item)
            # Add the button widget to the layout with the id 'button_box'
            self.root.ids.button_box.add_widget(temp_button)

    def press_item(self, instance):
        """Update the label with the button's text when pressed."""
        self.root.ids.info_label.text = f"Button pressed: {instance.text}"


if __name__ == '__main__':
    MoreButtons().run()
