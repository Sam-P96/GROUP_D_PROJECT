import random
from attack_dict import attack_dict
from type_chart_factor import type_bonus_dict


def type_bonus(key, defender):
    if str(attack_dict[key][0]) + str(defender.type_1) in type_bonus_dict:
        bonus_1 = type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_1)]
        if str(attack_dict[key][0]) + str(defender.type_2) in type_bonus_dict:
            bonus_2 = type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_1)] * type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_2)]
            return bonus_2
        return bonus_1
    else:
        return 1

class Pokemon:
    def __init__(self, name, evo, type_1, type_2, hp, att,
                 deff, spd, a1, a2, a3, a4):
        self.name = name
        self.evo = evo
        self.type_1 = type_1
        self.type_2 = type_2
        self.hp_1 = hp
        self.atk_stat = att
        self.deff = deff
        self.spd = spd
        self.lvl = 1
        self.health = round((1 + ((self.lvl - 1) /10)) *150 * (hp/100))
        self.max_health = round((1 + ((self.lvl - 1) /10)) *150 * (hp/100))
        self.atk_1 = a1
        self.atk_2 = a2
        self.atk_3 = a3
        self.atk_4 = a4
        self.att_key = [a1, a2, a3, a4]



    def attack(self, player_2, key):
        dmg_pre = round(self.atk_stat * attack_dict[key][1] / random.randint(200, 300))
        dmg_out = round(((1 + ((self.lvl - 1) /10)) * (dmg_pre * 0.5) + (dmg_pre * (0.5 * (player_2.deff/300)))) * float(type_bonus(key, player_2)))
        player_2.health -= dmg_out
        # print(dmg_pre)
        # print(dmg_out)
        print(f"{self.name} used {key} on {player_2.name}! [{dmg_out}]")
        if float(type_bonus(key, player_2)) > 1.5:
            print("Its super effective!")
        elif float(type_bonus(key, player_2)) == 0:
            print(f"{player_2.name} is immune to {key}")
        elif float(type_bonus(key, player_2)) < 1:
            print("Its not very effective!")
        # + str(player_2.health) + " " + str(dmg_out))

Charmander = Pokemon("Charmander", "Charmeleon",
                       "Fire", None,
                       12, 52, 50, 65,"Scratch",
                     "Flamethrower", "Rock Slide", "Shadow Claw")

Charmeleon = Pokemon("Charmeleon", "Charizard",
                       "Fire", None, 58, 80,
                       65, 80, "Slash", "Flamethrower",
                     "Thunder Punch", "Shadow Claw")

Charizard = Pokemon("Charizard", "Mega Charizard X",
                      "Fire", "Flying", 78, 109,
                      85, 100, "Overheat","Thunder Punch",
                    "Aerial Ace", "Shadow Claw")

Mega_Charizard_X = Pokemon("Mega Charizard X", "Charizard",
                            "Fire", "Dragon", 78,
                            130, 111, 100, "Overheat",
                           "Thunder Punch", "Shadow Claw",
                           "Dragon Claw")

Dialga_O = Pokemon("Dialga, Origin Form", None,
                            "Steel", "Dragon", 100,
                            150, 120, 90, "Roar of Time",
                   "Earthquake", "Hyper Beam", "Iron Tail")

Mega_Mewtwo_Y = Pokemon("Mega Mewtwo Y", None, "Psychic",
                        None, 106, 194, 120, 140,
                        "Psystrike", "Shadow Ball", "Hyper Beam",
                        "Ice Beam")

Landorus_T = Pokemon("Landorus Therian Form", None,
                           "Ground", "Flying", 89,
                           145, 90, 91, "Earthquake",
                           "Iron Tail", "Rock Slide", "Aerial Ace")

Torterra = Pokemon("Torterra", None, "Grass", "Ground",
                   95, 109, 105, 56, "Earthquake",
                   "Solar Beam", "Hyper Beam", "Rock Slide")

Blaziken = Pokemon("Blaziken", None, "Fire", "Fighting",
                   80, 120, 70, 80, "Blaze Kick",
                   "Aerial Ace", "Sky Uppercut", "Slash")

Mega_Blaziken = Pokemon("Mega Blaziken", None, "Fire", "Fighting",
                   80, 160, 80, 100, "Overheat",
                        "Sky Uppercut", "Thunder Punch", "Shadow Claw")

Rhyperior = Pokemon("Rhyperior", None, "Rock", "Ground",
                    115, 140, 55, 40, "Earthquake",
                    "Rock Slide", "Thunder Punch", "Ice Punch")

Cramorant = Pokemon("Cramorant", None, "Flying", "Water",
                    70, 85, 95, 85, "Hydropump",
                    "Aerial Ace", "Ice Beam", "Hyper Beam")

Vaporeon = Pokemon("Vaporeon", None, "Water", None,
                   130, 110, 95, 65, "Hydropump",
                   "Iron Tail", "Shadow Ball", "Ice Beam")

Raging_Bolt = Pokemon("Raging Bolt", None, "Electric",
                      "Dragon", 125, 137, 91, 75,
                      "Draco Meteor", "Thunderclap",
                      "Stomping Tantrum", "Crunch")

Ceruledge = Pokemon("Ceruledge", None, "Fire", "Ghost",
                    75, 125, 100, 85, "Close Comba",
                    "Phantom Force", "Flare Blitz", "Dragon Claw")

Giratina_O = Pokemon("Giratina Origin Form", None, "Ghost",
                     "Dragon", 150, 100, 120, 90,
                     "Phantom Force", "Outrage", "Aura Sphere",
                     "Thunder")

Sylveon = Pokemon("Sylveon", None, "Fairy", None,
                  95, 110, 130, 60, "Shadow Ball",
                  "Trump Card", "Moonblast", "Magical Leaf")

Venusaur = Pokemon("Venusaur", None, "Grass", "Poison",
                   80, 100, 100, 80, "Solar Beam",
                   "Sludge Bomb", "Stomping Tantrum", "Hyper Beam")

Blastoise = Pokemon("Blastoise", None, "Water", None,
                    79, 85, 105, 78, "Hydropump",
                    "Aura Sphere", "Seismic Toss", "Iron Tail")

Iron_Crown = Pokemon("Iron Crown", None, "Steel",
                     "Psychic", 90, 122, 108, 98,
                     "Hyper Beam", "Expanding Force",
                     "Flash Cannon", "Solar Blade")

Regice = Pokemon("Regice", None, "Ice", None, 80,
                 100, 200, 50, "Ice Beam", "Thunderbolt",
                 "Rock Tomb","Stomping Tantrum")

Lapras = Pokemon("Lapras", None, "Water", "Ice",
                 130, 85, 95, 60, "Ice Beam", "Surf",
                 "Iron Tail", "Psychic")

Glastrier = Pokemon("Glastrier", None, "Ice", None,
                    100, 145, 130, 30, "Close Combat",
                    "Ice Beam", "High Horsepower", "Crunch")

Vespiquen = Pokemon("Vespiquen", None, "Bug", "Flying",
                    70, 80, 102, 40, "X-Scissor",
                    "Sludge Bomb", "Aerial Ace", "Psychic Noise")

Mega_Scizor = Pokemon("Mega Scizor", None, "Bug",
                      "Steel", 70, 150, 140, 75,
                      "Bullet Punch", "X-Scissor", "Ominous Wind",
                      "Aerial Ace")

Arceus = Pokemon("Arceus", None, "Normal", None,
                 120, 120, 120, 120, "Judgment",
                 "Thunder", "Earthquake", "Seismic Toss")

