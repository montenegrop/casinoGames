
initial = 6
increment = 3
wild = "W"
total_reels = 5
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
free_spins_symbol = "S"


def winning_chains(
    screen: list,
) -> dict:

    chains = {}
    potential = set(screen[0])
    for symbol in potential:
        chains[symbol] = 1

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
            if not chains[key] == reel_index:
                continue
            symbol = key[0]
            if wild in set(reel):
                chains[key + "w" + str(reel_index)
                       ] = reel_index + 1
            if symbol in symbol_potential:
                chains[key] = reel_index + 1
            else:
                if reel_index == 1:
                    chains.pop(key)
                    continue
                if reel_index == 2:
                    if not symbol == "A" or "B":
                        chains.pop(key)

        reel_index += 1
    return chains

# payment functions:


def winnings(
    chains: dict,
) -> dict:

    keys = chains.keys()
    free_spins = 0
    total_win = 0
    for key in keys:
        win = payments[key[0]][str(chains[key])]
        if win > 0:
            total_win += win
            if key[0] == free_spins_symbol:
                free_spins += free_spins_list[chains[key] - 1]

    winnings = dict(
        total_win=total_win,
        free_spins=free_spins,
    )

    return winnings


def compute_combinations_GM(reels_round_set: list):

    # g, M, f, combinations
    gm01 = [0, 0]

    def combination_GM(combination):
        win_chains = winning_chains(combination)
        w_dict = winnings(win_chains)
        g = w_dict["total_win"]
        m = w_dict["free_spins"]
        return (g, m)

    def combinations_GM(combination=[], factor=1):
        arr = combination
        i = len(arr)
        if i == 1:
            f = open(arr[0] + ".json", "a")
            f.write("{" + "\n")

        for r in reels_round_set[i]:
            mult = factor * r[1]
            if i == 4:
                gm = combination_GM(arr + [r[0]])
                gm01[0] += gm[0] * mult
                gm01[1] += gm[1] * mult
            else:
                combinations_GM(combination=arr + [r[0]], factor=mult)
                if i == 1:
                    f.write("\"" + r[0] + "\"" + ": " + "\"" +
                            str(gm01) + "\"" + "," + "\n")
                    gm01[0] = 0
                    gm01[1] = 0
        if i == 1:
            f.truncate(f.tell() - 3)
            f.write("\n" + "}")
            f.close()
    combinations_GM()


reels = ['FCD',
         'GDSADGFAHFCBHAIFBGFGDJE',
         'SCAEGDBCFHCBADHACAFGCFICBFCASC',
         'WDJECHBCGEAHFBCHECWJAIBWDJFIBWD',
         'HFEJDHBCJDSBGFIBSCGFBJSDGBHJDHFJAB']

# reels = ['FCDBACSAEHDAEBSDEAGCBDIAFDJCDBGCDGEBSDCFBCIDFGDBIECJEDBEFSBAEHCBESDEBHCBIDFCJECFEBDGCBEDBGECIBCSDCBEAFCJCIDFBDEBCEDGBSEDCIJEBDICFDGBCEASDBCGCEBFDEGCEDBEFGBDCSECGBSCDIAB',
#          'GDSADGFAHFCBHAIFHDEIAHEIAJDWBHADFHAEHBWABSADWEJBACDSFGDFGDFESFDGCDEWGECFBGFASFCBHCDESADIAHEAIFDSHDEJBSADHFIDASDAWEJAEJDAHFWDGFAIAGEFSDGFDSFGDADSIAEFDGAFDBAJFEADISADHAGDAJE',
#          'SCAEGDBCFHCBADHACEDCBAGCFDHEDIBAHBFGDFSADHFBJEACFJDBGEBHEDCEDGECFAEGCAECGBAFGCFICBFCASCAEGABCFHCBADHACEDCBAJCFDHEDIBAHBFHDFSDCSADHFBJEACFJDBGEASEDIEDHECFAEGCAECHBAFGCFICBFCASC',
#          'WDJECHBCGEAHFBCHECBAFCDHFCGFCWAEICBHAFGBCHAFBEHFAGEBGFDHEAJDBHFCJDBHFAIBWDJCAIBWDJCIBWDJECHBCSEAHBCGFCEBFCDHFAGFCJAEICBHAFGBCHAFBEHFBGEBIFDHEAJDBWAFJBDWFAIBWDCJAIBWDJFIBWD',
#          'HFEJDHBCJDSBGFIBSCJDSAGBSAHBAJFHAIDHEJDGBJFDICHFBGFSBIFEJDHBCJDBGABIFSCJDSAGBSAIBAJDHAIDHFJDGAJFDICHEAGFSBHFEDAJFCBJFADGCSADIHJABJIGAFBIJHDSCABHGDFIJHFBJSDGBHJDHFJAB']


def reel_round(reel: str = "", visible: int = 3) -> str:
    return reel + reel[0: visible - 1]


def to_set(reel_round):
    s = set()
    for i in range(len(reel_round) - (3-1)):
        col = reel_round[i: i+3]
        count = reel_round.count(col)
        s.add((col, count))
    return s


visible = [3, 3, 3, 3, 3]
reels_round = [reel_round(reel, 3) for reel in reels]

print(reels_round)


reels_round_list_0 = [
    ('CGB', 1),
    ('BFC', 1),
    ('BAC', 1),
    ('IJE', 1),
    ('DBA', 1),
    ('DFG', 1),
    ('ESD', 1),
    ('ABF', 1),
    ('SED', 1),
    ('BDC', 1),
    ('BEF', 2),
    ('DIC', 1),
    ('DBI', 1),
    ('EBC', 1),
    ('EFS', 1),
    ('EDG', 1),
    ('EDB', 3),
    ('BGC', 1),
    ('BID', 1),
    ('EBS', 2),
    ('AFD', 1),
    ('CIB', 1),
    ('DCS', 1),
    ('EHC', 1),
    ('BEA', 1),
    ('CGC', 1),
    ('FDJ', 1),
    ('BSD', 2),
    ('CIJ', 1),
    ('DEG', 1),
    ('GEC', 1),
    ('DIA', 2),
    ('HDA', 1),
    ('FGD', 1),
    ('CBE', 3),
    ('DCF', 1),
    ('BCE', 2),
    ('GBD', 1),
    ('BDI', 2),
    ('IBC', 1),
    ('FBC', 1),
    ('ACS', 1),
    ('GCB', 2),
    ('IAF', 1),
    ('BED', 1),
    ('JEB', 1),
    ('ECI', 1),
    ('GCD', 1),
    ('AFC', 1),
    ('CFB', 1),
    ('DGB', 2),
    ('SBA', 1),
    ('FCJ', 2),
    ('CED', 2),
    ('DCI', 1),
    ('AGC', 1),
    ('CEA', 1),
    ('BFD', 1),
    ('BAE', 1),
    ('DEB', 2),
    ('BGE', 1),
    ('EBF', 1),
    ('DGC', 1),
    ('EAS', 1),
    ('DFB', 1),
    ('BDE', 1),
    ('BCG', 1),
    ('GCE', 2),
    ('ECJ', 1),
    ('EAG', 1),
    ('IDF', 3),
    ('FCD', 1),
    ('ASD', 1),
    ('FGB', 1),
    ('BES', 1),
    ('SEC', 1),
    ('GDB', 1),
    ('EDC', 1),
    ('CFD', 1),
    ('BHC', 1),
    ('SDE', 2),
    ('HCB', 2),
    ('GBC', 1),
    ('BSC', 1),
    ('BDG', 1),
    ('DFC', 1),
    ('CBI', 1),
    ('SDC', 2),
    ('JCD', 1),
    ('BCI', 1),
    ('EBD', 2),
    ('CEB', 1),
    ('SAE', 1),
    ('CSA', 1),
    ('CJC', 1),
    ('DCB', 1),
    ('FEB', 1),
    ('IAB', 1),
    ('CFE', 1),
    ('DBC', 1),
    ('CDG', 1),
    ('BIE', 1),
    ('IEC', 1),
    ('AEH', 2),
    ('JCI', 1),
    ('CSE', 1),
    ('CJE', 2),
    ('GBS', 2),
    ('CDI', 1),
    ('FDE', 1),
    ('FSB', 1),
    ('EBH', 1),
    ('SDB', 1),
    ('ICF', 1),
    ('CID', 2),
    ('CBD', 1),
    ('DEA', 1),
    ('DGE', 1),
    ('EGC', 1),
    ('EFG', 1),
    ('ECG', 1),
    ('FDG', 1),
    ('JEC', 1),
    ('SCD', 1),
    ('GEB', 1),
    ('DBG', 2),
    ('CSD', 1),
    ('JED', 1),
    ('CDB', 2),
    ('DAE', 1),
    ('BCS', 1),
    ('EHD', 1),
    ('DJC', 1),
    ('EAF', 1),
    ('AEB', 1),
    ('DBE', 2),
    ('BSE', 1),
    ('ECF', 1),
    ('FBD', 1)
]
reels_round_set_0 = set(reels_round_list_0[initial: initial + increment])
reels_round_set_1234 = [to_set(reel) for reel in reels_round[1:5]]
reels_round_set = [reels_round_set_0] + reels_round_set_1234


compute_combinations_GM(reels_round_set=reels_round_set)

print("termino:", reels_round_list_0[initial: initial + increment])
