

from .parameters import winning_chains, winnings


def reel_round(reel: str, visible: int) -> str:
    return reel + reel[0: visible - 1]


def compute_GM(
    reels: list,
    payments: dict,
    free_spins_list,
    visible=[3, 3, 3, 3, 3]
) -> float:

    wild = "W"
    freeSpins = "S"

    # g, M, f, combinations
    globalGM = [0, 0, 0, 0]

    sizes = [len(reel) for reel in reels]
    reels_round = [reel_round(reel, visible[i])
                   for (i, reel) in enumerate(reels)]

    def GM(combination):
        win_chains = winning_chains(combination, 5, wild)
        w_dict = winnings(win_chains, payments, freeSpins, free_spins_list)
        g = w_dict["total_win"]
        m = w_dict["free_spins"]
        return (g, m)

    def combinations(combination=[]):
        arr = combination
        i = len(arr)
        for j in range(sizes[i]):
            r = reels_round[i][j: j + visible[i]]
            if len(arr) == len(sizes) - 1:
                gm = GM(arr + [r])
                globalGM[0] += gm[0]
                globalGM[1] += gm[1]
                globalGM[2] += 1
            else:
                if i == 1:
                    print("array:", arr + [r], "i:",
                          1, "j:", j, "GM:", globalGM)
                combinations(combination=arr + [r])

    combinations()
    return globalGM
