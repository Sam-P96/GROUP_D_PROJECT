import random


def type_bonus(key, defender):
    if str(attack_dict[key][0]) + str(defender.type_1) in type_chart_dict:
        bonus_1 = type_chart_dict[str(attack_dict[key][0]) + str(defender.type_1)]
        if str(attack_dict[key][0]) + str(defender.type_2) in type_chart_dict:
            bonus_2 = type_chart_dict[str(attack_dict[key][0]) + str(defender.type_1)] * type_chart_dict[str(attack_dict[key][0]) + str(defender.type_2)]
            return bonus_2
        return bonus_1
    else:
        return 1


def poke_hp_bar(pokemon_a):
    c_hp = int(pokemon_a.health)
    f_hp = int(pokemon_a.max_health)
    bar ="■" * (round( c_hp / f_hp * 20))
    output = ("[" + f"{bar:<20}]" )
    # print(c_hp)
    # print(f_hp)
    return output

# print("■" * round((20 / 100) * 20))


def pokemon_battle(your_mon, opo_mon):
    def swap_out(opponent):
        print("Who do you want to swap to?")
        for index, pokemon in enumerate(poke_team):
            print(index + 1, pokemon.name)
        while True:
            poke_2 = int(input("Send out: "))
            pokemon_battle(poke_team[poke_2 - 1], opponent)
            break
    while your_mon.health > 0 and opo_mon.health > 0:
        print("=" * 100)
        your_hp_str = f"{your_mon.health}/{your_mon.max_health}"
        opo_hp_str = f"{opo_mon.health}/{opo_mon.max_health}"
        print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
              f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
        print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
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
                if your_att == "SWAP":
                    swap_out(opo_mon)
                    continue
                # your_att = "Flamethrower"
                elif your_att in attack_dict:
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
        print("=" * 100)
        print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
              f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
        print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
        print(f"HP:{"0":<38}HP:{opo_hp_str}")
        print(f"Your {your_mon.name} fainted!")
        print("That's okay, you can get em next time!")
    elif your_mon.health > 0 and opo_mon.health < 0:
        print("=" * 100)
        print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
              f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
        print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
        print(f"HP:{your_hp_str:<38}HP:{"0"}")
        print("The opposing Pokémon is knocked out!")
        print("You won!")
        your_mon.lvl += 1



attack_dict = {
    "Flamethrower": ("Fire", 95),
    "Dragon Claw": ("Dragon", 80),
    "Hydropump": ("Water", 120),
    "Draco Meteor": ("Dragon", 130),
    "Earthquake": ("Ground", 100),
}

type_chart_dict = {"FireWater": 0.5,
                   "FireFire": 0.5,
                   "FireDragon": 0.5,
                   "WaterFire": 2,
                   "WaterDragon": 0.5,
                   "GroundFlying": 0,
                   "GroundFire": 2,
}

class Pokemon:
    def __init__(self, name, evo, type_1, type_2, hp, att,
                 deff, spd):
        self.name = name
        self.evo = evo
        self.type_1 = type_1
        self.type_2 = type_2
        self.hp_1 = hp
        self.att_1 = att
        self.deff = deff
        self.spd = spd
        self.lvl = 1
        self.health = round((1 + ((self.lvl - 1) /10)) *150 * (hp/100))
        self.max_health = round((1 + ((self.lvl - 1) /10)) *150 * (hp/100))

    def attack(self, player_2, key):
        dmg_pre = round(self.att_1 * attack_dict[key][1] / random.randint(200,300))
        dmg_out = round(((1 + ((self.lvl - 1) /10)) * (dmg_pre * 0.5) + (dmg_pre * (0.5 * (player_2.deff/300)))) * float(type_bonus(key, player_2)))
        player_2.health -= dmg_out
        # print(dmg_pre)
        # print(dmg_out)
        print(f"{self.name} used {key} on {player_2.name}! [{dmg_out}]")
        if float(type_bonus(key, player_2)) > 1.5:
            print("Its super effective!")
        elif float(type_bonus(key, player_2)) == 0:
            print(f"{player_2.name} is immune to {attack_dict[key]}")
        elif float(type_bonus(key, player_2)) < 1:
            print("Its not very effective!")
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
                       12, 52, 50, 65,)

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



poke_team = [Charmander, Charmeleon, Charizard, Mega_Charizard_X]

# print(Charmeleon.health)
# Charmander.attack(Charmeleon, "Flamethrower")
# print(Charmander.health)
#
# print(Charmeleon.health)
# Charizard.attack(Charmeleon, "Flamethrower")

pokemon_battle(Charizard, Charizard_2)

# print(str(attack_dict["Earthquake"][0]) + str(Charizard.type_1))
# print(type_chart_dict[str(attack_dict["Earthquake"][0]) + str(Charizard.type_1)])
#
# print(type_bonus("Earthquake", Charmeleon))
# print(attack_dict["Flamethrower"][1])