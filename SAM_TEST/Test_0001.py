class PokemonS1:
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

class PokemonS2:
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

class PokemonS3:
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

class PokemonM:
    def __init__(self, name, revert, type_1, type_2, hp, att,
                 deff, spd):
        self.name_1 = name
        self.revert = revert
        self.type_1 = type_1
        self.type_2 = type_1
        self.hp_1 = hp
        self.att_1 = att
        self.deff = deff
        self.spd = spd



Charmander = PokemonS1("Charmander", "Charmeleon",
                       "Fire", "None",
                       39, 52, 50, 65,)

Charmeleon = PokemonS2("Charmeleon", "Charizard",
                       "Fire", "None", 58, 80,
                       65, 80)

Charizard = PokemonS3("Charizard", "Mega Charizard X",
                      "Fire", "Flying", 78, 109,
                      85, 100)

Mega_Charizard_X = PokemonM("Mega Charizard X", "Charizard",
                            "Fire", "Dragon", 78,
                            130, 111, 100)

