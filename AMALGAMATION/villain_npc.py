import random
import pokedex_player

your_pc = []
your_team =[]
wild_pool = []
intern_team = [pokedex_player.Charmander, pokedex_player.Cramorant, pokedex_player.Blaziken]  # Basic Pokemon 1x
grunt_team = [pokedex_player.Vespiquen, pokedex_player.Charmeleon, pokedex_player.Sylveon, pokedex_player.Ceruledge,]  # Mid Stage Evo 2x
manager_team = [pokedex_player.Iron_Crown, pokedex_player.Regice, pokedex_player.Mega_Scizor, pokedex_player.Mega_Blaziken, pokedex_player.Mega_Mewtwo_Y,
             pokedex_player.Mega_Charizard_X, pokedex_player.Glastrier, pokedex_player.Giratina_O, pokedex_player.Dialga_O, pokedex_player.Raging_Bolt,
             pokedex_player.Landorus_T ,pokedex_player.Blaziken, pokedex_player.Charizard, pokedex_player.Venusaur, pokedex_player.Blastoise, pokedex_player.Lapras, pokedex_player.Torterra]  # Final Forms 3x
exec_team = [pokedex_player.Iron_Crown, pokedex_player.Regice, pokedex_player.Giratina_O]
             # pokedex_player.Mega_Scizor, pokedex_player.Mega_Blaziken, pokedex_player.Mega_Mewtwo_Y,
             # pokedex_player.Mega_Charizard_X, pokedex_player.Glastrier, pokedex_player.Giratina_O, pokedex_player.Dialga_O, pokedex_player.Raging_Bolt,
             # pokedex_player.Landorus_T]  # Legendary & Mega 6x

class Villain:


    def __init__(self, name: str, rank: str):
        self.name = name
        self.rank = rank
        self.team = []
        self.exclude = set()
        if rank == "intern":
            for team_no in range(1):
               available_poke = []
               for poke in intern_team:
                   if poke not in self.exclude:
                       available_poke.append(poke)
               poke = random.choice(available_poke)
               self.team.append(poke)
               self.exclude.add(poke)
        elif rank == "grunt":
            for team_no in range(2):
               available_poke = []
               for poke in grunt_team:
                   if poke not in self.exclude:
                       available_poke.append(poke)
               poke = random.choice(available_poke)
               self.team.append(poke)
               self.exclude.add(poke)
        elif rank == "manager":
            for team_no in range(3):
               available_poke = []
               for poke in manager_team:
                   if poke not in self.exclude:
                       available_poke.append(poke)
               poke = random.choice(available_poke)
               self.team.append(poke)
               self.exclude.add(poke)
        elif rank == "exec":
            for team_no in range(6):
               available_poke = []
               for poke in exec_team:
                   if poke not in self.exclude:
                       available_poke.append(poke)
               poke = random.choice(available_poke)
               self.team.append(poke)
               self.exclude.add(poke)
        else:
            print("Hold up, check class Villain")


Sam = Villain("Sam", "grunt")
Meeri = Villain("Meeri", "manager")




