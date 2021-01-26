import unittest
import play
from unittest.mock import patch, call


class TestStringMethods(unittest.TestCase):

    def test_init(self):
        initialPotion = "blah"
        initialSkill = 10
        initialStamina = 10
        initialLuck = 10
        initialEquipment = ["fire ring", "shield"]
        myplayer = play.player(potion=initialPotion, skill=initialSkill, stamina=initialStamina, equipment=initialEquipment, luck=initialLuck)
        self.assertEqual(myplayer.potion, initialPotion)
        self.assertEqual(myplayer.skill, initialSkill)
        self.assertEqual(myplayer.stamina, initialStamina)
        self.assertEqual(myplayer.luck, initialLuck)
        self.assertEqual(myplayer.equipment, initialEquipment)

    @patch('builtins.print')
    def test_player_print(self, mocked_print):
        initialPotion = "blah"
        initialSkill = 10
        initialStamina = 10
        initialLuck = 10
        initialEquipment = ["fire ring", "shield"]
        myplayer = play.player(potion=initialPotion, skill=initialSkill, stamina=initialStamina, equipment=initialEquipment)
        myplayer.print_player();
        assert mocked_print.mock_calls == [call('Potion: ', 'blah')]

if __name__ == '__main__':
    unittest.main()
