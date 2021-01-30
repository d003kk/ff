import random

def onedie():
    return random.randrange(1, 6, 1)
def twodie():
    return ondie() + ondie()



class player:
    BASE_STAMINA = 6
    BASE_SKILL = 12
    BASE_LUCK = 6
    def __init__(self, potion=None, skill=0, stamina=0, luck=0, equipment=[], gold=0):
                self.gold = gold
                self.potion = potion
                self.skill = skill
                self.stamina = stamina
                self.luck = luck
                self.equipment = equipment
    def gen_stat(self):
                self.skill = player.BASE_SKILL + onedie()
                self.stamina =  player.BASE_STAMINA + onedie()
                self.luck = player.BASE_LUCK + onedie()
    def test_luck()
        passed =  towdie() <= self.luck
        self.luck = self.luck -1
        return passed
    def flee(tryLuck = False)
        decrement = 2
        if tryLuck and test_luck()
            decrement = 1
        self.stamina = self.stamina - decrement
        
    def print_player(self):
        print("Gold: ", self.gold)
        print("Potion: ", self.potion)
        print("Skill: ", self.skill)
        print("Stamina: ", self.stamina)
        print("Luck: ", self.luck)
        print("Equipment: ", self.equipment)

