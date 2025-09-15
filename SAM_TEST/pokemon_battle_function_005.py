import random
from attack_dict import attack_dict
from npc_attack_dict import npc_attack_dict
from type_chart_factor import type_bonus_dict

def opo_bonus(opponent):
    opponent.health *= 2
    opponent.max_health *= 2


def type_bonus(key, defender):
    if str(attack_dict[key][0]) + str(defender.type_1) in type_bonus_dict:
        bonus_1 = type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_1)]
        if str(attack_dict[key][0]) + str(defender.type_2) in type_bonus_dict:
            bonus_2 = type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_1)] * type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_2)]
            return bonus_2
        return bonus_1
    else:
        return 1



def type_display(poke):
    if poke.type_2 != None:
        output = f"[{poke.type_1:^10}][{poke.type_2:^10}]"
    else:
        output = f"[{poke.type_1:^10}]"

    return output



def poke_hp_bar(pokemon_a):
    c_hp = int(pokemon_a.health)
    f_hp = int(pokemon_a.max_health)
    bar ="■" * (round( c_hp / f_hp * 20))
    output = ("[" + f"{bar:<20}]" )
    # print(c_hp)
    # print(f_hp)
    return output



def alive_team(teammates, exclude=None):
    alive_members = [p for p in teammates if p.health > 0 and p is not exclude]
    return alive_members



def choose_switch_from_team(teammates, exclude = None, prompt =
"Who do you want to swap to?"):
    options = alive_team(teammates, exclude=exclude)
    if not options:
        return None
    print(prompt)
    for index, pokemon_a in enumerate(options, start=1):
        print(f"{index}. {pokemon_a.name} [HP: {max(pokemon_a.health,0)} / {pokemon_a.max_health}] (Lv. {pokemon_a.lvl})")
    while True:
        try:
            pick = int(input("Send out: "))
            if 1 <= pick <= len(options):
                return options[pick - 1]
        except ValueError:
            pass
        print("Invalid choice. Try again.")



def pokemon_battle(your_mon, opo_mon):
    def swap_out(current, opponent):
        return choose_switch_from_team(poke_team, exclude=current, prompt = "Who do you want to swap to?")



    while your_mon.health > 0 and opo_mon.health > 0:
        print("=" * 100)
        your_hp_str = f"{your_mon.health}/{your_mon.max_health}"
        opo_hp_str = f"{opo_mon.health}/{opo_mon.max_health}"
        print(f"{str(your_mon.name) + " [Lv." + str(your_mon.lvl) + "]":<40} "
              f"{str(opo_mon.name) + " [Lv." + str(opo_mon.lvl)}]")
        print(f"{type_display(your_mon):<41}" + type_display(opo_mon))
        print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
        print(f"HP:{your_hp_str:<38}HP:{opo_hp_str}" )
        print("")
        print("")
        print("")
        print("Your Moves: ")
        print(f"[{your_mon.atk_1:^20}][{your_mon.atk_2:^20}]")
        print(f"[{your_mon.atk_3:^20}][{your_mon.atk_4:^20}]")
        # print("1234567890"*10)
        if your_mon.spd >= opo_mon.spd:
            if your_mon.health > 0:
                # print("Your turn!")
                your_att = input("Select your attack: ")
                if your_att == "SWAP":
                    new_mon = swap_out(your_mon, opo_mon)
                    if new_mon is None:
                        print("No other healthy Pokemon!!")
                    else:
                        print(f"{your_mon.name} come back! Go, {new_mon.name}!")
                        your_mon = new_mon
                # your_att = "Flamethrower"
                if your_att in your_mon.att_key:
                    your_mon.attack(opo_mon, your_att)
                    input("Press Enter to continue")
                elif your_att != "SWAP" and your_att not in your_mon.att_key:
                    print(f"You fumbled your command, {your_mon.name} froze in confusion!")
                    input("Press Enter to continue")
                else:
                    input("Press Enter to continue")
            if opo_mon.health > 0:
                print("Opponent's turn!")
                opo_mon.attack(your_mon, random.choice(opo_mon.att_key))
                input("Press Enter to continue")
        else:
            if opo_mon.health > 0:
                print("Your opponent is fast!")
                opo_mon.attack(your_mon, random.choice(opo_mon.att_key))
                input("Press Enter to continue")
            if your_mon.health > 0:
                print("Now is your chance!")
                your_att = input("Select your attack: ")
                if your_att == "SWAP":
                    new_mon = swap_out(your_mon, opo_mon)
                    if new_mon is None:
                        print("No other healthy Pokemon!!")
                    else:
                        print(f"{your_mon.name} come back! Go, {new_mon.name}!")
                        your_mon = new_mon
                if your_att in your_mon.att_key:
                    your_mon.attack(opo_mon, your_att)
                    input("Press Enter to continue")
                elif your_att != "SWAP" and your_att not in your_mon.att_key:
                    print(f"You fumbled your command, {your_mon.name} froze in confusion!")
                    input("Press Enter to continue")
                else:
                    input("Press Enter to continue")


        if your_mon.health <= 0:
            print("=" * 100)
            print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
                  f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
            print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
            print(f"HP:{"0":<38}HP:{opo_hp_str}")
            print(f"Your {your_mon.name} fainted!")
            replacement = choose_switch_from_team(poke_team, exclude=your_mon, prompt = "Who will you send out next?! ")
            if replacement is None:
                print("You have no Pokemon left..")
                print("That's okay, you can get em next time!")
                break
            print(f"Go, {replacement.name}!")
            your_mon = replacement
        elif your_mon.health > 0 and opo_mon.health < 0:
            print("=" * 100)
            print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
                  f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
            print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
            print(f"HP:{your_hp_str:<38}HP:0/{opo_mon.max_health}")
            print("The opposing Pokémon is knocked out!")
            print("You won!")
            your_mon.lvl += 1



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

Landorus_Therian = Pokemon("Landorus Therian Form", None,
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

Arceus = Pokemon("Arceus", None, "Normal", None,
                 120, 120, 120, 120, "Judgment",
                 "Thunder", "Earthquake", "Seismic Toss")

all_pokemon_list = [Charmeleon, Charizard, Mega_Charizard_X, Dialga_O,
                    Mega_Mewtwo_Y, Landorus_Therian, Torterra, Blaziken,
                    Mega_Blaziken, Rhyperior, Cramorant]
poke_team = [random.choice(all_pokemon_list),
             random.choice(all_pokemon_list),
             random.choice(all_pokemon_list)] # I'd add an exclude thing, but this is just for testing
strong_pokemon_list = [Mega_Charizard_X, Dialga_O, Mega_Mewtwo_Y,
                       Landorus_Therian, Mega_Blaziken, Vaporeon, Arceus]
opponent_1 = random.choice(strong_pokemon_list)
# opponent_1 = Arceus
opo_bonus(opponent_1)

pokemon_battle(random.choice(poke_team), opponent_1)
