# 12 símbolos
# 11 comodín, 12 free spins
# comodín solo aparece en reel 2 y 4
from machine.computations.random_numbers import random_integer
from random import choices

wild_symbol = "K"
free_spins_symbol = "L"


symbols_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
symbols_1_3_5 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L"]
symbols_2_4 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
weight_12 = 100/12
weight_11 = 100/11
equal_11 = (weight_11, weight_11, weight_11, weight_11, weight_11,
            weight_11, weight_11, weight_11, weight_11, weight_11, weight_11)
equal_12 = (weight_12, weight_12, weight_12, weight_12, weight_12, weight_12,
            weight_12, weight_12, weight_12, weight_12, weight_12, weight_12)
symbols = {
    "1": symbols_1_3_5,
    "2": symbols_2_4,
    "3": symbols_1_3_5,
    "4": symbols_2_4,
    "5": symbols_1_3_5
}
lengths = {
    "1": 101,
    "2": 102,
    "3": 103,
    "4": 104,
    "5": 105
}
visible = [3, 3, 3, 3, 3]
weights = {"1": equal_11,
           "2": equal_12,
           "3": equal_11,
           "4": equal_12,
           "5": equal_11}
payments = {
    "A": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "B": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "C": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "D": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "E": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "F": {1: 0, 2: 0, 3: 1, 4: 10, 5: 50},
    "G": {1: 0, 2: 0, 3: 1, 4: 10, 5: 50},
    "H": {1: 0, 2: 0, 3: 1, 4: 10, 5: 50},
    "I": {1: 0, 2: 0, 3: 1, 4: 10, 5: 50},
    "J": {1: 0, 2: 0, 3: 1, 4: 10, 5: 50},
    "K": {1: 0, 2: 0, 3: 1, 4: 10, 5: 50},
    "L": {1: 0, 2: 0, 3: 1, 4: 10, 5: 50},
}
free_spins_list = [0, 0, 15, 20, 25]

# mover a payments:

# machine functions:


def generate_reel(array, weights, length):
    array_reel = choices(population=array, weights=weights, k=length)
    return ''.join(array_reel)


def generate_reels(symbols_dict, weights_dict, lengths_dict, total_reels=5):
    return [generate_reel(symbols_dict[str(n)],
                          weights_dict[str(n)], lengths_dict[str(n)]) for n in range(1, total_reels + 1)]


def generate_reels_r(reels, visible):
    return [reel + reel[0: visible[index]-1]
            for (index, reel) in enumerate(reels)]

# roll functions:


def roll(lengths_dict, total_reels=5):
    return [random_integer(0, lengths_dict[str(n)]) for n in range(1, total_reels + 1)]


def visibles(reels_r, roll, visible=[3, 3, 3, 3, 3]) -> list:
    return [reel_r[roll[index]: roll[index]+visible[index]]
            for (index, reel_r) in enumerate(reels_r)]


def winning_chains(
    screen: list,
    total_reels=5,
    wild=wild_symbol
) -> dict:

    chains = {}
    v0 = screen[0]
    potential = set(v0)
    for symbol in potential:
        chains[symbol] = [v0.index(symbol)]

    reel_index = 1
    while potential and reel_index < total_reels:
        reel = screen[reel_index]
        if not wild in reel:
            potential = potential.intersection(set(reel))
            symbol_potential = potential
        else:
            symbol_potential = potential.intersection(set(reel))

        keys = list(chains.keys())
        for key in keys:
            if not len(chains[key]) == reel_index:
                continue
            symbol = v0[chains[key][0]]
            if wild in set(reel):
                chains[key + "w" + str(reel_index)
                       ] = chains[key] + [reel.index(wild)]
            if symbol in symbol_potential:
                chains[key].append(reel.index(symbol))
        reel_index += 1
    return chains

# payment functions:


def winnings(
    chains: dict,
    payments: dict = payments,
    free_spins_symbol: str = free_spins_symbol,
    free_spins_list: list = free_spins_list
) -> dict:

    line_wins = []
    keys = chains.keys()
    total_win = 0
    for key in keys:
        chain = chains[key]
        wild = []
        win = payments[key][str(len(chain))]
        # si hay multiplicador del len(key)
        if len(key) == 3:
            wild.append(int(key[2]))
        if len(key) == 5:
            wild.append(int(key[4]))

        if win > 0:
            total_win += win
            line_wins.append(
                dict(symbol=key[0], chain=chain, wild=wild, win=win))
    free_spins = 0
    if free_spins_symbol in keys:
        free_spins = free_spins_list[len(chains[free_spins_symbol])-1]

    winnings = dict(total_win=total_win,
                    free_spins=free_spins, line_wins=line_wins)

    return winnings
