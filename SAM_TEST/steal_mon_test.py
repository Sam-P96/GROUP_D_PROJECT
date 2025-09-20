

def into_team(player, opo, wild):
    if wild == None:
        while True:
            print("Which Pokemon would you like to add to your team?")
            for index_o, poke_o in opo.team:
                print(f"{index_o}. {poke_o.name}")
                print(f"0. End")
                user_input_opo = input("Select your choice: ")
                if 0 < int(user_input_opo) <= len(opo.team):
                    print("Which Pokemon from your team would you like to release?")
                    for index_p, poke_p in player.team:
                        print(f"{index_p}. {poke_p.name}")
                        print(f"0. End")
                        user_input_player = input("Select your choice: ")
                        if 0 < int(user_input_player) <= len(player.team):
                            player.team[int(user_input_player)] = opo.team[user_input_opo]
                            opo.team.remove(opo.team[user_input_opo])
                        elif user_input_player == 0:
                            print("Stealing ended")
                        else:
                            print("Invalid input")
                elif user_input_opo == 0:
                    print("Stealing ended")
                else:
                    print("Invalid input")
    elif opo == None:
        print("Which Pokemon from your team would you like to release?")
        for index_p, poke_p in player.team:
            print(f"{index_p}. {poke_p.name}")
            print(f"0. End")
            user_input_player = input("Select your choice: ")
            if 0 < int(user_input_player) <= len(player.team):
                player.team[int(user_input_player)] = wild
                wild_poke.remove(wild)
            elif user_input_player == 0:
                print("Capture ended")
            else:
                print("Invalid input")



def wild_capture(wild, player):
    while True:
        if player.team < 6:
            print(f"You defeated the {wild.name}, it started following you.")
            player.team.append(wild)
            break
        else:
            print("""You cannot have more than 6 Pokemon, and you do not have 
            legal access to a PC to store excess Pokemon.""")
            print("Would you like to capture this Pokemon?")
            print("1. Yes")
            print("2. No")
            y_n = input("Select your choice:")
            if y_n.casefold() == "yes" or y_n == 1:
                into_team(player, None, wild)
                break
            if y_n.casefold() == "no" or y_n == 2:
                break
            else:
                print("Invalid input")



def battle_steal(player, opo):
    first_time = 1
    while first_time >= 1 and len(player.team) >= 6:
        print("""You won! In the Sacred Book of Criminal Law Section 4.213, rules all 
        hardened criminals abide by, you may take their Pokemon. Since you 
        are an outlaw you do not have access to a PC. So if you have more than 
        6 Pokemon, you must choose one Pokemon to release when adding one 
        to your team.""")
        first_time -= 1
        into_team(player, opo, None)
