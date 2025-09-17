import random

class Villain:
    intern_team = []  # Basic Pokemon 1x
    grunt_team = []  # Mid Stage Evo 2x
    manager_team = []  # Final Forms 3x
    exec_team = []  # Legendary & Mega 6x

    def __init__(self, name: str, rank: str):
        self.name = name
        self.rank = rank
        self.team = []
        if rank == "intern":
            self.team.append(random.choice)
        elif rank == "grunt":
            self.team.append(random.choice)
            self.team.append(random.choice)
        elif rank == "manager":
            self.team.append(random.choice)
            self.team.append(random.choice)
            self.team.append(random.choice)
        elif rank == "exec":
            self.team.append(random.choice)
            self.team.append(random.choice)
            self.team.append(random.choice)
            self.team.append(random.choice)
            self.team.append(random.choice)
            self.team.append(random.choice)




