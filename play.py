class player:
    def __init__(self, potion=None, skill=0, stamina=0, luck=0, equipment=[]):
                self.potion = potion
                self.skill = skill
                self.stamina = stamina
                self.luck = luck
                self.equipment = equipment
    def print_player(self):
        print("Potion: ", self.potion)
        print("Skill: ", self.skill)
        print("Stamina: ", self.stamina)
        print("Luck: ", self.luck)
        print("Equipment: ", self.equipment)

