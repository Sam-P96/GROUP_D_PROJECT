def second_menu(input_sec):
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
        print("PLACE HOLDER MENU FOR STATS")
        input("Press Enter to continue")
        print("=" * 120)
        return None
    elif choice == "d" or choice.casefold() == "achievements":
        print("=" * 120)
        print("PLACE HOLDER MENU FOR ACHIEVEMENTS")
        input("Press Enter to continue")
        print("=" * 120)
        return None
    elif input_sec == "PAYDAY":
        print("=" * 120)
        print("[YOU RECEIVED MEOWTH]") # Saved for later MIGHT REMOVE
        input("Press Enter to continue")
        print("=" * 120)
        return None
    else:
        print("=" * 120)
        print("Please enter a valid input.")
        input("Press Enter to continue")
        print("=" * 120)
        return None


def travel_menu(input_travel):
    choice = int(input_travel)
    if choice == 1:
        print("=" * 120)
        print("PLACE HOLDER MENU FOR TRAVEL OPTION 1")
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
        print("C. Player & Pokemon Stats")
        print("D. Open Achievements")
        main_input = input("Enter choice: ")
        if main_input.isdigit():
            travel_menu(main_input)
        else:
            if second_menu((main_input)) == "exit":
                print("-Session Ended-")
                break



class Player:
    def __init__(self, name):
        self.health = 300
        self.fuel = 100
        self.location = ["60.3179° N", "24.9496° E"]



airport_range_list = ["Thailand, Suvarnabhumi International Airport [Longitude, Latitude] NW 354°",
                "Cambodia, Phnom Penh International Airport [Longitude, Latitude] NW 340°",
                "Vietnam, Noi Bai International Airport [Longitude, Latitude] NE 112°",
                "Singapore, Changi Airport [Longitude, Latitude] NE 170°",
]

distress_list = []

Sam = Player("Sam")

main_menu(Sam)
