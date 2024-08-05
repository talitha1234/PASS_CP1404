"""Invader class - PASS"""
from alien import Alien


class Invader(Alien):
    """Specialized version of Alien."""

    def __init__(self, alien_type, health, color="white"):  # can also use **kwargs
        """Initialize an Invader type alien. It has an extra variable called color."""
        super().__init__(alien_type, health)
        self.color = color

    def __str__(self):
        """Return a string representation:
       'Type: {self.alien_type} - Health: {self.health} : COLOR - {self.color}'
       This looks similar to the parent's string... maybe we can use that? Remember no DRY here!"""
        return f"{super().__str__()} : COLOR - {self.color}"
