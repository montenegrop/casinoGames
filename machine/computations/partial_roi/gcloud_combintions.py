
def winning_chains(
    screen: list,
    total_reels=5,
    wild="W"
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
    payments: dict,
    free_spins_symbol: str,
    free_spins_list: list
) -> dict:

    line_wins = []
    keys = chains.keys()
    total_win = 0
    for key in keys:
        chain = chains[key]
        wild = []
        win = payments[key[0]][str(len(chain))]
        # si hay multiplicador del len(key)
        if len(key) == 3:
            wild.append(int(key[2]))
        if len(key) == 5:
            wild.append(int(key[4]))

        if win > 0:
            total_win += win
            line_wins.append(
                dict(
                    symbol=key[0],
                    chain=chain,
                    wild=wild,
                    win=win
                )
            )
    free_spins = 0
    if free_spins_symbol in keys:
        free_spins = free_spins_list[len(chains[free_spins_symbol])-1]

    winnings = dict(
        total_win=total_win,
        free_spins=free_spins,
        line_wins=line_wins
    )

    return winnings


def compute_combinations_GM(
    reels_round_set: list,
    payments: dict,
    free_spins_list
) -> float:

    wild = "W"
    freeSpins = "S"

    # g, M, f, combinations
    globalGM = [0, 0, 0]
    gm01 = [0, 0, 0]

    def combination_GM(combination):
        win_chains = winning_chains(combination, 5, wild)
        w_dict = winnings(win_chains, payments, freeSpins, free_spins_list)
        g = w_dict["total_win"]
        m = w_dict["free_spins"]
        return (g, m)

    def combinations_GM(combination=[]):
        arr = combination
        i = len(arr)

        for j in reels_round_set[i]:
            r = j

            if i == 5 - 1:
                gm = combination_GM(arr + [r])
                globalGM[0] += gm[0]
                globalGM[1] += gm[1]
                globalGM[2] += 1
                gm01[0] += gm[0]
                gm01[1] += gm[1]
                gm01[2] += 1
            else:
                combinations_GM(combination=arr + [r])
                if i == 0:
                    f = open("r0.json", "a")
                    f.write("_" + r + "_GM:" + str(globalGM) + "\n")
                    f.close()
                if i == 1:
                    f = open("r01.json", "a")
                    f.write("_" + arr[0] + r + "_gm01:" + str(gm01) + "\n")
                    f.close()
                    gm01[0] = 0
                    gm01[1] = 0
                    gm01[2] = 0

    combinations_GM()
    return globalGM


reels = ['FCDBACSAEHDAEBSDEAGCBDIAFDJCDBGCDGEBSDCFBCIDFGDBIECJEDBEFSBAEHCBESDEBHCBIDFCJECFEBDGCBEDBGECIBCSDCBEAFCJCIDFBDEBCEDGBSEDCIJEBDICFDGBCEASDBCGCEBFDEGCEDBEFGBDCSECGBSCDIAB',
         'GDSADGFAHFCBHAIFBGFGDJE',
         'SCAEGDBCFHCBADHACAFGCFICBFCASC',
         'WDJECHBCGEAHFBCHECWJAIBWDJFIBWD',
         'HFEJDHBCJDSBGFIBSCGFBJSDGBHJDHFJAB']


def reel_round(reel: str, visible: int) -> str:
    return reel + reel[0: visible - 1]


visible = [3, 3, 3, 3, 3]
reels_round = [reel_round(reel, visible[i])
               for (i, reel) in enumerate(reels)]


def to_set(reel):
    s = set()
    for i in range(len(reel)):
        col = reel[i: i+3]
        s.add(col)
    return s


reels_round_set = [to_set(reel) for reel in reels_round]


# reels = ['FCDBACSAEHDAEBSDEAGCBDIAFDJCDBGCDGEBSDCFBCIDFGDBIECJEDBEFSBAEHCBESDEBHCBIDFCJECFEBDGCBEDBGECIBCSDCBEAFCJCIDFBDEBCEDGBSEDCIJEBDICFDGBCEASDBCGCEBFDEGCEDBEFGBDCSECGBSCDIAB',
#          'GDSADGFAHFCBHAIFHDEIAHEIAJDWBHADFHAEHBWABSADWEJBACDSFGDFGDFESFDGCDEWGECFBGFASFCBHCDESADIAHEAIFDSHDEJBSADHFIDASDAWEJAEJDAHFWDGFAIAGEFSDGFDSFGDADSIAEFDGAFDBAJFEADISADHAGDAJE',
#          'SCAEGDBCFHCBADHACEDCBAGCFDHEDIBAHBFGDFSADHFBJEACFJDBGEBHEDCEDGECFAEGCAECGBAFGCFICBFCASCAEGABCFHCBADHACEDCBAJCFDHEDIBAHBFHDFSDCSADHFBJEACFJDBGEASEDIEDHECFAEGCAECHBAFGCFICBFCASC',
#          'WDJECHBCGEAHFBCHECBAFCDHFCGFCWAEICBHAFGBCHAFBEHFAGEBGFDHEAJDBHFCJDBHFAIBWDJCAIBWDJCIBWDJECHBCSEAHBCGFCEBFCDHFAGFCJAEICBHAFGBCHAFBEHFBGEBIFDHEAJDBWAFJBDWFAIBWDCJAIBWDJFIBWD',
#          'HFEJDHBCJDSBGFIBSCJDSAGBSAHBAJFHAIDHEJDGBJFDICHFBGFSBIFEJDHBCJDBGABIFSCJDSAGBSAIBAJDHAIDHFJDGAJFDICHEAGFSBHFEDAJFCBJFADGCSADIHJABJIGAFBIJHDSCABHGDFIJHFBJSDGBHJDHFJAB']

payments = {
    'A': {'1': 0, '2': 3, '3': 6, '4': 25, '5': 80},
    'B': {'1': 0, '2': 3, '3': 6, '4': 25, '5': 80},
    'C': {'1': 0, '2': 0, '3': 6, '4': 25, '5': 100},
    'D': {'1': 0, '2': 0, '3': 6, '4': 25, '5': 100},
    'E': {'1': 0, '2': 0, '3': 12, '4': 40, '5': 150},
    'F': {'1': 0, '2': 0, '3': 12, '4': 80, '5': 200},
    'G': {'1': 0, '2': 0, '3': 20, '4': 100, '5': 400},
    'H': {'1': 0, '2': 0, '3': 30, '4': 200, '5': 500},
    'I': {'1': 0, '2': 0, '3': 50, '4': 400, '5': 1000},
    'J': {'1': 0, '2': 0, '3': 100, '4': 500, '5': 1500},
    'S': {'1': 0, '2': 0, '3': 5, '4': 20, '5': 50},
    'W': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
}

free_spins_list = [0, 0, 15, 20, 25]


gmlist = compute_combinations_GM(reels_round_set=reels_round_set, payments=payments,
                                 free_spins_list=free_spins_list)

gm = {"G": gmlist[0], "M": gmlist[1], "counter": gmlist[2]}
print("termino:", gm)
