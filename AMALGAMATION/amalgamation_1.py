import random
from type_chart_factor import type_bonus_dict
from attack_dict import attack_dict

def type_bonus(key: str, defender) -> int:
    """
    Returns the integer of the type bonus an attack has on any specific Pokemon.
    :param key: The attack key for the attack dictionary
    :param defender: The defending Pokemon
    :return: Integer of percentage bonus, 1 = 100%
    """
    if str(attack_dict[key][0]) + str(defender.type_1) in type_bonus_dict:
        bonus_1 = type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_1)]
        if str(attack_dict[key][0]) + str(defender.type_2) in type_bonus_dict:
            bonus_2 = type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_1)] * type_bonus_dict[str(attack_dict[key][0]) + str(defender.type_2)]
            return bonus_2
        return bonus_1
    else:
        return 1

def team_health_check(trainer):
    """
    Checks the Trainer's team, returns a list of Pokemon in that team who
    health is over 0.
    :param trainer: Variable the trainer is assigned to
    :return: List of healthy Pokemon
    """
    healthy_trainer_team = []
    for poke in trainer.team:
        if poke.health > 0:
            healthy_trainer_team.append(poke)
    return healthy_trainer_team

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



def opo_bonus(opponent):
    """
    Adjusts the health stats of a particular Pokemon, this code is meant
    to be used to increase the health of an opponent to artificially increase
    difficulty.
    :param opponent: The Pokemon, whose stat to be modified
    :return: None
    """
    opponent.health *= 2
    opponent.max_health *= 2



def type_display(poke):
    """
    Returns str of a Pokemon's type as such: [ Type 1 ] [ Type 2 ] with
    space reserved
    :param poke: Pokemon
    :return: Str of the Pokemon's type
    """
    if poke.type_2 != None:
        output = f"[{poke.type_1:^10}][{poke.type_2:^10}]"
    else:
        output = f"[{poke.type_1:^10}]"

    return output



def poke_hp_bar(pokemon_a):
    """
    Returns the Pokemon HP bar, used as a visual indicator of the Pokemon's
    health percentage
    :param pokemon_a: Pokemon whose health is to be displayed
    :return: Str of Pokemon's health as a bar
    """
    c_hp = int(pokemon_a.health)
    f_hp = int(pokemon_a.max_health)
    bar ="■" * (round( c_hp / f_hp * 20))
    output = ("[" + f"{bar:<20}]" )
    return output


 #PROPERLY DOCUMENT THIS FUNCTION PLS
def alive_team(teammates, exclude=None):
    """
    Takes in your team via you.team format and returns your alive team
    members.
    :param teammates: Your team in you.team format
    :param exclude:
    :return: Alive team members.
    """
    alive_members = [p for p in teammates if p.health > 0 and p is not exclude]
    return alive_members



def choose_switch_from_team(teammates, exclude = None, prompt =
"Who do you want to swap to?"):
    """
    Takes in your team (you.team), with option to exclude and gives you
    a prompt asking who do you want to swap to. Prints out your healthy Pokemon
    and returns your selection for who to send out next.
    :param teammates: Your team in you.team format
    :param exclude: Leave empty
    :param prompt: Leave empty
    :return: Chosen Pokemon
    """
    options = alive_team(teammates, exclude=exclude)
    if not options:
        return None
    print(prompt)
    for index, pokemon_a in enumerate(options):
        print(f"{index + 1}. {pokemon_a.name} [HP: {max(pokemon_a.health,0)} / {pokemon_a.max_health}] (Lv. {pokemon_a.lvl})")
    while True:
        try:
            pick = int(input("Send out: "))
            if 1 <= pick <= len(options):
                return options[pick - 1]
        except ValueError:
            pass
        print("Invalid choice. Try again.")



def swap_out(current, you):
    """
    (This is meant to be used when its your turn and you want to swap,
    not when your Pokemon fainted)
    Takes in your current Pokemon, and You, then shows you your other Pokemon
    and asks you if you want to switch to any of them.
    :param current: your current Pokemon
    :param you: The player
    :return: The Pokemon you chose to swap to
    """
    return choose_switch_from_team(you.team, exclude = current, prompt = "Who do you want to swap to?")

def your_battle_turn(your_mon, opo_mon, you, opo):
    """
    Function for your battle turn, takes in your pokemon, opponent Pokemon,
    you, and opponent then performs the battle functions or swap functions
    for gameplay.
    :param your_mon: Your Pokemon
    :param opo_mon: Your opponent's Pokemon
    :param you: The player
    :param opo: The opponent
    :return:
    """
    your_att = input("Select your attack: ")
    if your_att == "SWAP":
        new_mon = swap_out(your_mon, you)
        if new_mon is None:
            print("No other healthy Pokemon!!")
        else:
            print(f"{your_mon.name} come back! Go, {new_mon.name}!")
            return "switch", new_mon
    # your_att = "Flamethrower"
    if your_att in your_mon.att_key:
        your_mon.attack(opo_mon, your_att)
        input("Press Enter to continue")
        return "no switch"
    elif your_att != "SWAP" and your_att not in your_mon.att_key:
        print(f"You fumbled your command, {your_mon.name} froze in confusion!")
        input("Press Enter to continue")
        return "no switch"
    else:
        input("Press Enter to continue")
        return "no switch"



def pokemon_battle_4trainer(your_mon, opo_mon, you, opo):
    """
    The inner function for the trainer battle function. Requires you to enter
    the player's first Pokemon, the Opponent's first Pokemon, the player, and
    the opponent.
    :param your_mon: Player's Pokemon
    :param opo_mon: Opponent's Pokemon
    :param you: The Player
    :param opo: The Opponent
    :return: None
    """
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
        if your_mon.spd >= opo_mon.spd:
            if your_mon.health > 0:
                battle_input = your_battle_turn(your_mon, opo_mon, you, opo)
                if battle_input[0] == "switch":
                    your_mon = battle_input[1]
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
                battle_input = your_battle_turn(your_mon, opo_mon, you, opo)
                if battle_input[0] == "switch":
                    your_mon = battle_input[1]

        if your_mon.health <= 0:
            print("=" * 100)
            print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
                  f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
            print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
            print(f"HP:{"0":<38}HP:{opo_hp_str}")
            print(f"Your {your_mon.name} fainted!")
            replacement = choose_switch_from_team(you.team, exclude=your_mon,
            prompt = "Who will you send out next?! ")
            if replacement is None:
                print("You have no Pokemon left..")
                print("That's okay, you can get em next time!")
                break
            print(f"Go, {replacement.name}!")
            your_mon = replacement
        elif your_mon.health > 0 and opo_mon.health <= 0:
            healthy_opo_team = team_health_check(opo)
            your_healthy_team = team_health_check(you)
            if len(healthy_opo_team) > 0:
                print(f"Opponent sends out {healthy_opo_team[0].name}!")
                opo_mon = healthy_opo_team[0]
                input("Press Enter to continue")
            # print("=" * 100)
            # print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
            #       f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
            # print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
            # print(f"HP:{your_hp_str:<38}HP:0/{opo_mon.max_health}")
            # print("The opposing Pokémon is knocked out!")
            # print("You won!")



def trainer_battle(you, opo):
    """
    The outer function for trainer battles, takes in the player and the
    TRAINER opponent, then automatically runs the pokemon_battle_4trainer
    function, with the appropriate prompts when winning or losing.
    :param you: Player
    :param opo: Trainer Opponent
    :return:
    """
    healthy_opo_team = team_health_check(opo)
    your_healthy_team = team_health_check(you)
    print(f"You send out {you.team[0].name}")
    while len(healthy_opo_team) > 0 and len(your_healthy_team) > 0:
        healthy_opo_team = team_health_check(opo)
        your_healthy_team = team_health_check(you)
        pokemon_battle_4trainer(you.team[0], opo.team[0], you, opo)


    if len(healthy_opo_team) <= 0:
        print("You Won!")
    elif len(your_healthy_team) <= 0:
        print("You Lost!")



def pokemon_battle_4wild(your_mon, wild_mon, you):
    """
    The inner function for the wild encounter battle with wild Pokemon.
    :param your_mon: Your first Pokemon in your team
    :param wild_mon: The wild Pokemon
    :param you: The player
    :return:
    """
    opo_mon = wild_mon
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
        if your_mon.spd >= opo_mon.spd:
            if your_mon.health > 0:
                battle_input = your_battle_turn(your_mon, opo_mon, you, None)
                if battle_input[0] == "switch":
                    your_mon = battle_input[1]
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
                battle_input = your_battle_turn(your_mon, opo_mon, you, None)
                if battle_input[0] == "switch":
                    your_mon = battle_input[1]

        if your_mon.health <= 0:
            print("=" * 100)
            print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
                  f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
            print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
            print(f"HP:{"0":<38}HP:{opo_hp_str}")
            print(f"Your {your_mon.name} fainted!")
            replacement = choose_switch_from_team(you.team, exclude=your_mon,
            prompt = "Who will you send out next?! ")
            if replacement is None:
                print("You have no Pokemon left..")
                print("That's okay, you can get em next time!")
                break
            print(f"Go, {replacement.name}!")
            your_mon = replacement
        elif your_mon.health > 0 and opo_mon.health <= 0:
            your_healthy_team = team_health_check(you)
            print("=" * 100)
            print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
                  f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
            print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
            print(f"HP:{your_hp_str:<38}HP:0/{opo_mon.max_health}")
            print("The opposing Pokémon is knocked out!")
            print("You won!")



def wild_encounter_battle(your_mon, you, wild_pokemon_list):
    """
    Takes in your first Pokemon, you, and the wild Pokemon list (wild Poke)
    or you can change the wild Poke list to be randomly selected from, then
    runs the wild Pokemon Battle Function
    :param your_mon: Your first Pokemon in you.team format
    :param you: The player
    :param wild_pokemon_list: the list of wild Pokemon to be randomly selected
    :return:
    """
    wild_mon = random.choice(wild_pokemon_list)
    print(wild_mon.name)
    pokemon_battle_4wild(your_mon, wild_mon, you)

# def wild_encounter(you, wild_poke_list):
#     wild = random.choice(wild_poke_list)
#     pokemon_battle(you.team[0], wild, you, None) # THIS DOES NOT BELONG HERE, MAKE A NEW FILE FO RWILD ENCOUNTERS


from  villain_npc import Sam
from villain_npc import Meeri

sam_list = []
for pokemon in Sam.team:
    sam_list.append(pokemon.name)
print(sam_list)

meeri_list = []
for pokemon in Meeri.team:
    meeri_list.append(pokemon.name)
print(meeri_list)

trainer_battle(Sam, Meeri)

# from random_pokemon_encounter import wild_poke
#
#
#
# wild_encounter_battle(Sam.team[0], Sam, wild_poke)
