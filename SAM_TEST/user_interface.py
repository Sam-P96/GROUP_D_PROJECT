from main_pokemon_file import player
from main_pokemon_file import player_achv
from main_pokemon_file import into_team
from all_pokemon_list import Meowth
from all_pokemon_list import Pikachu
from main_pokemon_file import wild_capture
from main_pokemon_file import villain_interaction
from main_pokemon_file import Meeri
from main_pokemon_file import villain_list
import main_pokemon_file

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


# main_menu(player)
print(villain_list)
