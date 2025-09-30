import random
import sys
import time
import all_pokemon_list
from type_chart_factor import type_bonus_dict
from attack_dict import attack_dict
from all_pokemon_list import Arceus
from all_pokemon_list import Pikachu
from all_pokemon_list import Meowth
from all_pokemon_list import LC_Poke
from all_pokemon_list import NU_Poke
from all_pokemon_list import OU_Poke
from all_pokemon_list import Uber_Poke
from achievements import achv_dict
from dialogues import villain_intro
from dialogues import wdyw_line
from dialogues import battle_intro_line
from dialogues import poker_intro_line
from dialogues import roulette_intro_line
from dialogues import invalid_selection_line
from dialogues import leave_chat_line



class Human:
    def __init__(self, name: str, rank: str):
        self.name = name
        self.rank = rank
        self.health = 300
        self.max_health = 300
        self.fuel = 100
        self.location = ["60.3179° N", "24.9496° E"]
        self.team = []
        self.exclude = set()
        self.team_p = []
        self.exclude_p = set()
        self.achv = []
        if rank == "cop":
            for team_no in range(1):
                available_poke = []
                for poke in NU_Poke:
                    if poke not in self.exclude:
                        available_poke.append(poke)
                poke = random.choice(available_poke)
                self.team.append(poke)
                self.exclude.add(poke)
                evil_poke.append(poke)
        elif rank == "grunt":
            for team_no in range(2):
                available_poke = []
                for poke in NU_Poke:
                    if poke not in self.exclude:
                        available_poke.append(poke)
                poke = random.choice(available_poke)
                self.team.append(poke)
                self.exclude.add(poke)
                evil_poke.append(poke)
        elif rank == "manager":
            for team_no in range(3):
                available_poke = []
                for poke in OU_Poke:
                    if poke not in self.exclude:
                        available_poke.append(poke)
                poke = random.choice(available_poke)
                self.team.append(poke)
                self.exclude.add(poke)
                evil_poke.append(poke)
        elif rank == "exec":
            for team_no in range(6):
                uber_rate = random.randint(1,2)
                available_poke = []
                if uber_rate == 1:
                    for poke in Uber_Poke:
                        if poke not in self.exclude:
                            available_poke.append(poke)
                    poke = random.choice(available_poke)
                    self.team.append(poke)
                    self.exclude.add(poke)
                    evil_poke.append(poke)
                else:
                    for poke in OU_Poke:
                        if poke not in self.exclude:
                            available_poke.append(poke)
                    poke = random.choice(available_poke)
                    self.team.append(poke)
                    self.exclude.add(poke)
                    evil_poke.append(poke)


    def capture(self, pokemon):
        self.team.append(pokemon)



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
        d_print(f"{self.name} used {key} on {player_2.name}! [{dmg_out}]\n")
        if float(type_bonus(key, player_2)) > 1.5:
            d_print("Its super effective!\n")
        elif float(type_bonus(key, player_2)) == 0:
            d_print(f"{player_2.name} is immune to {key}\n")
        elif float(type_bonus(key, player_2)) < 1:
            d_print("Its not very effective!\n")
        # + str(player_2.health) + " " + str(dmg_out))



def police_attack():
    "function to place at the beginning of every flight selection"
    if "Global Warming" in  player_achv:
        player.health -= 50
        print("Global ")



def flight_cost(distance):
    fuel_cost = (distance / 7500) * 100
    player.fuel -= int(fuel_cost)
    co2_cost = int(distance * 0.246)
    achv_dict["co2"][1] -= co2_cost



def achievement_check(achv_dict, player_achv):
    if achv_dict["co2"][1] <= 0:
        achv_dict["co2"][1] = 999 ** 99
        player_achv.append(achv_dict["co2"][0])
    if achv_dict["rr"][1] <= 0:
        achv_dict["rr"][1] = 999 ** 99
        player_achv.append(achv_dict["rr"][0])
    if achv_dict["poker"][1] <= 0:
        achv_dict["poker"][1] = 999 ** 99
        player_achv.append(achv_dict["poker"][0])
    if achv_dict["continent"][1] <= 0:
        achv_dict["continent"][1] = 999 ** 99
        player_achv.append(achv_dict["continent"][0])
    if achv_dict["polar"][1] <= 0:
        achv_dict["polar"][1] = 999 ** 99
        player_achv.append(achv_dict["polar"][0])
    if achv_dict["defeat god"][1] <= 0:
        achv_dict["defeat god"][1] = 999 ** 99
        player_achv.append(achv_dict["defeat god"][0])
    if achv_dict["free god"][1] <= 0:
        achv_dict["free god"][1] = 999 ** 99
        player_achv.append(achv_dict["free god"][0])



def d_print(s): # CHANGE time.sleep to 0 when testing code.
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    # print(s)



def helper(context):
    if context == "rr_game":
        user_input = input("Press enter to continue")
        if user_input == "/HELP":
            print("You're on your own now. You signed up for this.")
            user_input_2 = input("Press enter to continue")
            return user_input_2
        return user_input
    elif context == "trainer_battle":
        user_input = input("Enter your attack: ")
        if user_input == "/HELP":
            print("In a Pokemon Battle, you command your Pokemon by writing their attacks correctly.")
            print("Remember that attack commands are case sensitive. So pay attention to capital letters.")
            print("Swap out your Pokemon during battle by entering 'SWAP' then select the Pokemon you with to swap out")
            print("Once you defeated the opponent, you can choose to add that Pokemon to your Team.")
            print("Remember, you are a criminal on the run, and will not be able to have more than 6 Pokemon.")
            print("That means, you wont store excess Pokemon in a PC, your only option is to release them.")
            user_input_2 = input("Select your attack: ")
            return user_input_2
        return user_input
    elif context == "Poker": ### I dont know what to do here yet
        user_input = input("Enter your choice: ")
        if user_input == "/HELP":
            print("Play Poker, bet your Pokemon on the line. Remember.")
            user_input_2 = input("Select your choice: ")
            return user_input_2
        return user_input
    else:
        user_input_2 = input("Select your choice: ")
        return user_input_2



def game_russian(self, player_2):
    player_team_hp = team_health_check(self)
    opo_team_hp = team_health_check(player_2)
    print(f"{self.name} challenged {player_2.name} to Russian Roulette!")
    while len(player_team_hp) > 0 and len(opo_team_hp) > 0:
        player_team_hp = team_health_check(self)
        opo_team_hp = team_health_check(player_2)
        sacrifice = 0
        print("You must select a Pokemon to play for you.")
        for index, pokemon in enumerate(self.team):
            print(f"{index + 1}. {pokemon.name}")
        while sacrifice not in self.team:
            p_select = input("Select your Pokemon: ")
            try:
                test_1 = int(p_select)
            except ValueError:
                print("Invalid input")
                continue

            if self.team[int(p_select) - 1] in self.team:
                sacrifice = self.team[int(p_select) - 1]
            else:
                print("Invalid input")
        shot = 1
        player_list = [self, player_2]
        print(f"{sacrifice.name} will stand in for {self.name}")
        while sacrifice in self.team and len(player_2.team) > 0:
            for turn in player_list:
                print("*Spinning the barrel*")
                bullet = random.randint(1, 6)
                # print(f"Bullet is {bullet}") #remove later after testing
                if turn == self:
                    print(f"{self.name}'s turn. Click.")
                    if shot != bullet:
                        input("Press Enter to shoot")
                        print("Nothing happened.")
                        input("Press Enter to continue")
                    else:
                        input("Press Enter to shoot")
                        wild_poke.append(sacrifice)
                        self.team.remove(sacrifice)
                        print("=" * 100)
                        print(f"Bang! {sacrifice.name} fell giving you everything.")
                        input("Press enter to continue.")
                        player_team_hp = team_health_check(self)
                        opo_team_hp = team_health_check(player_2)
                        break
                elif turn == player_2:
                    print(f"{player_2.name}'s turn. Click.")
                    if shot != bullet:
                        input("Press Enter to shoot")
                        print("Nothing happened.")
                        input("Press Enter to continue")
                    else:
                        input("Press Enter to shoot")
                        print("=" * 100)
                        print(f"Bang! {player_2.team[0].name} fell abruptly.")
                        wild_poke.append(player_2.team[0])
                        player_2.team.remove(player_2.team[0])
                        player_team_hp = team_health_check(self)
                        opo_team_hp = team_health_check(player_2)
                        if len(player_2.team) > 0:
                            print(f"{player_2.team[0].name} steps up in its trainer's place.")
                        else:
                            print(f"{player_2.name} is out of Pokemon.")
                            break
                    print("=" * 100)
                    player_team_hp = team_health_check(self)
                    opo_team_hp = team_health_check(player_2)


    if len(player_team_hp) > 0:
        print("You get to walk away.")
    else:
        print("You made a lot of bad choices. Game Over.")



def wild_pokemon_assigner(player, evil):
    """
    A function to move all the unused pokemon into the wild pool
    :param player:
    :param evil:
    :return:
    """
    for pokemon in LC_Poke:
        if pokemon not in evil and pokemon not in player.team:
            wild_poke.append(pokemon)
    for pokemon in NU_Poke:
        if pokemon not in evil and pokemon not in player.team:
            wild_poke.append(pokemon)
    for pokemon in OU_Poke:
        if pokemon not in evil and pokemon not in player.team:
            wild_poke.append(pokemon)
    for pokemon in Uber_Poke:
        if pokemon not in evil and pokemon not in player.team:
            wild_poke.append(pokemon)



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
    your_att = helper("trainer_battle")
    if your_att == "SWAP":
        new_mon = swap_out(your_mon, you)
        if new_mon is None:
            print("No other healthy Pokemon!!")
        else:
            d_print(f"{your_mon.name} come back! Go, {new_mon.name}!\n")
            return "switch", new_mon
    # your_att = "Flamethrower"
    if your_att in your_mon.att_key:
        your_mon.attack(opo_mon, your_att)
        input("Press Enter to continue")
        return "no switch"
    elif your_att != "SWAP" and your_att not in your_mon.att_key:
        d_print(f"You fumbled your command, {your_mon.name} froze in confusion!\n")
        input("Press Enter to continue")
        return "no switch"
    else:
        input("Press Enter to continue")
        return "no switch"



def into_team(player, opo, wild):
    """
    The inner function used for stealing or capturing Pokemon, the function
    creates a loop until you enter 0 that allows you to move the opposing
    pokemon into your team, and moves excess Pokemon into the wild list
    :param player: player
    :param opo: opponent whose team to check, write None if capturing wild Pokemon
    :param wild: wild pokemon, write None if battling human NPC
    :return: None
    """
    if wild == None:
        while True:
            if len(player.team) < 6:
                while len(player.team) < 6 and len(opo.team) > 0:
                    print(f"{opo.team[0].name} was added to your team.")
                    player.team.append(opo.team[0])
                    opo.team.remove(opo.team[0])
                break
            else:
                d_print("Which Pokemon would you like to add to your team?\n")
                for index_o, poke_o in enumerate(opo.team):
                    print(f"{index_o + 1}. {poke_o.name}")
                print(f"0. End")
                user_input_opo = input("Select your choice: ")
                try:
                    test_1 = int(user_input_opo)
                except ValueError:
                    print("Invalid input")
                    continue
                if 0 < int(user_input_opo) <= len(opo.team):
                    d_print("Which Pokemon from your team would you like to release?\n")
                    for index_p, poke_p in enumerate(player.team):
                        print(f"{index_p + 1}. {poke_p.name}")
                    print(f"0. End")
                    user_input_player = input("Select your choice: ")
                    try:
                        test_01 = int(user_input_player)
                    except ValueError:
                        print("Invalid input")
                        continue
                    if 0 < int(user_input_player) <= len(player.team):
                        wild_poke.append(player.team[int(user_input_player) - 1])
                        player.team[int(user_input_player) - 1] = opo.team[int(user_input_opo) - 1]
                        opo.team.remove(opo.team[int(user_input_opo) - 1])
                    elif int(user_input_player) == 0:
                        if len(opo.team) > 0:
                            for index, poke in enumerate(opo.team):
                                wild_poke.append(opo.team[index])
                                opo.team.remove(opo.team[index])
                        d_print("Stealing ended\n")
                        break
                    else:
                        print("Invalid input")
                elif int(user_input_opo) == 0:
                    if len(opo.team) > 0:
                        for index, poke in enumerate(opo.team):
                            wild_poke.append(opo.team[index])
                            opo.team.remove(opo.team[index])
                    d_print("Stealing ended\n")
                    break
                else:
                    print("Invalid input")
    elif opo == None:
        while True:
            d_print("Which Pokemon from your team would you like to release?\n")
            for index_p, poke_p in enumerate(player.team):
                print(f"{index_p + 1}. {poke_p.name}")
            print(f"0. End")
            user_input_player = input("Select your choice: ")
            try:
                test_01 = int(user_input_player)
            except ValueError:
                print("Invalid input")
                continue
            if 0 < int(user_input_player) <= len(player.team):
                wild_poke.append(player.team[int(user_input_player) - 1])
                player.team[int(user_input_player) - 1] = wild
                wild_poke.remove(wild)
                break
            elif int(user_input_player) == 0:
                print("Capture ended")
                break
            else:
                print("Invalid input")


# Ignore the highlight here
def wild_capture(wild, player):
    """
    Takes in wild Pokemon and Player, and asks you if you want to add it to
    your team. If you select yes, it will run the into_team function
    :param wild:
    :param player:
    :return:
    """
    while True:
        if len(player.team) < 6:
            print(f"{wild.name}, started following you.")
            player.team.append(wild)
            break
        else:
            d_print("""You cannot have more than 6 Pokemon, and you do not have 
legal access to a PC to store excess Pokemon.\n""")
            print("Would you like to capture this Pokemon?")
            print("1. Yes")
            print("2. No")
            y_n = int(input("Select your choice:"))
            if y_n == 1:
                into_team(player, None, wild)
                break
            if y_n == 2:
                break
            else:
                print("Invalid input")


# Ignore the highlight here
def battle_steal(player, opo):
    """
    Takes in Opponent and Player, and asks you if you want to add pokemon from
    the opponent's team to your team. If you select yes, it will run the
    into_team function. If it is the first time you are running this function it
    will present an extra prompt
    :param player: player
    :param opo: opponent
    :return:
    """
    first_time = 1
    while first_time >= 1 and len(player.team) >= 6:
        d_print("""You won! But you're only able to carry 6 Pokemon at all times.\n""")
        first_time -= 1

    into_team(player, opo, None)



def all_poke_heal(player):
    """
    Heals all Pokemon in the team, can be used for any trainer class.
    :param player:
    :return:
    """
    for pokemon in player.team:
        pokemon.health = round((1 + ((pokemon.lvl - 1) /10)) *150 * (pokemon.hp_1/100))



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
                d_print("Opponent's turn!\n")
                opo_mon.attack(your_mon, random.choice(opo_mon.att_key))
                input("Press Enter to continue")
        else:
            if opo_mon.health > 0:
                d_print("Your opponent is fast!\n")
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
            d_print(f"Your {your_mon.name} is knocked out!\n")
            replacement = choose_switch_from_team(you.team, exclude=your_mon,
            prompt = "Who will you send out next?! ")
            if replacement is None:
                d_print("You have no Pokemon left..\n")
                d_print("That's okay, you can get em next time!\n")
                break
            d_print(f"Go, {replacement.name}!\n")
            your_mon = replacement
        elif your_mon.health > 0 and opo_mon.health <= 0:
            healthy_opo_team = team_health_check(opo)
            your_healthy_team = team_health_check(you)
            d_print(f"{opo_mon.name} is knocked out!\n")
            if len(healthy_opo_team) > 0:
                d_print(f"Opponent sends out {healthy_opo_team[0].name}!\n")
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
    print(f"\n{opo.name} sends out {opo.team[0].name}")
    print(f"\nYou send out {you.team[0].name}")
    while len(healthy_opo_team) > 0 and len(your_healthy_team) > 0:
        healthy_opo_team = team_health_check(opo)
        your_healthy_team = team_health_check(you)
        pokemon_battle_4trainer(you.team[0], opo.team[0], you, opo)


    if len(healthy_opo_team) <= 0:
        print("You Won!")
        battle_steal(you, opo)
    elif len(your_healthy_team) <= 0:
        print("You Lost!")

    # for poke in you.team: # Code for testing team modification
    #     print(poke.name)



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
                d_print("Opponent's turn!\n")
                opo_mon.attack(your_mon, random.choice(opo_mon.att_key))
                input("Press Enter to continue")
        else:
            if opo_mon.health > 0:
                d_print("Your opponent is fast!\n")
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
            print(f"Your {your_mon.name} is knocked out!")
            replacement = choose_switch_from_team(you.team, exclude=your_mon,
            prompt = "Who will you send out next?! ")
            if replacement is None:
                d_print("You have no Pokemon left..\n")
                d_print("That's okay, you can get em next time!\n")
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
            d_print("The opposing Pokémon is knocked out!\n")
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
    d_print(f"\nA wild {wild_mon.name} appeared!!\n")
    pokemon_battle_4wild(your_mon, wild_mon, you)
    your_healthy_team = team_health_check(you)
    if len(your_healthy_team) <= 0:
        print("You Lost!")
    else:
        wild_capture(wild_mon, you)
    # for poke in you.team: # Code for testing team modification
    #     print(poke.name)



def start_rr_game(player, opo):
    """
    For starting the Russian roulette game.
    :param player: Player
    :param opo: Opponent NPC
    :return:
    """
    print("""You are about to initiate a game of Russian Roulette. There's no
turning back if you decide to start until either you or your opponent are out
of Pokemon. Are you sure you want to continue?""")
    print("1. Yes")
    print("2. No")
    while True:
        choice = input("Select your choice: ")
        try:
            y_n = int(choice)
        except ValueError:
            print("Invalid input.")
            continue
        if y_n == 1:
            game_russian(player, opo)
            break
        elif y_n == 2:
            print("You left the interaction.")
            break
        else:
            print("Invalid input")



def poker(player1,player2):
    """
    Poker demo (2 players) with ASCII card rendering and basic hand evaluation.
    Notes:
    - Ranking tuple shape varies across categories; see `CATEGORY_NAME`.
    """
    import random
    ranks = list(range(2,15))
    # suits = ['C','D','H','S']  #C -> Clubs, D-> Diamonds, H-> Hearts, S -> Spades
    ranks_string = {11: 'J',12: 'Q',13: 'K',14: 'A'}
    # suits_icon = {'C': '♣', 'D': '♦', 'H': '♥', 'S': '♠'}
    suits = ['♣','♦','♥','♠']

    CATEGORY_NAME = {
        10: "Royal Flush",
        9: "Straight Flush",
        8: "Four of a Kind",
        7: "Full House",
        6: "Flush",
        5: "Straight",
        4: "Three of a Kind",
        3: "Two Pair",
        2: "One Pair",
        1: "High Card",
    }

    # Pack of cards
    def new_pack():
        """
        Build a standard 52-card pack.

        Returns:
            list[tuple[int, str]]: List of cards where each card is (rank, suit),
            rank in [2..14] (14 = Ace), suit in {'♣','♦','♥','♠'}.
        """
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append((rank,suit))
        return deck
    pack_of_cards = new_pack()
    random.shuffle(pack_of_cards)
    #Card
    # a = random.choice(pack_of_cards)

    def card_str(card):
        """
           Convert a card tuple to a short human-readable string.

           Args:
               card (tuple[int, str]): The card as (rank, suit).

           Returns:
               str: e.g., "A♠", "10♦", "J♥".
           """
        r, s = card
        return f"{ranks_string.get(r, r)}{s}"

    def deal(n):
        """
           Pop and return n cards from the global shuffled pack.

           Args:
               n (int): Number of cards to deal.

           Returns:
               list[tuple[int, str]]: A list of n cards (rank, suit).

           Side Effects:
               Mutates `pack_of_cards` by popping from the end.
           """
        return [pack_of_cards.pop() for _ in range(n)]
    your_cards = deal(2)
    # print(your_cards)
    bot_cards = deal(2)
    Flop = deal(3)
    Turn = deal(1)
    River = deal(1)

    # print(' - '.join(card_str(i)for i in your_cards)) -> Card output
    def show(x):

        y = (' - '.join(card_str(c) for c in x))
        return y
    ##Draw
    def ascii_card(rank, suit):
        """
          Render a single card as a list of ASCII-art lines.

          Args:
              rank (int): 2..14 (11=J,12=Q,13=K,14=A).
              suit (str): One of {'♣','♦','♥','♠'}.

          Returns:
              list[str]: 5 lines forming a boxed ASCII card.
                         Use together with `show_hand` to print side-by-side.
          """
        suit_symbol = {
            '♠': '♠',
            '♥': '♥',
            '♦': '♦',
            '♣': '♣'
        }
        rank_str = {11: "J", 12: "Q", 13: "K", 14: "A"}.get(rank, str(rank))
        s = suit_symbol[suit]

        return [
            "┌───────┐",
            f"│{rank_str:<2}     │",
            f"│   {s}   │",
            f"│     {rank_str:>2}│",
            "└───────┘"
        ]

    def show_hand(cards):
        """
          Print multiple ASCII cards side-by-side.

          Args:
              cards (list[tuple[int, str]]): Cards to render, each (rank, suit).

          Output:
              Prints to stdout the combined ASCII-art of all cards.
          """
        ascii_cards = [ascii_card(r, s) for (r, s) in cards]
        for row in zip(*ascii_cards):
            print("  ".join(row))

    # board = [show(Flop), show(Turn), show(River)]
    board = [Flop, Turn, River]
    street = []
    idx = -1
    #Main Gameplay
    print('[PRE-FLOP]')
    print('Your card: ')

    # print('Your cards: ',show(your_cards))
    show_hand(your_cards)
    while True:
        idx = idx + 1
        lst = ['FLOP', 'TURN', 'RIVER']
        for i in board[idx]:
            street.append(i)
        # street.append(board[idx])
        if input('Press enter to continue...: ') == '':

            print(f'{lst[idx]}')
            print('Your card: ')
            show_hand(your_cards)
            print('Board: ')
            show_hand(street)
            # print(f'Board: {street}')
            if idx == 2:
                break
    #Whole
    your_whole = your_cards + Flop + Turn + River
    # for i in your_cards:
    #     whole.append(i)
    # for i in Flop:
    #     whole.append(i)
    # for i in Turn:
    #     whole.append(i)
    # for i in River:
    #     whole.append(i)
    # print('whole=',your_whole)

    from collections import Counter

    ranks7 = [r for r, s in your_whole]
    suits7 = [s for r, s in your_whole]

    rc = Counter(ranks7)   #Count by rank
    sc = Counter(suits7)   #Count by suit
    # print('ranks7=',rc)
    # print('suits7=',sc)
    #Pair
    pair = [r for r, c in rc.items() if c >= 2]
    # print('pair=',pair)
    #Triple
    triple = [r for r,c in rc.items() if c >= 3]
    # print('triple=',triple)
    #Four of a Kind
    four = [r for r,c in rc.items() if c ==4]
    # print('four=',four)
    #Flush
    flush = [s for s,c in sc.items() if c >= 5]
    # print('flush=',flush)
    pairs = sorted([r for r,c in rc.items() if c == 2], reverse=True)
    trips = sorted([r for r,c in rc.items() if c == 3], reverse=True)
    # Straight
    r = []
    s = []
    for i in your_whole:
        a, b = i
        r.append(a)
        s.append(b)
    r = set(r)
    s = set(s)
    r = list(r)
    s = list(s)
    r.sort(reverse=True)

    # print('r=',r)
    def straight():
        """
         Detect straight or straight flush from player's 7 cards.

         Logic:
             - Check straight flush/royal flush by scanning ranks within any flush suit.
             - Then check normal straight using unique sorted ranks.
             - Straight wheel (A-2-3-4-5) is NOT considered.

         Returns:
             tuple:
                 (kind, high, sequence)
                 - kind (str): 'Royal Flush', 'Straight Flush', 'Normal straight', or 'Not Straight'
                 - high (int): Highest rank of the straight (e.g., 14 for A-high), or a fallback top rank.
                 - sequence (list[int]): Ranks of the found straight window, or the unique rank list when not found.

         Notes:
             Uses outer-scope variables `your_whole` and `flush`.
         """
        for fs in flush:
            suit_ranks = sorted({rr for (rr, ss) in your_whole if ss == fs}, reverse=True) #To get the number with the same suit by flush
            for i in range(len(suit_ranks) - 4):
                w = suit_ranks[i:i + 5]
                if all(w[j] - 1 == w[j + 1] for j in range(4)):
                    if w[0] == 14:
                        return 'Royal Flush', 14, w
                    else:
                        return 'Straight Flush', w[0], w
        for i in range(len(r) - (5 - 1)):
            window = r[i:i + 5]
            if all(window[j] - 1 == window[j + 1] for j in range(4)):
                return 'Normal straight', window[0], window
        else:
                return 'Not Straight', r[0], r

    #Main mechanic of game
    ##What you got
    if straight()[0] == 'Royal Flush':
        Bool, High, Straight = straight()
        rank = 10,High
    elif straight()[0] == 'Straight Flush':
        Bool, High, Straight = straight()
        rank = 9, High
    elif len(four) >=1:
        rest = sorted(set(ranks7), reverse=True)
        rest.remove(four[0])
        kicker = rest[0]
        rank = 8, max(four), kicker
    elif len(trips) >= 2:
            rank = (7, trips[0], trips[1])  # Highest trips + Next Trips
    elif trips and pairs:
            rank = (7, trips[0], pairs[0])  # trips + Highest pair
    elif len(flush) >=1:
        for fs in flush:
            rank_in_fs = [r for (r, s) in your_whole if s == fs]
            rank_in_fs.sort(reverse=True)
            rank = 6, rank_in_fs[:5]
    elif straight()[0] == 'Normal straight':
        Bool, High, Straight = straight()
        rank = 5, High
    elif len(triple) >=1:
        rest = sorted(set(ranks7), reverse=True)
        rest.remove(triple[0])
        kicker = rest[:2]
        k1, k2 = kicker
        rank = 4, max(triple), k1, k2
    elif len(pair) >= 2:
        rest = sorted(set(ranks7), reverse=True)
        pair.sort(reverse=True)
        rest.remove(pair[0])
        rest.remove(pair[1])
        rank = 3, pair[0],pair[1],max(rest)
    elif len(pair) >= 1:
        rest = sorted(set(ranks7), reverse=True)
        rest.remove(pair[0])
        kicker = rest[:3]

        rank = 2, pair[0], kicker
    else:
        card = r[:5]
        rank = 1, card

    # print(50*'=')
    # print(f'Bot cards {show(bot_cards)}')
    ##What Bot Got
    #Bot Whole
    bot_whole = bot_cards + Flop + Turn + River

    # print('Bot whole=',bot_whole)

    from collections import Counter

    ranksbots7 = [r for r, s in bot_whole]
    suitsbots7 = [s for r, s in bot_whole]

    rcbot = Counter(ranksbots7)
    scbot = Counter(suitsbots7)
    # print('ranks7=',rcbot)
    # print('suits7=',scbot)
    #Pair
    pairbot = [r for r, c in rcbot.items() if c >= 2]
    # print('pairbot=',pairbot)
    #Triple
    triplebot = [r for r,c in rcbot.items() if c >= 3]
    # print('triplebot=',triplebot)
    #Four of a Kind
    fourbot = [r for r,c in rcbot.items() if c ==4]
    # print('fourbot=',fourbot)
    #Flush
    flushbot = [s for s,c in scbot.items() if c >= 5]
    # print('flushbot=',flushbot)
    pairsbot = sorted([r for r,c in rcbot.items() if c == 2], reverse=True)
    tripsbot = sorted([r for r,c in rcbot.items() if c == 3], reverse=True)
    # Straight
    rbot = []
    sbot = []
    for i in bot_whole:
        a, b = i
        rbot.append(a)
        sbot.append(b)
    rbot = set(rbot)
    sbot = set(sbot)
    rbot = list(rbot)
    sbot = list(sbot)
    rbot.sort(reverse=True)
    # print('r=',r)
    def straightbot():
        """
        Same logic with straight() function.
        """
        for fs in flushbot:
            suit_ranks = sorted({rr for (rr, ss) in bot_whole if ss == fs}, reverse=True)
            for i in range(len(suit_ranks) - 4):
                w = suit_ranks[i:i + 5]
                if all(w[j] - 1 == w[j + 1] for j in range(4)):
                    if w[0] == 14:
                        return 'Royal Flush', 14, w
                    else:
                        return 'Straight Flush', w[0], w
        for i in range(len(rbot) - (5 - 1)):
            window = rbot[i:i + 5]
            if all(window[j] - 1 == window[j + 1] for j in range(4)):
                return 'Normal straight', window[0], window
        else:
                return 'Not Straight', rbot[0], rbot
    if straightbot()[0] == 'Royal Flush':
        Bool, High, Straight = straightbot()
        rankbot = 10,High
    elif straightbot()[0] == 'Straight Flush':
        Bool, High, Straight = straightbot()
        rankbot = 9, High
    elif len(fourbot) >=1:
        rest = sorted(set(ranksbots7), reverse=True)
        rest.remove(fourbot[0])
        kicker = rest[0]
        rankbot = 8, max(fourbot), kicker
    elif len(tripsbot) >= 2:
            rankbot = (7, tripsbot[0], tripsbot[1])  # Highest trips + Next Trips
    elif tripsbot and pairsbot:
            rankbot = (7, tripsbot[0], pairsbot[0])  # trips + Highest pair
    elif len(flushbot) >=1:
        for fs in flushbot:
            rank_in_fs = [r for (r, s) in bot_whole if s == fs]
            rank_in_fs.sort(reverse=True)
            rankbot = 6, rank_in_fs[:5]
    elif straightbot()[0] == 'Normal straight':
        Bool, High, Straight = straightbot()
        rankbot = 5, High
    elif len(triplebot) >=1:
        rest = sorted(set(ranksbots7), reverse=True)
        rest.remove(triplebot[0])
        kicker = rest[:2]
        k1, k2 = kicker
        rankbot = 4, max(triplebot), k1, k2
    elif len(pairbot) >= 2:
        rest = sorted(set(ranksbots7), reverse=True)
        pairbot.sort(reverse=True)
        rest.remove(pairbot[0])
        rest.remove(pairbot[1])
        rankbot = 3, pairbot[0], pairbot[1], max(rest)
    elif len(pairbot) >= 1:
        rest = sorted(set(ranksbots7), reverse=True)
        rest.remove(pairbot[0])
        kicker = rest[:3]
        rankbot = 2, pairbot[0], kicker
    else:
        card = rbot[:5]
        rankbot = 1, card

    print(f'You have got a/an {CATEGORY_NAME.get(rank[0])}')
    print(f'Bot has got a/an {CATEGORY_NAME.get(rankbot[0])}')
    print(f'Bot Cards: {show(bot_cards)}')

    #Comparison
    if rank[0:] > rankbot[0:]:
        print("Congratulations! You won!")
        achv_dict["poker"][1] -= 1
        into_team2( player1, player2,None)
        # show_poke(main_pokemon_file.Sam)
        # print('Kari')
        # show_poke(main_pokemon_file.Kari)
    elif rank[0:] < rankbot[0:]:
        print("Hahahaha Loserrrr ")
        lose_poke(player1 ,player2 )

    elif rank[0:] == rankbot[0:]:
        print('DRAWW')
        a = input("Do you wanna play again? (y/n)")
        if a == 'y':
            poker(player1, player2)
        elif a == 'n':
            print("Fine")



def into_team2(player, opo, wild):
    """
    The inner function used for stealing or capturing Pokemon, the function
    creates a loop until you enter 0 that allows you to move the opposing
    Pokemon into your team, and moves excess Pokemon into the wild list
    :param player: player
    :param opo: opponent whose team to check, write None if capturing wild Pokemon
    :param wild: wild pokemon, write None if battling human NPC
    :return: None
    """
    if wild == None:
        while True:
            if len(player.team) < 6:
                while len(player.team) < 6 and len(opo.team) > 0:
                    print(f"{opo.team[0].name} was added to your team.")
                    player.team.append(opo.team[0])
                    opo.team.remove(opo.team[0])
                break
            else:
                d_print("Which Pokemon would you like to add to your team?\n")
                for index_o, poke_o in enumerate(opo.team):
                    print(f"{index_o + 1}. {poke_o.name}")
                print(f"0. End")
                user_input_opo = input("Select your choice: ")
                try:
                    test_1 = int(user_input_opo)
                except ValueError:
                    print("Invalid input")
                    continue
                if 0 < int(user_input_opo) <= len(opo.team):
                    d_print("Which Pokemon from your team would you like to release?\n")
                    for index_p, poke_p in enumerate(player.team):
                        print(f"{index_p + 1}. {poke_p.name}")
                    print(f"0. End")
                    user_input_player = input("Select your choice: ")
                    try:
                        test_01 = int(user_input_player)
                    except ValueError:
                        print("Invalid input")
                        continue
                    if 0 < int(user_input_player) <= len(player.team):
                        wild_poke.append(player.team[int(user_input_player) - 1])
                        player.team[int(user_input_player) - 1] = opo.team[int(user_input_opo) - 1]
                        opo.team.remove(opo.team[int(user_input_opo) - 1])
                    elif int(user_input_player) == 0:
                        if len(opo.team) > 0:
                            for index, poke in enumerate(opo.team):
                                wild_poke.append(opo.team[index])
                                opo.team.remove(opo.team[index])
                        d_print("Stealing ended\n")
                        break
                    else:
                        print("Invalid input")
                elif int(user_input_opo) == 0:
                    if len(opo.team) > 0:
                        for index, poke in enumerate(opo.team):
                            wild_poke.append(opo.team[index])
                            opo.team.remove(opo.team[index])
                    d_print("Stealing ended\n")
                    break
                else:
                    print("Invalid input")
    elif opo == None:
        while True:
            d_print("Which Pokemon from your team would you like to release?\n")
            for index_p, poke_p in enumerate(player.team):
                print(f"{index_p + 1}. {poke_p.name}")
            print(f"0. End")
            user_input_player = input("Select your choice: ")
            try:
                test_01 = int(user_input_player)
            except ValueError:
                print("Invalid input")
                continue
            if 0 < int(user_input_player) <= len(player.team):
                wild_poke.append(player.team[int(user_input_player) - 1])
                player.team[int(user_input_player) - 1] = wild
                wild_poke.remove(wild)
                break
            elif int(user_input_player) == 0:
                print("Capture ended")
                break
            else:
                print("Invalid input")



def lose_poke(player,opo):
    d_print("The opponent stole one od your Pokemon, you ran off!")
    if len(player.team) > 0:
        take = random.choice(player.team)
        player.team.remove(take)
        opo.team.append(take)
        wild_poke.append(take)



def villain_interaction(player, villain):
    """
    Function for interacting with a villain when player lands on an airport
    with an anomaly.
    :param player:
    :param villain:
    :return:
    """
    d_print(f"{villain.name}: {random.choice(villain_intro)}\n")
    d_print(f"{villain.name}: {random.choice(wdyw_line)}\n")
    print("""1. Battle
2. Play Poker
3. Play Russian Roulette
0. Exit""")
    while True:
        while True:
            user_input = input("Select your choice: ")
            try:
                input_check = int(user_input)
                break
            except ValueError:
                print("Invalid input")
                continue
        if user_input == "1": # Battle
            d_print(random.choice(battle_intro_line) + "\n")
            time.sleep(1)
            trainer_battle(player, villain)
            if len(villain.team) <= 0:
                d_print(f"{villain.name} surrendered and have given themselves to the police.\n")
                if len(villain.team) < 0:
                    villain_list.remove(villain)
                    wild_pokemon_assigner(player, evil_poke)
            break
        elif user_input == "2": # Poker
            d_print(random.choice(poker_intro_line) + "\n")
            time.sleep(1)
            poker(player, villain)
            if len(villain.team) <= 0:
                d_print(f"{villain.name} surrendered and have given themselves to the police.\n")
                # ACHV DICT ALREADY MODIFIED IN THE POKER FUNCTION
                if len(villain.team) < 0:
                    villain_list.remove(villain)
                    wild_pokemon_assigner(player, evil_poke)
            break
        elif user_input == "3": # Roulette
            d_print(random.choice(roulette_intro_line) + "\n")
            time.sleep(1)
            start_rr_game(player, villain)
            if len(villain.team) <= 0:
                d_print(f"{villain.name} surrendered and have given themselves to the police.\n")
                if len(villain.team) < 0:
                    achv_dict["rr"][1] -= 1
                    villain_list.remove(villain)
                    wild_pokemon_assigner(player, evil_poke)
            break
        elif user_input == "0":
            d_print(random.choice(leave_chat_line) + "\n")
            break
        else:
            print(random.choice(invalid_selection_line))



def villain_gen() -> list:
    """
    Generates a list of villains
    :return: list of villains
    """
    villain_1 = Human("Lady Gaga", "grunt")
    villain_2 = Human("Zandaya", "grunt")
    villain_3 = Human("Beyonce", "grunt")
    villain_4 = Human("P Diddy", "manager")
    villain_5 = Human("Taylor Swift", "manager")
    villain_6 = Human("Elon Musk", "exec")
    villain_7 = Human("Sydney Sweeney", "exec")
    villain_8 = Human("Ed Sheeran", "exec")
    villain_human_list = [villain_1, villain_2, villain_3, villain_4, villain_5, villain_6, villain_7, villain_8]
    return villain_human_list



def character_creator():
    """
    Creates the player and assigns them their first Pokemon
    :return:
    """
    player_name = input("Enter Your Name: ")
    player = Human(str(player_name), "player")
    d_print(f"Welcome, {player.name}.\n")
    print("""Select your partner Pokemon:
    1. Venusaur
    2. Charizard
    3. Blastoise
    """)
    while True:
        while True:
            no_select = input("Choose your starter: ")
            try:
                test = int(no_select)
                break
            except ValueError:
                print("Invalid input")
        if int(no_select) == 1:
            poke_select = all_pokemon_list.Venusaur
            d_print(f"You chose {poke_select.name}.\n")
            player.team.append(poke_select)
            d_print(f"{player.team[0].name} has been added to your party\n")
            break
        elif int(no_select) == 2:
            poke_select = all_pokemon_list.Charizard
            d_print(f"You chose {poke_select.name}.\n")
            player.team.append(poke_select)
            d_print(f"{player.team[0].name} have been added to your party\n")
            break
        elif int(no_select) == 3:
            poke_select = all_pokemon_list.Blastoise
            d_print(f"You chose {poke_select.name}.\n")
            player.team.append(poke_select)
            d_print(f"{player.team[0].name} have been added to your party\n")
            break
        else:
            print("Invalid selection")
            continue
    return player



def tutorial(player):
    """
    Tutorial scenario to be run at the beginning of the game after character_creator
    :param player:
    :return:
    """
    print("=" * 100)
    print("")
    d_print(f"""News Anchor: This just in, 8 airports around the world have been
reported to being attacked by a terrorist organisation. We dont know their
motives but the international police have apprehended a 23 year old former 
Pokemon Champion, {player.name}, now stripped of their title, suspected to
be the criminal mastermind behind these attacks.\n""")
    print("")
    d_print(f"""News Anchor: {player.name}'s PC has been disabled, and their Pokemon
confiscated. Police found a device that lets a trainer steal another trainer's 
Pokemon, called a 'Snag Em' gear, and  will begin interroga... wait! What's this? 
I've just received a report that a {player.team[0].name} just burst out of its 
Pokeball in the police department where {player.name} is being held.\n""")
    # SLEEP
    print("")
    d_print("""You escaped the detention center with only one Pokemon in your 
party and the Snag Em gear.\n""")
    #SLEEP
    print("")
    input("--Press Enter to continue--")
    print("=" * 100)
    print()
    d_print("""You somehow made it to the airport. It's empty, everyone had been
evacuated due to the terrorist threats. They upped the the security, but you 
were able to make it past most of the guards. If only you could get to your
plane then you would be able to...\n""")
    print("")
    time.sleep(1)
    print("Police Officer Jeffrey Dahmer: HOLD IT RIGHT THERE!!!")
    time.sleep(3)
    print("")
    d_print("Oh no...\n")
    print()
    time.sleep(1)
    input("--Press Enter to continue--")
    print("")
    d_print(f"""Dahmer: {player.name}, you are under arrest! Unlike other criminals
like you, I'm not playing by the rules. I won't accept a challenge in a game
of Poker, or Russian Roulette. Don't bother with the command /HELP either,
that's only useful once you played past the tutorial.\n""")
    print()
    d_print("How will you respond?\n")
    print("""1. Challenge the Police Officer Jeffrey Dahmer to a Pokemon Battle.
2. Tell Dahmer that he is legally obligated to battle you before arresting you.
3. He's a cop, he is probably crooked anyway, so as a criminal, he has moral 
obligations to comply with the criminal code of conduct but hes so crooked, he 
probably doesn't care.""")
    input("Select your choice: ")
    d_print("""\nDahmer: Dont underestimate me, I am aware that when battling, 
that my command to my Pokemon is case sensitive, or my Pokemon will get confused 
and freeze.\n""")
    print("=" * 100)
    trainer_battle(player, Dahmer)
    if len(player.team) > 0:
        d_print("""Dahmer: If I had more Pokemon, I could have swapped out 
Pokemon by using the SWAP command when it was my turn.\n""")
    all_poke_heal(player)
    print()
    d_print("=" * 100 + "\n")
    print()
    d_print("""You quickly make your way to your airplane, the runway is empty
so you easily took off without worrying about collision with another
plane in the area.\n""")
    print()
    d_print("=" * 100)
    print("\n")
    print("-beep beep-")
    d_print(f"""Ed Sheeran: Hey man, I saw what happened to you on the news, this
is so unfair. I think you should lay low for now, don't draw any 
attention to yourself and go into hiding.\n-bzz- *click*""")
    print("\n")
    d_print("""I guess he got cut off.. You can either take your friend's 
advice, or... you can clear your name and defeat all 8 terrorists scattered
throughout the world. Surely, if you defeat all 8 of them, you will be 
pardoned of all misunderstandings.\n""")
    print("=" * 100 + "\n")
    # USE DUY'S FLIGHT AIMATION HERE 3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    time.sleep(2)


def arceus_encounter():
    """
    Used for when the player triggers an Arceus encounter after playing
    Russian Roulette 2 times.
    :return: None
    """
    if Arceus not in wild_poke and Arceus not in player.team:
        wild_encounter_battle(player.team[0], player, arceus_list)



arceus_list = [Arceus]
wild_poke = []
evil_poke = []
player_achv = []
villain_list = villain_gen()


Sam = Human("Sam", "exec")
Meeri = Human("Meeri", "cop")
Dahmer = Human("Police Officer Dahmer", "cop")
player = character_creator()
tutorial(player)
# print(villain_list[0].name)
# print(villain_list[0].team)
# for pokemon in villain_list[4].team:
#     print(pokemon.name)
# villain_interaction(player, villain_list[0])
#
# for pokemon in player.team:
#     print(pokemon.name)
# # print(player_achv)
# print(achv_dict["poker"][1])

# all_poke_heal(player)
# villain_interaction(player, villain_list[0])
#
# all_poke_heal(player)
# wild_encounter_battle(player.team[0], player, wild_poke)


# distance = "calculate_distance(A,B,C,D)"
distance = 5000


# for i in range(10):
#     flight_cost(distance)
#     achievement_check(achv_dict, player_achv)
#     print(player_achv)
#     print(player.fuel)

###############################################################3 TEST

def second_menu(input_sec, player):
    choice = str(input_sec).strip().casefold()

    if choice == "a" or choice.casefold() == "menu":
        print("=" * 120)
        print("PLACE HOLDER MENU FOR MENU")
        a_menu = input("Press Enter to continue")
        print("=" * 120)
        if a_menu.casefold() == "exit":
            return "exit"
        return None
    elif choice == "b" or choice.casefold() == "bag":
        print("=" * 120)
        print("PLACE HOLDER MENU FOR BAG")
        input("Press Enter to continue")
        print("=" * 120)
        return None
    elif choice == "c" or choice.casefold() == "stats":
        print("=" * 120)
        print("Pokemon List:")
        for index, pokemon in enumerate(player.team):
            print(f"{index + 1}. {pokemon.name} "
                  f"[{pokemon.health}/{pokemon.max_health}]"
                  f" - Attacks: [{pokemon.atk_1:^16}] [{pokemon.atk_2:^16}]"
                  f" [{pokemon.atk_3:^16}] [{pokemon.atk_4:^16}]")
        input("Press Enter to continue")
        print("=" * 120)
        return None
    elif choice == "d" or choice.casefold() == "achievements":
        print("=" * 120)
        for index, achv in enumerate(player_achv):
            print(f"{index + 1}. {achv}")
        input("Press Enter to continue")
        print("=" * 120)
        return None
    elif input_sec == "PAYDAY" and Meowth not in player.team:
        print("=" * 120)
        print("[YOU RECEIVED MEOWTH]") # Saved for later MIGHT REMOVE
        if len(player.team) == 6:
            into_team(player, None, Meowth)
        else:
            wild_capture(Meowth, player)
        input("Press Enter to continue")
        print("=" * 120)
        return None
    elif input_sec == "I choose you!" and Pikachu not in player.team:
        print("=" * 120)
        print("[YOU RECEIVED PIKACHU]") # Saved for later MIGHT REMOVE
        if len(player.team) == 6:
            into_team(player, None, Pikachu)
        else:
            wild_capture(Pikachu, player)
        input("Press Enter to continue")
        print("=" * 120)
        return None
    else:
        print("=" * 120)
        print("Please enter a valid input.")
        input("Press Enter to continue")
        print("=" * 120)
        return None



def travel_menu(input_travel, player):
    choice = int(input_travel)
    if choice == 1:
        print("=" * 120)
        print("PLACE HOLDER MENU FOR TRAVEL OPTION 1")
        villain_interaction(player, villain_list[0])
        input("Press Enter to continue")
        print("=" * 120)
    elif choice == 2:
        print("=" * 120)
        print("PLACE HOLDER MENU FOR TRAVEL OPTION 2")
        input("Press Enter to continue")
        print("=" * 120)
    elif choice == 3:
        print("=" * 120)
        print("PLACE HOLDER MENU FOR TRAVEL OPTION 3")
        input("Press Enter to continue")
        print("=" * 120)
    elif choice == 0 or choice == "FREE FLIGHT":
        print("=" * 120)
        print("PLACE HOLDER MENU FOR FREE FLIGHT")
        input("Press Enter to continue")
        print("=" * 120)
    else:
        print("=" * 120)
        print("Please enter a valid input.")
        input("Press Enter to continue")
        print("=" * 120)



def main_menu(player):
    while True:
        print("Airplane: " + str(player.health) + "/300")
        print("Fuel: " + str(player.fuel) + "/100")
        print("Location: " + str(player.location))
        print("Airport Distress Signals: ")
        if len(distress_list) > 0:
            for index, distress in enumerate(distress_list[0:3]):
                print(str(index) + distress_list[distress])
        else:
            print("[None]")
        print("\n" * 4)
        print("Travel: ")
        if len(airport_range_list) > 0:
            for index, airport in enumerate(airport_range_list[0:3]):
                print(str(index +1) + ". " + airport)
        else:
            print("[No airport within landing range]")
        print("0. Free Flight")
        print("-" * 120)
        print("A. Open Menu")
        print("B. Open Bag")
        print("C. Pokemon Stats")
        print("D. Open Achievements")
        main_input = input("Enter choice: ")
        if main_input.isdigit():
            travel_menu(main_input, player)
        else:
            if second_menu(main_input, player) == "exit":
                print("-Session Ended-")
                break





airport_range_list = ["Thailand, Suvarnabhumi International Airport [Longitude, Latitude] NW 354°",
                "Cambodia, Phnom Penh International Airport [Longitude, Latitude] NW 340°",
                "Vietnam, Noi Bai International Airport [Longitude, Latitude] NE 112°",
                "Singapore, Changi Airport [Longitude, Latitude] NE 170°",
]

distress_list = []

main_menu(player)