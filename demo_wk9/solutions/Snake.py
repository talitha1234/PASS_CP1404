"""Snake.py"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class SnakeApp(App):
    """Main program."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.snake_to_info = {"Green Tree Snake": ["Green", "1m"],
                              "Brown Snake": ["Brown", "1.5m"],
                              "Taipan": ["Brown", "1"],
                              "Death Adder": ["Black", "2m"],
                              "Puff Adder": ["Yellow", "2.3m"],
                              "Incredibly Deadly Viper": ["Black", "12.7m"]}

    def build(self):
        """Build the Kivy GUI from the kivy file 'Snakes.kv' with the title 'Snakes' and then create the widgets."""
        self.root = Builder.load_file('Snakes.kv')
        self.title = "Snakes"
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from the snake_to_info dictionary entries and add them to the GUI."""
        for snake in self.snake_to_info:
            temp_button = Button(text=snake)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, button):
        """Handle pressing entry buttons. It will update the snake_info with 'The snake is a {NAME} which is {COLOR}
        in color and approximately {SIZE} in length'"""
        snake_name = button.text
        self.root.ids.snake_info.text = (f"The snake is a {snake_name} which is {self.snake_to_info[snake_name][0]} "
                                         f"in color and approximately {self.snake_to_info[snake_name][1]} in length ")


SnakeApp().run()
