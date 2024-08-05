"""Boss class - PASS"""
from alien import Alien


class Boss(Alien):
    """Specialized version of alien - Boss."""

    def __init__(self, alien_type, health, shield=10):
        """Initialize a Boss type alien. It has an extra variable called shield."""
        super().__init__(alien_type, health)
        self.shield = shield

    def __str__(self):
        """Return a string representation if it has a shield:
       'Type: {self.alien_type} - Health: {self.health}. SHIELD {self.shield}'
       Or return the parent's string if there is no shield."""
        if self.shield > 0:
            message = f"{super().__str__()}: SHIELD {self.shield}"
        else:
            message = super().__str__()
        return message

    def attack(self, damage):
        """Attack the boss and knock down its health once it has no shield. Remember, no DRY here!"""
        if self.shield > 0:
            self.shield -= damage
            print(f"You knocked down the {self.alien_type}'s shield to {self.shield}")
        else:
            super().attack(damage)
