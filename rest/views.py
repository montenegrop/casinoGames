from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
from machine.computations.calculate_roi import compute_GM
from machine.computations.random_numbers import random_integer
from machine.computations.examples.victorious_payment import payment
from machine.models import Machine
from machine.computations.parameters import roll, winning_chains, visibles, winnings

f = open("rest/dummy_data/dama_muerta_1.json", "r")
data = json.load(f)
f.close()


@api_view()
def dummy_casino_json(request):
    return Response(data)


@api_view()
def dummy_victorious_json(request):
    roll = []
    for num in range(0, 5):
        roll.append(random_integer(0, 8))

    result = payment(roll=roll, bet=1)
    data = result
    return Response(data)


@api_view()
def realistic_victorious_json(request):
    bet = 1

    machine = Machine.objects.first()
    random_roll = roll(lengths_dict={
        "1": 101,
        "2": 102,
        "3": 103,
        "4": 104,
        "5": 105
    })

    visible = visibles(machine.reels_round, random_roll, [3, 3, 3, 3, 3])
    chains = winning_chains(screen=visible, total_reels=5, wild="k")
    wins = winnings(chains, payments=machine.payments,
                    free_spins_symbol="L", free_spins_tuple=machine.free_spins)

    # result = payment(roll=roll, bet=1)
    # data = result
    # data["bet"] = bet
    return Response(wins)


@api_view()
def victorious2(request):
    bet = 1

    machine = Machine.objects.get(name="victoriousTests")
    reels = machine.normal_reel
    payments = machine.payments
    visible = machine.visible
    free_spins_list = machine.free_spins

    gmlist = compute_GM(reels=reels, payments=payments, visible=visible,
                        free_spins_list=free_spins_list)

    gm = {"G": gmlist[0], "M": gmlist[1], "counter": gmlist[2]}

    return Response(gm)
