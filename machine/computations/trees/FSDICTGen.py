import copy
# from rrs_FSDict import FSDict
from time_decorator import timeit

wild = "W"
total_reels = 5
payments = {
    'A': {"0": 0, '1': 0, '2': 3, '3': 6, '4': 25, '5': 80},
    'B': {"0": 0, '1': 0, '2': 3, '3': 6, '4': 25, '5': 80},
    'C': {"0": 0, '1': 0, '2': 0, '3': 6, '4': 25, '5': 100},
    'D': {"0": 0, '1': 0, '2': 0, '3': 6, '4': 25, '5': 100},
    'E': {"0": 0, '1': 0, '2': 0, '3': 12, '4': 40, '5': 150},
    'F': {"0": 0, '1': 0, '2': 0, '3': 12, '4': 80, '5': 200},
    'G': {"0": 0, '1': 0, '2': 0, '3': 20, '4': 100, '5': 400},
    'H': {"0": 0, '1': 0, '2': 0, '3': 30, '4': 200, '5': 500},
    'I': {"0": 0, '1': 0, '2': 0, '3': 50, '4': 400, '5': 1000},
    'J': {"0": 0, '1': 0, '2': 0, '3': 100, '4': 500, '5': 1500},
    'S': {"0": 0, '1': 0, '2': 0, '3': 125, '4': 500, '5': 1250},
    'W': {"0": 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
}
payments = {
    'A': {"0": 0, '1': 0, '2': 3, '3': 6, '4': 1, '5': 1},
    'B': {"0": 0, '1': 0, '2': 3, '3': 6, '4': 1, '5': 1},
    'C': {"0": 0, '1': 0, '2': 0, '3': 6, '4': 1, '5': 1},
    'D': {"0": 0, '1': 0, '2': 0, '3': 6, '4': 1, '5': 1},
    'E': {"0": 0, '1': 0, '2': 0, '3': 12, '4': 1, '5': 1},
    'F': {"0": 0, '1': 0, '2': 0, '3': 12, '4': 1, '5': 1},
    'G': {"0": 0, '1': 0, '2': 0, '3': 20, '4': 1, '5': 1},
    'H': {"0": 0, '1': 0, '2': 0, '3': 30, '4': 1, '5': 1},
    'I': {"0": 0, '1': 0, '2': 0, '3': 50, '4': 1, '5': 1},
    'J': {"0": 0, '1': 0, '2': 0, '3': 100, '4': 1, '5': 1},
    'S': {"0": 0, '1': 0, '2': 0, '3': 125, '4': 1, '5': 1},
    'W': {"0": 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
}


free_spins_list = [0, 0, 0, 15, 20, 25]
free_spins_symbol = "S"

# g, m, c
# se espera m = c x key
expectations = {
    "0": [0, 0, 0],
    "15": [0, 0, 0],
    "20": [0, 0, 0],
    "25": [0, 0, 0],
    "30": [0, 0, 0],
    "35": [0, 0, 0],
    "40": [0, 0, 0],
    "50": [0, 0, 0],
    "80": [0, 0, 0],
    "100": [0, 0, 0],
}


def compute_combinations_GM(reels_round_set: list, lengths_mult_array):

    # g, M, count
    gmTotal = [0, 0, 0]
    initial_chains = {"A": [0, 1], "B": [0, 1], "C": [0, 1], "D": [0, 1], "E": [0, 1], "F": [
        0, 1], "G": [0, 1], "H": [0, 1], "I": [0, 1], "J": [0, 1], "S": [0, 1], "W": [0, 1]}

    # @timeit("")
    def combinations_GM(index=0, factor=1, chains=initial_chains):
        for r in reels_round_set[index]:

            r_factor = factor * r[1]
            r_chains = copy.deepcopy(chains)
            rg = 0
            rm = 0

            keys = list(r_chains.keys())
            if "W" in r[0][0]:
                for key in keys:
                    r_chains[key + "w" +
                             str(index)] = [index + 1, r[0][0].count("W") * r_chains[key][1]]

            for key in keys:
                if key[0] in r[0][0]:
                    r_chains[key][0] += 1
                    if key[0] == r[0][1]:
                        reps = r[0][0].count(key[0])
                        r_chains[key][1] *= reps

            for key in keys:
                key_win = 0
                key_spins = 0
                if r_chains[key][0] == index:
                    if not "W" in r[0][0]:
                        key_win = payments[key[0]][str(index)] * \
                            r_factor * \
                            lengths_mult_array[total_reels-index-1] * \
                            r_chains[key][1]
                        rg += key_win
                        if key[0] == "S":
                            key_spins = free_spins_list[index] * \
                                r_factor * \
                                lengths_mult_array[total_reels -
                                                   index-1] * \
                                r_chains[key][1]
                            rm += key_spins
                    r_chains.pop(key)
            if r_chains:
                if index < total_reels - 1:
                    combinations_GM(
                        index=index+1, factor=r_factor, chains=r_chains)
                else:
                    for key in r_chains:
                        key_win = 0
                        key_spins = 0
                        key_win = payments[key[0]][str(index + 1)] * \
                            r_factor * \
                            lengths_mult_array[total_reels-index-1] * \
                            r_chains[key][1]
                        rg += key_win
                        if key[0] == "S":
                            key_spins = free_spins_list[index + 1] * \
                                r_factor * \
                                lengths_mult_array[total_reels -
                                                   index-1] * \
                                r_chains[key][1]
                            rm += key_spins
                    gmTotal[2] += r_factor * \
                        lengths_mult_array[total_reels-index-1]
            else:
                gmTotal[2] += r_factor * \
                    lengths_mult_array[total_reels-index-1]
            gmTotal[0] += rg
            gmTotal[1] += rm
    combinations_GM()
    return gmTotal


# lengths = [168, 171, 165, 139, 165]
reels = ['ABCEFGESCBDEHCIEBIACEFGCEBDESHCEIAJEICGBDCEDICFBEDCASDJSCBDHEDACBGJDSEBCDECDEBDAGDCGBHEDFBGCIDAGBDESBDSJCIDFBDEBCEDGBSEDCIJEBDICFDGBCEASDBCGCEBFDEGCEDBEFGBDCSECGBSCDIAB',
         'JEBFDGJASCHGAEDHBAFDIHFAIECGDFAGBHASJEFAHDISAFBGAHIECWDFAWJDHSEBAJWIFGWHCEDWAGWFJSBDAFGEIWDCFHADSEAFGIWDAJWCBAJEDHSEAFGDAIJAIWDBHJDAGFEAHDWEHADSIAEFDGAFDBAJFEADISADHAGDAJE',
         'DABEACFDGCEASBDFGAFDEAFSAFBDSEDBCFADEFDGCHADECBDAFBDFAECDBFCEDBHADCBIACHDFECDSFEADSGABSDCHEBCDAFSECGSEFDEFAHDJCAHBEDFHECDAJHBFEADCSHBJDEADBAFEDBSFEJHAIESCEAIFBHEACDA',
         'BADFCGHBIEDJHWBHEFBICJADBGFICHBFGAFCDBICJFBHFWJCFEAWIFHCGBWDHJCAIFJHCWDBJCIWFHBGDCBAECGHCFSAFDCIBJHCBGIJDBFDAEFBACGJFBCJAGDFBIAFBCEBHDFAHBA',
         'ABFGJCSAHFIJBDACFEBSJHBJGCIJBSFJDFBHDSIABJIGDFIJAECJBIDASFDHGFABJICSHICFGEHDAJHDSJIABJCFGBSHAJIDACDHFAJIFHCJEDAJFCBJFADGCSADIHJABJIGAFBIJHDSCABHGDFIJHFBJSDGBHJDHFJAB']
# sets_lengths free_spins: 69 98 74 89 97
lengths = [len(r) for r in reels]


def reel_round(reel: str = "", visible: int = 3) -> str:
    return reel + reel[0: visible - 1]


def to_set(reel_round):
    s = []
    reel_round_s = []
    for i in range(len(reel_round) - (3-1)):
        sym = ""
        col = reel_round[i: i+3]
        if len(set(col)) < 3:
            sym = [s for s in col if col.count(s) > 1][0]
        reel_round_s.append([set(col), sym])

    repeated = []
    for col_s in reel_round_s:
        if col_s in repeated:
            continue
        repeated.append(col_s)
        count = reel_round_s.count(col_s)
        s.append([col_s, count])

    for col in s:
        word = ""
        for sym in col[0][0]:
            word = word + sym
        if len(word) < 3:
            word = word + col[0][1]
        if len(word) < 3:
            word = word + col[0][1]
        col[0][0] = word

    return s


visible = [3, 3, 3, 3, 3]

reels_round_set = [to_set(reel_round(reel, visible[i]))
                   for (i, reel) in enumerate(reels)]

print(reels_round_set)

FSDict_structure = {
    "0,0": [],
    "0,1": [],
    "0,2": [],
    "0,3": [],

    "1,0": [],
    "1,1": [],
    "1,2": [],
    "1,3": [],

    "2,0": [],
    "2,1": [],
    "2,2": [],
    "2,3": [],

    "3,0": [],
    "3,1": [],
    "3,2": [],
    "3,3": [],

    "4,0": [],
    "4,1": [],
    "4,2": [],
    "4,3": [],
}

FSReelsDict = {
    "0": [],
    "15": [],
    "30": [],
    "45": [],
    "20": [],
    "40": [],
    "60": [],
    "80": [],
    "25": [],
    "50": [],
    "75": [],
    "100": [],
}

FSGMPDict = {
    "0": [0, 0, 0],
    "15": [0, 0, 0],
    "30": [0, 0, 0],
    "45": [0, 0, 0],
    "20": [0, 0, 0],
    "40": [0, 0, 0],
    "60": [0, 0, 0],
    "80": [0, 0, 0],
    "25": [0, 0, 0],
    "50": [0, 0, 0],
    "75": [0, 0, 0],
    "100": [0, 0, 0],
}


def reels_round_set_SN(dictionaryFS, fs=0, mult=1):
    if fs == 0:
        r0x = []
        for n in range(1, 4):
            r0x += dictionaryFS["0" + "," + str(n)]
        r1x = []
        for n in range(1, 4):
            r1x += dictionaryFS["1" + "," + str(n)]
        reels = [[dictionaryFS["0,0"]], [r0x, dictionaryFS["1,0"]],
                 [r0x, r1x, dictionaryFS["2,0"]]]
        # caso R[0] no tiene
        rest = []
    elif fs == 3:
        if mult == 1:
            reels = [[dictionaryFS["0,1"], dictionaryFS["1,1"],
                      dictionaryFS["2,1"], dictionaryFS["3,0"]]]
        elif mult == 2:
            reels = [
                [dictionaryFS["0,2"], dictionaryFS["1,1"],
                    dictionaryFS["2,1"], dictionaryFS["3,0"]],
                [dictionaryFS["0,1"], dictionaryFS["1,2"],
                    dictionaryFS["2,1"], dictionaryFS["3,0"]],
                [dictionaryFS["0,1"], dictionaryFS["1,1"],
                    dictionaryFS["2,2"], dictionaryFS["3,0"]]
            ]
        elif mult == 4:
            reels = [
                [dictionaryFS["0,2"], dictionaryFS["1,2"],
                    dictionaryFS["2,1"], dictionaryFS["3,0"]],
                [dictionaryFS["0,2"], dictionaryFS["1,1"],
                    dictionaryFS["2,2"], dictionaryFS["3,0"]],
                [dictionaryFS["0,1"], dictionaryFS["1,2"],
                    dictionaryFS["2,2"], dictionaryFS["3,0"]],
            ]
    elif fs == 4:
        if mult == 1:
            reels = [[dictionaryFS["0,1"], dictionaryFS["1,1"],
                      dictionaryFS["2,1"], dictionaryFS["3,1"], dictionaryFS["4,0"]]]
        elif mult == 2:
            reels = [
                [dictionaryFS["0,2"], dictionaryFS["1,1"], dictionaryFS["2,1"],
                    dictionaryFS["3,1"], dictionaryFS["4,0"]],
                [dictionaryFS["0,1"], dictionaryFS["1,2"], dictionaryFS["2,1"],
                    dictionaryFS["3,1"], dictionaryFS["4,0"]],
                [dictionaryFS["0,1"], dictionaryFS["1,1"], dictionaryFS["2,2"],
                    dictionaryFS["3,1"], dictionaryFS["4,0"]],
                [dictionaryFS["0,1"], dictionaryFS["1,1"], dictionaryFS["2,1"],
                    dictionaryFS["3,2"], dictionaryFS["4,0"]],
            ]
        elif mult == 4:
            reels = [
                [dictionaryFS["0,2"], dictionaryFS["1,2"], dictionaryFS["2,1"],
                    dictionaryFS["3,1"], dictionaryFS["4,0"]],
                [dictionaryFS["0,2"], dictionaryFS["1,1"], dictionaryFS["2,2"],
                    dictionaryFS["3,1"], dictionaryFS["4,0"]],
                [dictionaryFS["0,2"], dictionaryFS["1,1"], dictionaryFS["2,1"],
                    dictionaryFS["3,2"], dictionaryFS["4,0"]],

                [dictionaryFS["0,1"], dictionaryFS["1,2"], dictionaryFS["2,2"],
                    dictionaryFS["3,1"], dictionaryFS["4,0"]],
                [dictionaryFS["0,1"], dictionaryFS["1,2"], dictionaryFS["2,1"],
                    dictionaryFS["3,2"], dictionaryFS["4,0"]],
                [dictionaryFS["0,1"], dictionaryFS["1,1"], dictionaryFS["2,2"],
                    dictionaryFS["3,2"], dictionaryFS["4,0"]],
            ]
    elif fs == 5:
        if mult == 1:
            reels = [[dictionaryFS["0,1"], dictionaryFS["1,1"],
                      dictionaryFS["2,1"], dictionaryFS["3,1"], dictionaryFS["4,1"]]]
        elif mult == 2:
            reels = [
                [dictionaryFS["0,2"], dictionaryFS["1,1"], dictionaryFS["2,1"],
                    dictionaryFS["3,1"], dictionaryFS["4,1"]],
                [dictionaryFS["0,1"], dictionaryFS["1,2"], dictionaryFS["2,1"],
                    dictionaryFS["3,1"], dictionaryFS["4,1"]],
                [dictionaryFS["0,1"], dictionaryFS["1,1"], dictionaryFS["2,2"],
                    dictionaryFS["3,1"], dictionaryFS["4,1"]],
                [dictionaryFS["0,1"], dictionaryFS["1,1"], dictionaryFS["2,1"],
                    dictionaryFS["3,2"], dictionaryFS["4,1"]],
                [dictionaryFS["0,1"], dictionaryFS["1,1"], dictionaryFS["2,1"],
                    dictionaryFS["3,1"], dictionaryFS["4,2"]]
            ]
        elif mult == 4:
            reels = [
                [dictionaryFS["0,2"], dictionaryFS["1,2"], dictionaryFS["2,1"],
                    dictionaryFS["3,1"], dictionaryFS["4,1"]],
                [dictionaryFS["0,2"], dictionaryFS["1,1"], dictionaryFS["2,2"],
                    dictionaryFS["3,1"], dictionaryFS["4,1"]],
                [dictionaryFS["0,2"], dictionaryFS["1,1"], dictionaryFS["2,1"],
                    dictionaryFS["3,2"], dictionaryFS["4,1"]],
                [dictionaryFS["0,2"], dictionaryFS["1,1"], dictionaryFS["2,1"],
                    dictionaryFS["3,1"], dictionaryFS["4,2"]],

                [dictionaryFS["0,1"], dictionaryFS["1,2"], dictionaryFS["2,2"],
                    dictionaryFS["3,1"], dictionaryFS["4,1"]],
                [dictionaryFS["0,1"], dictionaryFS["1,2"], dictionaryFS["2,1"],
                    dictionaryFS["3,2"], dictionaryFS["4,1"]],
                [dictionaryFS["0,1"], dictionaryFS["1,2"], dictionaryFS["2,1"],
                    dictionaryFS["3,1"], dictionaryFS["4,2"]],

                [dictionaryFS["0,1"], dictionaryFS["1,1"], dictionaryFS["2,2"],
                    dictionaryFS["3,2"], dictionaryFS["4,1"]],
                [dictionaryFS["0,1"], dictionaryFS["1,1"], dictionaryFS["2,2"],
                    dictionaryFS["3,1"], dictionaryFS["4,2"]],

                [dictionaryFS["0,1"], dictionaryFS["1,1"], dictionaryFS["2,1"],
                    dictionaryFS["3,2"], dictionaryFS["4,2"]],
            ]
    reels = list(filter(lambda x: [] not in x, reels))
    for r in reels:
        for i in range(len(r), 5):
            new_reel = []
            for n in range(0, 4):
                new_reel += dictionaryFS[str(i) + "," + str(n)]
            r.append(new_reel)
        # caso R[0] tiene y R[1] no tiene

    FSReelsDict[str(fs * mult * 5)] = reels


def reel_with_nSW(reels_set, i, n):
    new_reel = []
    for r in reels_set[i]:
        word = r[0][0]
        t = word.count("S") + word.count("W")
        if t == n:
            new_reel.append(r)
    return new_reel


for i in range(0, 5):
    suma = 0
    for n in range(0, 4):
        FSDict_structure[str(i)+","+str(n)
                         ] = reel_with_nSW(reels_round_set, i, n)


for l in [0, 3, 4, 5]:
    for mult in [1, 2, 4]:
        reels_round_set_SN(dictionaryFS=FSDict_structure, fs=l, mult=mult)

FSReelsDict

# for key in reels_roud_set_FSDict:


def lengh_mult(reel_set, i):
    cols = 1
    for col in reel_set[total_reels-i:total_reels]:
        w = 0
        for word in col:
            w += word[1]
        cols *= w
    return cols


d = open("fs.py", "a")
d.write(str(FSDict_structure))
d.close()
