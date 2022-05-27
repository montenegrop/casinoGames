# 12 símbolos
# 11 comodín, 12 free spins
# comodín solo aparece en reel 2 y 4
symbols_1_3_5 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L"]
symbols_2_4 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
weight_12 = 100/12
weight_11 = 100/11
equal_11 = (weight_11, weight_11, weight_11, weight_11, weight_11,
            weight_11, weight_11, weight_11, weight_11, weight_11, weight_11)
equal_12 = (weight_12, weight_12, weight_12, weight_12, weight_12, weight_12,
            weight_12, weight_12, weight_12, weight_12, weight_12, weight_12)
lengths = (100, 100, 100, 100, 100)
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
    "F": {1: 0, 2: 0, 3: 1, 4: 10, 5: 50},
}
free_spins = [15, 20, 25]
