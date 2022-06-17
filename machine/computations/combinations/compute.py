wild = "W"
freeSpin = "S"

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
reels = ['FCDBACSAEHDAEBSDEAGCBDIAFDJCDBGCDGEBSDCFBCIDFGDBIECJEDBEFSBAEHCBESDEBHCBIDFCJECFEBDGCBEDBGECIBCSDCBEAFCJCIDFBDEBCEDGBSEDCIJEBDICFDGBCEASDBCGCEBFDEGCEDBEFGBDCSECGBSCDIAB',
         'GDSADGFAHFCBHAIFHDEIAHEIAJDWBHADFHAEHBWABSADWEJBACDSFGDFGDFESFDGCDEWGECFBGFASFCBHCDESADIAHEAIFDSHDEJBSADHFIDASDAWEJAEJDAHFWDGFAIAGEFSDGFDSFGDADSIAEFDGAFDBAJFEADISADHAGDAJE',
         'SCAEGDBCFHCBADHACEDCBAGCFDHEDIBAHBFGDFSADHFBJEACFJDBGEBHEDCEDGECFAEGCAECGBAFGCFICBFCASCAEGABCFHCBADHACEDCBAJCFDHEDIBAHBFHDFSDCSADHFBJEACFJDBGEASEDIEDHECFAEGCAECHBAFGCFICBFCASC',
         'WDJECHBCGEAHFBCHECBAFCDHFCGFCWAEICBHAFGBCHAFBEHFAGEBGFDHEAJDBHFCJDBHFAIBWDJCAIBWDJCIBWDJECHBCSEAHBCGFCEBFCDHFAGFCJAEICBHAFGBCHAFBEHFBGEBIFDHEAJDBWAFJBDWFAIBWDCJAIBWDJFIBWD',
         'HFEJDHBCJDSBGFIBSCJDSAGBSAHBAJFHAIDHEJDGBJFDICHFBGFSBIFEJDHBCJDBGABIFSCJDSAGBSAIBAJDHAIDHFJDGAJFDICHEAGFSBHFEDAJFCBJFADGCSADIHJABJIGAFBIJHDSCABHGDFIJHFBJSDGBHJDHFJAB']

visible = [3, 3, 3, 3, 3]

symbols_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
symbols_1_3_5 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L"]
symbols_2_4 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]


def reel_round(reel: str, visible: int) -> str:
    return reel + reel[0: visible - 1]


reels_round = [reel_round(reel, visible[i]) for (i, reel) in enumerate(reels)]

f = open("combinations.json", "a")
f.write("{" + "\n")


def values(chain):
    x = chain[0]
    i = 1
    while x + chain[i]:


f.truncate(f.tell() - 3)
f.write("\n" + "}")
f.close()
