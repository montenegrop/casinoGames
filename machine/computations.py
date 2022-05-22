# visible de cada reel
visible = [3, 3, 3]

# reels: ¿letras suficientes simbolos espero?
reel1 = "ABCDEABCD"
reel2 = "AABBCCDDEABCEF"
reel3 = "ABCAABCDE"

# reels redondos
reel1_r = reel1 + reel1[0:visible[0]-1]
reel2_r = reel2 + reel2[0:visible[1]-1]
reel3_r = reel3 + reel3[0:visible[2]-1]

# de arriba a abajo, valor en lo visible de cada reel que forma la linea de pago
lane1 = [2, 2, 2]

# pagos
pagos = {
    "A": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "B": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "C": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "D": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "E": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "F": {1: 0, 2: 0, 3: 1, 4: 10, 5: 50}
}

# roll, posicion del elemento superior de cada reel redondo

# valor i = 0, 1, 2, ..., len(reeli) -1 ;limitados por la longitud de reeli menos 1: pensar
roll = [0, 4, 6]
visible_roll1 = reel1_r[roll[0]: visible[0]]

# corregir: crear archivo computed.py para propiedades de elementos, estilo len(reel1), ...

# computando linea1
# simbolos en linea1
symbolo1_index = -1 + lane1[0] + roll[0]
symbol_roll1_lane1 = reel1[symbolo1_index]
