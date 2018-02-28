"""
Bygger tårn med hjelp av stjerner.
Skal øke med to i nederste etasje hver gang.
"""


def tower_builder(n_floors):
    pyramideListe = []

    for i in range(n_floors):
        n_floors -= 1
        # writing out excatly what i want, i think ther som better soulution here. 
        pyramideListe.append(" " * n_floors + "*" * (i * 2 + 1) + " " * n_floors)

    return pyramideListe


print(tower_builder(1))
