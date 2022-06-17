import copy
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
    'S': {"0": 0, '1': 0, '2': 0, '3': 5, '4': 20, '5': 50},
    'W': {"0": 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
}
free_spins_list = [0, 0, 0, 15, 20, 25]
free_spins_symbol = "S"


def compute_combinations_GM(reels_round_set: list):

    # g, M, count
    gmTotal = [0, 0, 0]

    @timeit("")
    def combinations_GM(index=0, factor=1, chains={"A": [0, 1], "B": [0, 1], "C": [0, 1], "D": [0, 1], "E": [0, 1], "F": [0, 1], "G": [0, 1], "H": [0, 1], "I": [0, 1], "J": [0, 1], "S": [0, 1], "W": [0, 1]}):
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
                if r_chains[key][0] == index:
                    key_win = payments[key[0]][str(index)] * \
                        r_factor * \
                        lengths_mult[total_reels-index-1] * \
                        r_chains[key][1]
                    rg += key_win
                    if key[0] == "S":
                        key_spins = free_spins_list[index] * \
                            r_factor * \
                            lengths_mult[total_reels -
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
                        key_win = payments[key[0]][str(index + 1)] * \
                            r_factor * \
                            lengths_mult[total_reels-index-1] * \
                            r_chains[key][1]
                        rg += key_win
                        if key[0] == "S":
                            key_spins = free_spins_list[index + 1] * \
                                r_factor * \
                                lengths_mult[total_reels -
                                             index-1] * \
                                r_chains[key][1]
                            rm += key_spins
                    gmTotal[2] += r_factor * lengths_mult[total_reels-index-1]
            else:
                gmTotal[2] += r_factor * lengths_mult[total_reels-index-1]
            gmTotal[0] += rg
            gmTotal[1] += rm
    combinations_GM()
    return gmTotal


normal_reels = ['FCDBACSAEHDAEBSDEAGCBDIAFDJCDBGCDGEBSDCFBCIDFGDBIECJEDBEFSBAEHCBESDEBHCBIDFCJECFEBDGCBEDBGECIBCSDCBEAFCJCIDFBDEBCEDGBSEDCIJEBDICFDGBCEASDBCGCEBFDEGCEDBEFGBDCSECGBSCDIAB',
                'GDSADGFAHFCBHAIFHDEIAHEIAJDWBHADFHAEHBWABSADWEJBACDSFGDFGDFESFDGCDEWGECFBGFASFCBHCDESADIAHEAIFDSHDEJBSADHFIDASDAWEJAEJDAHFWDGFAIAGEFSDGFDSFGDADSIAEFDGAFDBAJFEADISADHAGDAJE',
                'SCAEGDBCFHCBADHACEDCBAGCFDHEDIBAHBFGDFSADHFBJEACFJDBGEBHEDCEDGECFAEGCAECGBAFGCFICBFCASCAEGABCFHCBADHACEDCBAJCFDHEDIBAHBFHDFSDCSADHFBJEACFJDBGEASEDIEDHECFAEGCAECHBAFGCFICBFCASC',
                'WDJECHBCGEAHFBCHECBAFCDHFCGFCWAEICBHAFGBCHAFBEHFAGEBGFDHEAJDBHFCJDBHFAIBWDJCAIBWDJCIBWDJECHBCSEAHBCGFCEBFCDHFAGFCJAEICBHAFGBCHAFBEHFBGEBIFDHEAJDBWAFJBDWFAIBWDCJAIBWDJFIBWD',
                'HFEJDHBCJDSBGFIBSCJDSAGBSAHBAJFHAIDHEJDGBJFDICHFBGFSBIFEJDHBCJDBGABIFSCJDSAGBSAIBAJDHAIDHFJDGAJFDICHEAGFSBHFEDAJFCBJFADGCSADIHJABJIGAFBIJHDSCABHGDFIJHFBJSDGBHJDHFJAB']
lengths = [168, 171, 175, 171, 165]
lengths_mult = [
    1,
    lengths[4],
    lengths[4] * lengths[3],
    lengths[4] * lengths[3] * lengths[2],
    lengths[4] * lengths[3] * lengths[2] * lengths[1],
    lengths[4] * lengths[3] * lengths[2] * lengths[1] * lengths[0]
]

# sets_lengths normal spins: 69 78 54 67 84


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
                   for (i, reel) in enumerate(normal_reels)]


# print("start")
# gm_Total = compute_combinations_GM(reels_round_set=reels_round_set)
# tot_file = open("final_4.json", "a")
# tot_file.write(str(gm_Total))
# tot_file.close()
# print("end")
