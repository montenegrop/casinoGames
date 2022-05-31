

from array import array
from examples.victorious_parameters import reel_normal


def compute_G(reels: array, payments: dict = None) -> float:
    return reels[0][0]


print(compute_G(reel_normal))
