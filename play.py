import random

def onedie():
    return random.randrange(1, 6, 1)



class player:
    BASE_STAMINA = 6
    BASE_SKILL = 6
    BASE_LUCK = 6
    def __init__(self, potion=None, skill=0, stamina=0, luck=0, equipment=[]):
                self.potion = potion
                self.skill = skill
                self.stamina = stamina
                self.luck = luck
                self.equipment = equipment
    def gen_stat(self):
                self.skill = player.BASE_SKILL + onedie()
                self.stamina =  player.BASE_STAMINA + onedie()
                self.luck = player.BASE_LUCK + onedie()
        
    def print_player(self):
        print("Potion: ", self.potion)
        print("Skill: ", self.skill)
        print("Stamina: ", self.stamina)
        print("Luck: ", self.luck)
        print("Equipment: ", self.equipment)

