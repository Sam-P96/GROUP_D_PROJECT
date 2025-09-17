import random
import pokedex_player
import pokemon_battle_function_006
import type_chart_factor
import attack_dict
import npc_attack_dict
from pokemon_battle_function_006_trainer import pokemon_battle
from villain_npc import Sam
from villain_npc import Meeri

def team_health_check(trainer):
    healthy_trainer_team = []
    for poke in trainer.team:
        if poke.health > 0:
            healthy_trainer_team.append(poke)
    return healthy_trainer_team

def trainer_battle(you, opo):
    healthy_opo_team = team_health_check(opo)
    your_healthy_team = team_health_check(you)
    print(f"You send out {you.team[0].name}")
    while len(healthy_opo_team) > 0 and len(your_healthy_team) > 0:
        pokemon_battle(you.team[0], opo.team[0])

    if len(healthy_opo_team) <= 0:
        print("You Won!")
    elif len(your_healthy_team) <= 0:
        print("You Lost!")

sam_list = []
for pokemon in Sam.team:
    sam_list.append(pokemon.name)
print(sam_list)

meeri_list = []
for pokemon in Meeri.team:
    meeri_list.append(pokemon.name)
print(meeri_list)
trainer_battle(Sam, Meeri)