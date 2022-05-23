# Settings de maquina:

# visible de cada reel
visible = [3, 3, 3, 3, 3]

# reels: ¿letras suficientes simbolos espero?
reel1 = "ABCDEABCD"
reel2 = "AABBCCDDEABCEF"
reel3 = "ABCAABCDE"
reel4 = "ABCAABCDE"
reel5 = "ABCAABCDE"

reels = [reel1, reel2, reel3, reel4, reel5]

# pagos
pagos = {
    "A": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "B": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "C": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "D": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "E": {1: 0, 2: 0, 3: 1, 4: 10, 5: 20},
    "F": {1: 0, 2: 0, 3: 1, 4: 10, 5: 50}
}

# Calculados:

machina_width = len(reels)

# reels redondos
# reel1_r = reel1 + reel1[0:visible[0]-1]


reels_r = [reel + reel[0: visible[index]-1]
           for (index, reel) in enumerate(reels)]
print(reels_r)

# lineas: de arriba a abajo, valor en lo visible de cada reel que forma la linea de pago
lane1 = [2, 2, 2, 2, 2]

# roll: posicion del elemento superior visivble de cada reel redondo
# valor i = 0, 1, 2, ..., len(reel_i) -1 ;limitados por la longitud de reeli menos 1: pensar
roll = [0, 4, 6, 2, 0]

# mostrar en pantalla:
visible_output = [reel_r[roll[index]: roll[index]+visible[index]]
                  for (index, reel_r) in enumerate(reels_r)]


# corregir: crear archivo computed.py para propiedades de elementos, estilo len(reel1), ...

# computando linea1
# simbolos en linea1
symbolo1_index = -1 + lane1[0] + roll[0]
symbol_roll1_lane1 = reel1[symbolo1_index]


def calculated_payment(machine, roll):
    paymenj_json = {"payment": 8}
    return paymenj_json
