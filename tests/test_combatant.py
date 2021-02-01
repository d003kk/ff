import unittest
import combatant
from unittest.mock import patch, call

class TestCombatant(unittest.TestCase):

    def test_init(self):
        skill = 10
        stamina = 10
        c = combatant.combatant(stamina=stamina, skill=skill)
        self.assertEqual(stamina, c.stamina)
        self.assertEqual(skill, c.skill)

    def test_dead(self):
        skill = 10
        stamina = 10
        c = combatant.combatant(stamina=stamina, skill=skill)
        self.assertFalse(c.dead())
        c.stamina = 0
        self.assertTrue(c.dead())
        c.stamina = -2
        self.assertTrue(c.dead())

    @patch('combatant.dice.twodie')
    def test_combat(self, mock_twodie):
        skill = 10
        stamina = 10
        c = combatant.combatant(stamina=stamina, skill=skill)
        mock_twodie.side_effect = [2]
        combatroll = c.combat_roll()
        self.assertEqual(12, combatroll)

    def test_damage(self):
        skill = 10
        stamina = 10
        damage = 2
        c = combatant.combatant(stamina=stamina, skill=skill)
        c.takedamage(2)
        self.assertEqual(c.stamina, stamina - damage)

