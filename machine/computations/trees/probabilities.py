import math


expectationsN = {'0': [1974720932115, 0, 1753987733520], '15': [5474782170, 12353937750, 1186853250], '20': [9166024380, 4123904400,
                                                                                                             258326640], '25': [0, 0, 0], '30': [0, 0, 0], '35': [0, 0, 0], '40': [0, 0, 0], '50': [0, 0, 0], '80': [0, 0, 0], '100': [0, 0, 0]}

g, m, p = [1989361738665, 16477842150, 141848091000]
gs, ms, ps = [1626194395620, 23837012100, 108714652200]

expectationsFS = {'0': [1606002982700, 0, 1371234682455], '15': [9572203080, 19082547000, 1919864760], '20': [10619209840, 4754465100,
                                                                                                              321992880], '25': [0, 0, 0], '30': [0, 0, 0], '35': [0, 0, 0], '40': [0, 0, 0], '50': [0, 0, 0], '80': [0, 0, 0], '100': [0, 0, 0]}

xFS = {
    "0": [0, 0],
    "15": [0, 0],
    "20": [0, 0],
    "25": [0, 0],
    "30": [0, 0],
    "35": [0, 0],
    "40": [0, 0],
    "50": [0, 0],
    "80": [0, 0],
    "100": [0, 0]
}

# p(key) * E(|key)
xN = {
    "0": [0, 0],
    "15": [0, 0],
    "20": [0, 0],
    "25": [0, 0],
    "30": [0, 0],
    "35": [0, 0],
    "40": [0, 0],
    "50": [0, 0],
    "80": [0, 0],
    "100": [0, 0]
}

for key in expectationsN:
    if expectationsN[key][2]:
        xN[key][0] = expectationsN[key][0]/expectationsN[key][2]
        xN[key][1] = expectationsN[key][2]/p
        print(key, xN[key])

for key in expectationsFS:
    if expectationsFS[key][2]:
        xFS[key][0] = expectationsFS[key][0]/expectationsFS[key][2]
        xFS[key][1] = expectationsFS[key][2]/ps
        print(key, xFS[key])

# roi = xN["0"] * + \
#     (xN["15"] + 3 * 15 * xFS["0"]) + \
#     (xN["20"] + 3 * 20 * xFS["0"]) + \
#     (xN["25"] + 3 * 25 * xFS["0"]) + \
#     (xN["30"] + 3 * 30 * xFS["0"]) + \
#     (xN["35"] + 3 * 35 * xFS["0"]) + \
#     (xN["40"] + 3 * 40 * xFS["0"]) + \
#     (xN["50"] + 3 * 50 * xFS["0"]) + \
#     (xN["80"] + 3 * 80 * xFS["0"]) + \
#     (xN["100"] + 3 * 100 * xFS["0"])

roi = xN["0"][0] * xN["0"][1] + \
    (xN["15"][0] + 3 * 15 * xFS["0"][0])*(xN["15"][1]*xFS["0"][1]**15) + \
    (xN["20"][0] + 3 * 20 * xFS["0"][0])*(xN["20"][1]*xFS["0"][1]**20) + \
    (xN["25"][0] + 3 * 25 * xFS["0"][0])*(xN["25"][1]*xFS["0"][1]**25)

roi = roi / 25
print("roi=", roi)

print("desde aca Tree 2")


normal_keys = {'0': [1970109899595, 0, 140883138000], '15': [98805207045, 11177372250, 745158150], '30': [9941904885, 1176565500, 39218850], '20': [68019978471, 2598550200, 129927510], '40': [11261671086, 441180000, 11029500], '80': [443457039, 17647200, 220590], '25': [46115725644, 906471000, 36258840], '50': [7757226024, 153900000, 3078000], '100': [308524476, 6156000, 61560]}
fs_keys = {'0': [1597637896110, 0, 107216079300], '15': [170335643360, 19082547000, 1272169800], '30': [0, 0, 0], '20': [94590048168, 3622449600, 181122480], '40': [0, 0, 0], '80': [0, 0, 0], '25': [57566718382, 1132015500, 45280620], '50': [0, 0, 0], '100': [0, 0, 0]}

normal_keys = {'0': [1970109899595, 0, 140883138000], '15': [98805207045, 11177372250, 745158150]}


#nivel 2, 3 con 0

def fa(n):
    return math.factorial(n)

g, m, p = [2212763594265, 16477842150, 141848091000]
g1, m1, p1 = [1920130306020, 23837012100, 108714652200]

g0 = fs_keys["0"][0]/fs_keys["0"][2] if fs_keys["0"][2] != 0 else 0
g15 = fs_keys["15"][0]/fs_keys["15"][2] if fs_keys["15"][2] != 0 else 0
g20 = fs_keys["20"][0]/fs_keys["20"][2] if fs_keys["20"][2] != 0 else 0
g25 = fs_keys["25"][0]/fs_keys["25"][2] if fs_keys["25"][2] != 0 else 0
g30 = fs_keys["30"][0]/fs_keys["30"][2] if fs_keys["30"][2] != 0 else 0
g40 = fs_keys["40"][0]/fs_keys["40"][2] if fs_keys["40"][2] != 0 else 0
g50 = fs_keys["50"][0]/fs_keys["50"][2] if fs_keys["50"][2] != 0 else 0
g80 = fs_keys["80"][0]/fs_keys["80"][2] if fs_keys["80"][2] != 0 else 0
g100 = fs_keys["100"][0]/fs_keys["100"][2] if fs_keys["100"][2] != 0 else 0

p0 = fs_keys["0"][2]/p1
p15 = fs_keys["15"][2]/p1
p20 = fs_keys["20"][2]/p1
p25 = fs_keys["25"][2]/p1
p30 = fs_keys["30"][2]/p1
p40 = fs_keys["40"][2]/p1
p50 = fs_keys["50"][2]/p1
p80 = fs_keys["80"][2]/p1
p100 = fs_keys["100"][2]/p1



win = 0
for main_key in normal_keys:
    gmainkey = normal_keys[main_key][0]/normal_keys[main_key][2]
    pmain = normal_keys[main_key][2]/p
    for a0 in range(0,int(main_key)+1):
        for a1 in range(0,int(main_key)+1-a0):
            print("main:",main_key, "a0:", a0, "a1:", a1)
            for a2 in range(0,int(main_key)+1-a0-a1):
                for a3 in range(0,int(main_key)+1-a0-a1-a2):
                    for a4 in range(0,int(main_key)+1-a0-a1-a2-a3):
                        for a5 in range(0,int(main_key)+1-a0-a1-a2-a3-a4):
                            for a6 in range(0,int(main_key)+1-a0-a1-a2-a3-a4-a5):
                                for a7 in range(0,int(main_key)+1-a0-a1-a2-a3-a4-a5-a6):
                                    for a8 in range(0,int(main_key)+1-a0-a1-a2-a3-a4-a5-a6-a7):
                                        win+=(gmainkey + 3*(a0*g0 + a1*g15 + a2*g20 + a3*g25 + a4*g30 + a5*g40 + a6*g50 + a7*g80 + a8*g100) + \
                                            3*(g0 * (a1*15+a2*20+a3*25+a4*30+a5*40 + a6*50 + a7*80 + a8*100))) * \
                                                (fa(int(main_key))/(fa(a0)*fa(a1)*fa(a2)*fa(a3)*fa(a4)*fa(a5)*fa(a6)*fa(a7)*fa(a8))) * \
                                                    (pmain * p0**a0 * p15**a1 * p20**a2 * p25**a3 * p30**a4 * p40**a5 * p50**a6 * p80**a7 * p100**a8) * \
                                                        p0**(a1*15+a2*20+a3*25+a4*30+a5*40 + a6*50 + a7*80 + a8*100)

print("win", win)

