"""
Create a program as seen on slides where each snake can be pressed to reveal its information in the
below label. Create each button dynamically using the following the dictionary:
{"Green Tree Snake": ["Green", "1m"],
                     "Brown Snake": ["Brown", "1.5m"],
                     "Taipan": ["Brown", "1"],
                     "Death Adder": ["Black", "2m"],
                     "Puff Adder": ["Yellow", "2.3m"],
                     "Incredibly Deadly Viper": ["Black", "12.7m"]}


"""


# Import statements


class SnakeApp(App):
    """Main program."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)

    def build(self):
        """Build the Kivy GUI from the kivy file 'Snakes.kv' with the title 'Snakes' and then create the widgets."""

    def create_widgets(self):
        """Create buttons from the snake_to_info dictionary entries and add them to the GUI."""
        # start coding here...

    def press_entry(self, button):
        """Handle pressing entry buttons. It will update the snake_info with 'The snake is a {NAME} which is {COLOR}
        in color and approximately {SIZE} in length'"""
        # start coding here...


SnakeApp().run()
