import random
from type_chart_factor import type_bonus_dict
from attack_dict import attack_dict
from all_pokemon_list import Arceus
from all_pokemon_list import LC_Poke
from all_pokemon_list import NU_Poke
from all_pokemon_list import OU_Poke
from all_pokemon_list import Uber_Poke

# Include these at the top of the program

arceus_list = [Arceus]
wild_poke = []
evil_poke = []


class Human:
    def __init__(self, name: str, rank: str):
        self.name = name
        self.rank = rank
        self.health = 100
        self.team = []
        self.exclude = set()
        self.team_p = []
        self.exclude_p = set()
        if rank == "intern":
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
        print(f"{self.name} used {key} on {player_2.name}! [{dmg_out}]")
        if float(type_bonus(key, player_2)) > 1.5:
            print("Its super effective!")
        elif float(type_bonus(key, player_2)) == 0:
            print(f"{player_2.name} is immune to {key}")
        elif float(type_bonus(key, player_2)) < 1:
            print("Its not very effective!")
        # + str(player_2.health) + " " + str(dmg_out))



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
            p_select = input("Select your Pokemon")
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
        while sacrifice in self.team and player_2.team[0] in player_2.team:
            for turn in player_list:
                print("*Spinning the barrel*")
                bullet = random.randint(1, 2)
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
                        try:
                            print(f"{player_2.team[0].name} steps up in its trainer's place.")
                        except:
                            print(f"{player_2.name} is out of Pokemon.")
                    input("Press enter to continue")
                    print("=" * 100)
                    player_team_hp = team_health_check(self)
                    opo_team_hp = team_health_check(player_2)
                    break
            break

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
            print("Which Pokemon would you like to add to your team?")
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
                print("Which Pokemon from your team would you like to release?")
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
                    player.team[int(user_input_player) - 1] = opo.team[int(user_input_opo) - 1]
                    opo.team.remove(opo.team[int(user_input_opo) - 1])
                    wild_poke.append(player.team[int(user_input_player) - 1])
                elif int(user_input_player) == 0:
                    print("Stealing ended")
                    break
                else:
                    print("Invalid input")
            elif int(user_input_opo) == 0:
                print("Stealing ended")
                break
            else:
                print("Invalid input")
    elif opo == None:
        while True:
            print("Which Pokemon from your team would you like to release?")
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
                player.team[int(user_input_player) - 1] = wild
                wild_poke.remove(wild)
                wild_poke.append(player.team[int(user_input_player) - 1])
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
            print(f"You defeated the {wild.name}, it started following you.")
            player.team.append(wild)
            break
        else:
            print("""You cannot have more than 6 Pokemon, and you do not have 
legal access to a PC to store excess Pokemon.""")
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
        print("""You won! In the Sacred Book of Criminal Law Section 4.213, rules all 
hardened criminals abide by, you may take their Pokemon. Since you 
are an outlaw you do not have access to a PC. So if you have more than 
6 Pokemon, you must choose one Pokemon to release when adding one 
to your team.""")
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
    print(f"A wild {wild_mon.name} appeared!!")
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
            game_russian(Sam, Meeri)
            break
        elif y_n == 2:
            print("You left the interaction.")
            break
        else:
            print("Invalid input")














# print(len(Uber_Poke))
Ethan = Human("Ethan", "player")
Sam = Human("Sam", "exec")
Meeri = Human("Meeri", "intern")
Saara = Human("Saara", "grunt")
Kari = Human("Kari", "exec")

# for i in range(3):
#     Ethan.team.append(OU_Poke)
# wild_pokemon_assigner(Ethan, evil_poke)
# print(len(Ethan.team))
# print(len(wild_poke))
# print(len(evil_poke))



# from  villain_npc import Sam
# from villain_npc import Meeri
#
sam_list = []
for pokemon in Sam.team:
    sam_list.append(pokemon.name)
print(sam_list)
#
# meeri_list = []
# for pokemon in Meeri.team:
#     meeri_list.append(pokemon.name)
# print(meeri_list)



# start_rr_game(Sam, Meeri)

# trainer_battle(Sam, Meeri)
#
#
# wild_encounter_battle(Sam.team[0]
# all_poke_heal(Sam)
# wild_encounter_battle(Sam.team[0], Sam, wild_poke)

sam_list = []
for pokemon in Sam.team:
    sam_list.append(pokemon.name)
print(sam_list)
