attack_dict = {
    "Flamethrower": 95,
    "Hydropump": 120,
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
        self.health = round(100 * (hp/100))

    def attack(self, player_2, key):
        base_dmg = attack_dict[key]
        dmg_out = self.att_1 * attack_dict[key] / 250
        print(player_2.health)


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

Mega_Charizard_X = PokemonM("Mega Charizard X", "Charizard",
                            "Fire", "Dragon", 78,
                            130, 111, 100)

Charmander.attack(Charmeleon, "Flamethrower")