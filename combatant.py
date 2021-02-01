"""This module contains the Combatant class."""
import dice

class Combatant(object):

    """Combatants are capable of combat."""

    def __init__(self, stamina=0, skill=0):
        """ Initialize Combatant."""
        self.stamina = stamina
        self.skill = skill

    def combat_roll(self):
        """Roll a combat score."""
        return dice.twodie() + self.skill

    def dead(self):
        """Test is combatant dead."""
        return self.stamina <= 0

    def takedamage(self, damage):
        """Combatant subtracts damage from stamina."""
        self.stamina = self.stamina - damage
