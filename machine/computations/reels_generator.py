from parameters import symbols_1_3_5, symbols_2_4, weights, free_spins, lengths
import random


def generate_reel(array, weights, k=1):
    array_reel = random.choices(population=array, weights=weights, k=100)
    return ''.join(array_reel)


reels = []
reels.append(generate_reel(array=symbols_1_3_5,
             weights=weights["1"], k=lengths[0]))
reels.append(generate_reel(array=symbols_2_4,
             weights=weights["2"], k=lengths[1]))
reels.append(generate_reel(array=symbols_1_3_5,
             weights=weights["3"], k=lengths[2]))
reels.append(generate_reel(array=symbols_2_4,
             weights=weights["4"], k=lengths[3]))
reels.append(generate_reel(array=symbols_1_3_5,
             weights=weights["5"], k=lengths[4]))
