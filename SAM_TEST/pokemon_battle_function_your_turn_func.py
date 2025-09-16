import random
import pokedex_player
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



def your_battle_turn(your_mon, opo_mon):
    your_att = input("Select your attack: ")
    if your_att == "SWAP":
        new_mon = swap_out(your_mon, opo_mon)
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



def swap_out(current, opponent):
    return choose_switch_from_team(poke_team, exclude = current, prompt = "Who do you want to swap to?")



def pokemon_battle(your_mon, opo_mon):
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
                battle_input = your_battle_turn(your_mon, opo_mon)
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
                battle_input = your_battle_turn(your_mon, opo_mon)
                if battle_input[0] == "switch":
                    your_mon = battle_input[1]

        if your_mon.health <= 0:
            print("=" * 100)
            print(f"{str(your_mon.name) + " [lv." + str(your_mon.lvl) + "]":<40} "
                  f"{str(opo_mon.name) + " [lv." + str(opo_mon.lvl)}]")
            print(f"{poke_hp_bar(your_mon):<41}{poke_hp_bar(opo_mon)}")
            print(f"HP:{"0":<38}HP:{opo_hp_str}")
            print(f"Your {your_mon.name} fainted!")
            replacement = choose_switch_from_team(poke_team, exclude=your_mon,
            prompt = "Who will you send out next?! ")
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




all_pokemon_list = [pokedex_player.Vaporeon, pokedex_player.Charizard,
                    pokedex_player.Dialga_O, pokedex_player.Landorus_Therian,
                    pokedex_player.Charizard, pokedex_player.Mega_Charizard_X,
                    pokedex_player.Blaziken]

poke_team = [random.choice(all_pokemon_list),
             random.choice(all_pokemon_list),
             random.choice(all_pokemon_list)]

strong_pokemon_list = [pokedex_player.Arceus, pokedex_player.Dialga_O,
                       pokedex_player.Rhyperior, pokedex_player.Mega_Mewtwo_Y,
                       pokedex_player.Mega_Blaziken,
                       pokedex_player.Mega_Charizard_X,]
opponent_1 = random.choice(strong_pokemon_list)
# opponent_1 = Arceus
opo_bonus(opponent_1)

pokemon_battle(random.choice(poke_team), opponent_1)
