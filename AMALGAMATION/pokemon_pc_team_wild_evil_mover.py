from all_pokemon_list import NU_Poke
from all_pokemon_list import OU_Poke
from all_pokemon_list import Uber_Poke





def wild_pokemon_assigner(all_p = all_pokemon_list):
    for pokemon in all_p:
        if pokemon not in player.team or pokemon not in evil.team:
            wild_poke.append(pokemon)
            poke_list.remove(pokemon)