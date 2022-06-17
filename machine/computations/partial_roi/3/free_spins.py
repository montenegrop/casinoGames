reel_spins = [[11, 10, 9, 7, 6, 5, 7, 0, 9, 10, 8, 7, 4, 9, 3, 7, 10, 3, 11, 9, 7, 6, 5, 9, 7, 10, 8, 7, 0, 4, 9, 7, 3, 11, 2, 7, 3, 9, 5, 10, 8, 9, 7, 8, 3, 9, 6, 10, 7, 8, 9, 11, 0, 8, 2, 0, 9, 10, 8, 4, 7, 8, 11, 9, 10, 5, 2, 8, 0, 7, 10, 9, 8, 7, 9, 8, 7, 10, 8, 11, 5, 8, 9, 5, 10, 4, 7, 8, 6, 10, 5, 9, 3, 8, 11, 5, 10, 8, 7, 0, 10, 8, 0, 2, 9, 3, 8, 6, 10, 8, 7, 10, 9, 7, 8, 5, 10, 0, 7, 8, 9, 3, 2, 7, 10, 8, 3, 9, 6, 8, 5, 10, 9, 7, 11, 0, 8, 10, 9, 5, 9, 7, 10, 6, 8, 7, 5, 9, 7, 8, 10, 7, 6, 5, 10, 8, 9, 0, 7, 9, 5, 10, 0, 9, 8, 3, 11, 10],
              [2, 7, 10, 6, 8, 5, 2, 11, 0, 9, 4, 5, 11, 7, 8, 4, 10, 11, 6, 8, 3, 4, 6, 11, 3, 7, 9, 5, 8, 6, 11, 5, 10, 4, 11, 0, 2, 7, 6, 11, 4, 8, 3, 0, 11, 6, 10, 5, 11, 4, 3, 7, 9, 1, 8, 6, 11, 1, 2, 8, 4, 0, 7, 10, 11, 2, 1, 3, 6, 5, 1, 4, 9, 7, 8, 1, 11, 5, 1, 6, 2, 0, 10, 8, 11, 6,
                  5, 7, 3, 1, 8, 9, 6, 4, 11, 8, 0, 7, 11, 6, 5, 3, 1, 8, 11, 2, 1, 9, 10, 11, 2, 7, 8, 4, 0, 7, 11, 6, 5, 8, 11, 3, 2, 11, 3, 1, 8, 10, 4, 2, 8, 11, 5, 6, 7, 11, 4, 8, 1, 7, 4, 11, 8, 0, 3, 11, 7, 6, 8, 5, 11, 6, 8, 10, 11, 2, 6, 7, 11, 8, 3, 0, 11, 8, 4, 11, 5, 8, 11, 2, 7],
              [8, 11, 10, 7, 11, 9, 6, 8, 5, 9, 7, 11, 0, 10, 8, 6, 5, 11, 6, 8, 7, 11, 6, 0, 11, 6, 10, 8, 0, 7, 8, 10, 9, 6, 11, 8, 7, 6, 8, 5, 9, 4, 11, 8, 7, 9, 10, 8, 11, 6, 10, 8, 6, 11, 7, 9, 8, 10, 6, 9, 7, 8, 10, 4, 11, 8, 9, 10, 3, 11, 9, 4, 8, 6, 7, 9, 8, 0, 6, 7, 11, 8,
               0, 5, 11, 10, 0, 8, 9, 4, 7, 10, 9, 8, 11, 6, 0, 7, 9, 5, 0, 7, 6, 8, 7, 6, 11, 4, 8, 2, 9, 11, 4, 10, 7, 8, 6, 4, 7, 9, 8, 11, 2, 4, 10, 6, 7, 11, 8, 9, 0, 4, 10, 2, 8, 7, 11, 8, 10, 11, 6, 7, 8, 10, 0, 6, 7, 2, 4, 11, 3, 7, 0, 9, 7, 11, 3, 6, 10, 4, 7, 11, 9, 8, 11],
              [10, 11, 8, 6, 9, 5, 4, 10, 3, 7, 8, 2, 4, 1, 10, 4, 7, 6, 10, 3, 9, 2, 11, 8, 10, 5, 6, 3, 9, 4, 10, 6, 5, 11, 6, 9, 8, 10, 3, 9, 2, 6, 10, 4, 6, 1, 2, 9, 6, 7, 11, 1, 3, 6, 4, 9, 5, 10, 1, 8, 4, 2, 9, 11, 3, 6, 2, 4, 9, 1, 8,
               10, 2, 9, 3, 1, 6, 4, 10, 5, 8, 9, 10, 11, 7, 9, 5, 4, 9, 6, 0, 11, 6, 8, 9, 3, 10, 2, 4, 9, 10, 5, 3, 2, 8, 10, 6, 8, 11, 7, 6, 10, 11, 9, 5, 2, 6, 10, 9, 2, 11, 5, 8, 6, 10, 3, 11, 6, 10, 9, 7, 10, 4, 8, 6, 11, 4, 10, 11],
              [11, 10, 6, 5, 2, 9, 0, 11, 4, 6, 3, 2, 10, 8, 11, 9, 6, 7, 10, 0, 2, 4, 10, 2, 5, 9, 3, 2, 10, 0, 6, 2, 8, 6, 10, 4, 8, 0, 3, 11, 10, 2, 3, 5, 8, 6, 3, 2, 11, 7, 9, 2, 10, 3, 8, 11, 0, 6, 8, 4, 5, 6, 11, 10, 2, 3, 9, 0, 4, 3, 9, 6, 5, 7, 4, 8, 11, 2, 4, 8, 0, 2, 3, 11, 10, 2, 9, 6, 5, 10, 0, 4, 11, 2, 3, 8, 11, 9, 8, 4, 6, 11, 2, 3, 6, 4, 9, 2, 7, 8, 11, 2, 6, 9, 10, 2, 6, 11, 8, 5, 9, 0, 11, 8, 3, 4, 2, 11, 10, 2, 3, 5, 11, 6, 10, 3, 2, 4, 8, 0, 9, 11, 10, 4, 5, 8, 6, 3, 2, 4, 6, 10, 2, 0, 8, 5, 10, 4, 2, 8, 4, 6, 2, 11, 10]]

symbols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "W", "S"]

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

visible = [3, 3, 3, 3, 3]
free_spins = [0, 0, 15, 20, 25]
multiplier = 3


def mapping(number):
    # S = free spins, W = wild
    len_symbols = len(symbols) - 1
    return symbols[len_symbols - number]


def convert(reels):
    reels_list = []
    for reel in reels:
        reel_string = ''.join(mapping(el) for el in reel)
        reels_list.append(reel_string)
    return reels_list


convert(reel_spins)


reels_free_spins = ['ABCEFGESCBDEHCIEBIACEFGCEBDESHCEIAJEICGBDCEDICFBEDCASDJSCBDHEDACBGJDSEBCDECDEBDAGDCGBHEDFBGCIDAGBDESBDSJCIDFBDEBCEDGBSEDCIJEBDICFDGBCEASDBCGCEBFDEGCEDBEFGBDCSECGBSCDIAB',
                    'JEBFDGJASCHGAEDHBAFDIHFAIECGDFAGBHASJEFAHDISAFBGAHIECWDFAWJDHSEBAJWIFGWHCEDWAGWFJSBDAFGEIWDCFHADSEAFGIWDAJWCBAJEDHSEAFGDAIJAIWDBHJDAGFEAHDWEHADSIAEFDGAFDBAJFEADISADHAGDAJE',
                    'DABEACFDGCEASBDFGAFDEAFSAFBDSEDBCFADEFDGCHADECBDAFBDFAECDBFCEDBHADCBIACHDFECDSFEADSGABSDCHEBCDAFSECGSEFDEFAHDJCAHBEDFHECDAJHBFEADCSHBJDEADBAFEDBSFEJHAIESCEAIFBHEACDA',
                    'BADFCGHBIEDJHWBHEFBICJADBGFICHBFGAFCDBICJFBHFWJCFEAWIFHCGBWDHJCAIFJHCWDBJCIWFHBGDCBAECGHCFSAFDCIBJHCBGIJDBFDAEFBACGJFBCJAGDFBIAFBCEBHDFAHBA',
                    'ABFGJCSAHFIJBDACFEBSJHBJGCIJBSFJDFBHDSIABJIGDFIJAECJBIDASFDHGFABJICSHICFGEHDAJHDSJIABJCFGBSHAJIDACDHFAJIFHCJEDAJFCBJFADGCSADIHJABJIGAFBIJHDSCABHGDFIJHFBJSDGBHJDHFJAB']  # for r in reels_free_spins:

# [165,168,162,136,162] trello

lengths = [168, 171, 165, 139, 165]
