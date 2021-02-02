"""Container play class """
import dice
import combatant

class Player(combatant.Combatant):
    """ The actual player of the game"""

    BASE_STAMINA = 6
    BASE_SKILL = 12
    BASE_LUCK = 6

    def __init__(self, potion=None, skill=0, stamina=0, luck=0, equipment=None, gold=0):
        """initialize player instance"""
        self.gold = gold
        self.potion = potion
        self.luck = luck
        self.equipment = equipment
        super(Player, self).__init__(stamina=stamina, skill=skill)

    def gen_stat(self):
        """Randomly generate stats"""
        self.skill = Player.BASE_SKILL + dice.onedie()
        self.stamina = Player.BASE_STAMINA + dice.onedie()
        self.luck = Player.BASE_LUCK + dice.onedie()

    def test_luck(self):
        """Test luck against two dice"""
        passed = dice.twodie() <= self.luck
        self.luck = self.luck -1
        return passed

    def flee(self, try_luck=False):
        """Flee with optional luck test"""
        decrement = 2
        if try_luck and self.test_luck():
            decrement = 1
        self.stamina = self.stamina - decrement

    def print_player(self):
        """Print all stats and loot"""
        print("Gold: ", self.gold)
        print("Potion: ", self.potion)
        print("Skill: ", self.skill)
        print("Stamina: ", self.stamina)
        print("Luck: ", self.luck)
        print("Equipment: ", self.equipment)
