import unittest
import play
from unittest.mock import patch, call


class TestPlayer(unittest.TestCase):

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
        initialGold = 100
        initialStamina = 10
        initialLuck = 10
        initialEquipment = ["fire ring", "shield"]
        myplayer = play.player(gold=initialGold, potion=initialPotion, skill=initialSkill, stamina=initialStamina, equipment=initialEquipment, luck=initialLuck)
        myplayer.print_player()
        assert mocked_print.mock_calls == [call("Gold: ", initialGold) ,
                call("Potion: ", initialPotion) ,
                call("Skill: ", initialSkill) ,
                call("Stamina: ", initialStamina) ,
                call("Luck: ", initialLuck) ,call("Equipment: ", initialEquipment) ]

    @patch('play.dice.onedie')
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

    @patch('play.dice.twodie')
    def test_luck(self, mocked_twodie):
        initialPotion = "blah"
        initialSkill = 10
        initialStamina = 10
        initialLuck = 10
        initialEquipment = ["fire ring", "shield"]
        myplayer = play.player(potion=initialPotion, skill=initialSkill, stamina=initialStamina, equipment=initialEquipment, luck=initialLuck)
        mocked_twodie.side_effect = [6, 12]
        lucky = myplayer.test_luck()
        self.assertTrue(lucky)
        self.assertEqual(myplayer.luck, initialLuck -1)
        lucky = myplayer.test_luck()
        self.assertFalse(lucky)
        self.assertEqual(myplayer.luck, initialLuck -2)

    @patch('play.dice.twodie')
    def test_luck(self, mocked_twodie):
        initialPotion = "blah"
        initialSkill = 10
        initialStamina = 10
        initialLuck = 10
        initialEquipment = ["fire ring", "shield"]
        myplayer = play.player(potion=initialPotion, skill=initialSkill, stamina=initialStamina, equipment=initialEquipment, luck=initialLuck)
        mocked_twodie.side_effect = [6, 12]
        # Passes luck test
        myplayer.flee(tryLuck=True)
        self.assertEqual(myplayer.stamina, initialStamina -1)
        # Fails luck test
        myplayer.flee(tryLuck=True)
        self.assertEqual(myplayer.stamina, initialStamina -3 )
        # Dont use luck
        myplayer.flee()
        self.assertEqual(myplayer.stamina, initialStamina -5 )


if __name__ == '__main__':
    unittest.main()
