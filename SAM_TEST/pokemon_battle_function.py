import random

def pokemon_battle(your_mon, opo_mon):
    while your_mon.health > 0 and opo_mon.health > 0:
        print("=" * 100)
        your_hp_str = f"{your_mon.health}/{your_mon.max_health}"
        opo_hp_str = f"{opo_mon.health}/{opo_mon.max_health}"
        print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
              f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
        print("[" + "■" * 20 + "" + "]") # you will have to make a real one
        print(f"HP:{your_hp_str:<38}HP:{opo_hp_str}" )
        print("")
        print("")
        print("")
        print("Your Moves: ")
        print(f"[{"Flamethrower":^20}][{"Dragon Claw":^20}]")
        print(f"[{"Draco Meteor":^20}][{"Hydropump":^20}]")
        # print("1234567890"*10)
        if your_mon.spd >= opo_mon.spd:
            if your_mon.health > 0:
                # print("Your turn!")
                your_att = input("Select your attack: ")
                # your_att = "Flamethrower"
                if your_att in attack_dict:
                    your_mon.attack(opo_mon, your_att)
                    input("Press Enter to continue")
                else:
                    print(f"You fumbled your command, {your_mon.name} froze in confusion!")
                    input("Press Enter to continue")
            if opo_mon.health > 0:
                print("Opponent's turn!")
                opo_mon.attack(your_mon, "Flamethrower")
                input("Press Enter to continue")
        else:
            if opo_mon.health > 0:
                print("Your opponent is fast!")
                opo_mon.attack(your_mon, "Flamethrower")
                input("Press Enter to continue")
            if your_mon.health > 0:
                print("Now is your chance!")
                your_att = input("Select your attack: ")
                if your_att in attack_dict:
                    your_mon.attack(opo_mon, your_att)
                    input("Press Enter to continue")
                else:
                    print(f"You fumbled your command, {your_mon.name} froze in confusion!")
                    input("Press Enter to continue")

    if your_mon.health <= 0:
        print(f"Your {your_mon.name} fainted!")
        print("You lose")
    elif your_mon.health > 0:
        print("The opposing Pokémon is knocked out!")
        print("You win")
        your_mon.lvl += 1



attack_dict = {
    "Flamethrower": 95,
    "Dragon Claw": 80,
    "Hydropump": 120,
    "Draco Meteor": 130,
}

class Pokemon:
    def __init__(self, name, evo, type_1, type_2, hp, att,
                 deff, spd):
        self.name = name
        self.evo = evo
        self.type_1 = type_1
        self.type_2 = type_1
        self.hp_1 = hp
        self.att_1 = att
        self.deff = deff
        self.spd = spd
        self.lvl = 1
        self.health = round((1 + ((self.lvl - 1) /10)) *150 * (hp/100))
        self.max_health = round((1 + ((self.lvl - 1) /10)) *150 * (hp/100))

    def attack(self, player_2, key):
        dmg_pre = round(self.att_1 * attack_dict[key] / random.randint(200,300))
        dmg_out = round((1 + ((self.lvl - 1) /10)) * (dmg_pre * 0.5) + (dmg_pre * (0.5 * (player_2.deff/300))))
        player_2.health -= dmg_out
        # print(dmg_pre)
        # print(dmg_out)
        print(f"{self.name} used {key} on {player_2.name}! [{dmg_out}]")
        # + str(player_2.health) + " " + str(dmg_out))


class PokemonM:
    def __init__(self, name, evo_back, type_1, type_2, hp, att,
                 deff, spd):
        self.name = name
        self.evo = evo_back
        self.type_1 = type_1
        self.type_2 = type_1
        self.hp_1 = hp
        self.att_1 = att
        self.deff = deff
        self.spd = spd

Charmander = Pokemon("Charmander", "Charmeleon",
                       "Fire", "None",
                       39, 52, 50, 65,)

Charmeleon = Pokemon("Charmeleon", "Charizard",
                       "Fire", "None", 58, 80,
                       65, 80)

Charizard = Pokemon("Charizard", "Mega Charizard X",
                      "Fire", "Flying", 78, 109,
                      85, 100)

Charizard_2 = Pokemon("Opponent's Charizard", "Mega Charizard X",
                      "Fire", "Flying", 78, 109,
                      85, 100)

Mega_Charizard_X = Pokemon("Mega Charizard X", "Charizard",
                            "Fire", "Dragon", 78,
                            130, 111, 100)

# print(Charmeleon.health)
# Charmander.attack(Charmeleon, "Flamethrower")
# print(Charmander.health)
#
# print(Charmeleon.health)
# Charizard.attack(Charmeleon, "Flamethrower")

pokemon_battle(Charizard, Charizard_2)