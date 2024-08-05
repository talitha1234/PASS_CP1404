"""Boss class - PASS"""
from alien import Alien


class Boss(Alien):
   """Specialized version of alien - Boss."""

   def __init__(self):
       """Initialize a Boss type alien. It has an extra variable called shield."""
       #start coding here

   def __str__(self):
       """Return a string representation if it has a shield:
       'Type: {self.alien_type} - Health: {self.health}. SHIELD {self.shield}'
       Or return the base class string if there is no shield."""
       #start coding here

   def attack(self, damage):
       """Attack the boss and knock down its health once it has no shield. Remember, no DRY here! The base class
       already handles the health..."""
       #start coding here
