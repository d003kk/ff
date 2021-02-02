import play
import combatant

myplayer = play.Player()
myplayer.gen_stat()

potions=["Stamina", "Skill", "Strength"]
print("Choose one adventurer potion")
for i, f in enumerate(potions, start=1):
    option = f"For {f} press {i}"
    print(option)
myplayer.potion = potions[int(input("Enter (1-3)"))]
myplayer.print_player()

c1 = combatant.Combatant(3,3, "Goblin")
c2 = combatant.Combatant(4,4, "Troll")
combatants = [c1, c2]

while(1):
    for c in combatants:
        if c.dead():
            continue

        if c.combat_roll() > myplayer.combat_roll():
            print("Player damage")
            myplayer.takedamage(2)
        else:
            print("c damage")
            c.takedamage(2)
            print("c stamina", c.stamina)

        if myplayer.dead():
            print("Player is dead")
        if c.dead():
            print("Combatant is dead: ", c.name)

    if c1.dead() and c2.dead():
        print("All combatants dead")
        break





