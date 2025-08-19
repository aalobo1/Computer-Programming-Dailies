import random

Lakers = ["LeBron James", "Luka Doncic", "Deandre Ayton", "Bronny James", "Rui Hachimura", "Dalton Necht"]
def pick_random_player (Lakers):
    return random.choice(Lakers)
print(pick_random_player(Lakers))