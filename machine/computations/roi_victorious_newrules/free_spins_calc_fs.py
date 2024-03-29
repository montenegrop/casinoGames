import copy
from time_decorator import timeit
wild = "W"
total_reels = 5
payments = {
    'A': {'0': 0, '1': 0, '2': 3, '3': 6, '4': 25, '5': 80},
    'B': {'0': 0, '1': 0, '2': 3, '3': 6, '4': 25, '5': 80},
    'C': {'0': 0, '1': 0, '2': 0, '3': 6, '4': 25, '5': 100},
    'D': {'0': 0, '1': 0, '2': 0, '3': 6, '4': 25, '5': 100},
    'E': {'0': 0, '1': 0, '2': 0, '3': 12, '4': 40, '5': 150},
    'F': {'0': 0, '1': 0, '2': 0, '3': 12, '4': 80, '5': 200},
    'G': {'0': 0, '1': 0, '2': 0, '3': 20, '4': 100, '5': 400},
    'H': {'0': 0, '1': 0, '2': 0, '3': 30, '4': 200, '5': 500},
    'I': {'0': 0, '1': 0, '2': 0, '3': 50, '4': 400, '5': 1000},
    'J': {'0': 0, '1': 0, '2': 0, '3': 100, '4': 500, '5': 1500},
    'S': {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0},
    'W': {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
}

free_spins_list = [0, 0, 0, 15, 20, 25]
scatter = "S"

# g, m, c
# se espera m = c x key


def compute_combinations_GM(reels_round_set: list, lengths_mult_array):
    count0 = [0]

    # g, M, count
    gmTotal = [0, 0, 0]
    initial_chains = {"A": [0, 1], "B": [0, 1], "C": [0, 1], "D": [0, 1], "E": [0, 1], "F": [
        0, 1], "G": [0, 1], "H": [0, 1], "I": [0, 1], "J": [0, 1], "S": [0, 1], "W": [0, 1]}

    @timeit("")
    def combinations_GM(index=0, factor=1, chains=initial_chains, fs_symbols=0):
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
            if "S" in r_chains.keys():
                r_chains["S"][0] = 0

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
            if index == 0:
                count0[0] += 1
                print("count0:", count0[0])
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

lengths_mult = [
    1,
    lengths[4],
    lengths[4] * lengths[3],
    lengths[4] * lengths[3] * lengths[2],
    lengths[4] * lengths[3] * lengths[2] * lengths[1],
    lengths[4] * lengths[3] * lengths[2] * lengths[1] * lengths[0]
]


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


def contador_s_of_r(r):
    return r[0][0].count("S")


def factor_s_of_r(r):
    return r[1]


def fs_totales(reels_round_set):
    result = 0
    for r0 in reels_round_set[0]:
        factor0 = r0[1]
        print(result, r0)
        for r1 in reels_round_set[1]:
            factor1 = factor0 * r1[1]
            for r2 in reels_round_set[2]:
                factor2 = factor1 * r2[1]
                for r3 in reels_round_set[3]:
                    factor3 = factor2 * r3[1]
                    for r4 in reels_round_set[4]:
                        factor4 = factor3 * r4[1]
                        count = contador_s_of_r(r0) + \
                            contador_s_of_r(r1) + \
                            contador_s_of_r(r2) + \
                            contador_s_of_r(r3) + \
                            contador_s_of_r(r4)
                        fs = free_spins_list[count]
                        result += fs * factor4
    print("terminando", result)
    return result


print("start")
fs_tot = fs_totales(reels_round_set)
print("fstotal", fs_tot)
tot_file = open("free_spins_fs_tot.json", "a")
tot_file.write(str(fs_tot))
tot_file.close()
print("end")
