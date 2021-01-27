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
        myplayer = play.player(potion=initialPotion, skill=initialSkill, stamina=initialStamina, equipment=initialEquipment, luck=initialLuck)
        myplayer.print_player()
        assert mocked_print.mock_calls == [call("Potion: ", initialPotion) ,
                call("Skill: ", initialSkill) ,
                call("Stamina: ", initialStamina) ,
                call("Luck: ", initialLuck) ,call("Equipment: ", initialEquipment) ]

    @patch('play.onedie')
    def test_gen_stat(self, mocked_ondie):
        mocked_luck = 1
        mocked_stamina = 1
        mocked_skill = 1
        mocked_ondie.side_effect = [mocked_luck, mocked_stamina, mocked_skill]
        myplayer = play.player()
        myplayer.gen_stat()
        self.assertEqual(myplayer.skill, play.player.BASE_SKILL + mocked_skill)
        self.assertEqual(myplayer.stamina, play.player.BASE_STAMINA + mocked_stamina)
        self.assertEqual(myplayer.luck, play.player.BASE_LUCK + mocked_luck)

if __name__ == '__main__':
    unittest.main()
