import random

attack_dict = {
    "Flamethrower": ("Fire", 95),
    "Dragon Claw": ("Dragon", 80),
    "Hydropump": ("Water", 120),
    "Draco Meteor": ("Dragon", 130),
    "Earthquake": ("Ground", 100),
    "Roar of Time": ("Dragon", 150),
    "Shadow Ball": ("Ghost", 80),
    "Psystrike": ("Psychic", 100),
    "Blaze Kick": ("Fire", 85),
    "Sky Uppercut": ("Fighting", 85)
}

npc_attack_dict = [
    "Flamethrower",
    "Dragon Claw",
    "Hydropump",
    "Draco Meteor",
    "Earthquake",
    "Roar of Time",
    "Shadow Ball",
    "Psystrike",
    "Blaze Kick",
    "Sky Uppercut",
]

your_att = "flamethrower"

if your_att in attack_dict:
    print("attack")