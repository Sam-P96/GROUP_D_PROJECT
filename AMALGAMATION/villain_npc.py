import random
import pokedex_player
from all_pokemon_list import wild_poke
from all_pokemon_list import OU_Poke


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
               for poke in wild_poke:
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


Sam = Villain("Sam", "manager")
Meeri = Villain("Meeri", "manager")




