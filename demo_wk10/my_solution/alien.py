"""An alien class - PASS"""


class Alien:
    """Represents an alien invader."""

    def __init__(self, alien_type, health):
        """Initialize an alien instance. An alien has a name and health."""
        self.alien_type = alien_type
        self.health = health

    def __str__(self):
        """Return an alien in the form of: 'Type: {alien_type} - Health: {alien_health}."""
        return f"Type: {self.alien_type} - Health: {self.health}"

    def attack(self, damage):
        """Attack the alien to reduce its health.
       If its health is greater than 0, output:
       'You damaged the {alien_type} for {damage} damage!
       Current HP {health}'
       If the alien runs out of health, output:
       'The {alien_type has been defeated!}"""
        if self.health > 0:
            self.health -= damage
            print(f"You damaged the {self.alien_type} for {damage} damage!")
            print(f"Current HP {self.health}")
        if self.health <= 0:
            print(f"The {self.alien_type} has been defeated!")
