import play



myplayer = play.player()
myplayer.gen_stat()

potions=["Stamina", "Skill", "Strength"]
print("Choose one adventurer potion")
for i, f in enumerate(potions, start=1):
    option = "For {0} press {1}".format(f, i)
    print(option)
myplayer.potion = potions[int(input("Enter (1-3)"))]
myplayer.print_player()


