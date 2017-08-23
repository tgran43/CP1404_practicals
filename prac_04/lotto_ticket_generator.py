import random

quick_picks = []
number_of_quick_picks = int(input("How many quick picks? "))
for number in range(number_of_quick_picks):
    for i in range(6):
        quick_pick = random.randint(1, 46)
        while quick_pick in quick_picks:
            quick_pick = random.randint(1, 46)
        quick_picks.append(quick_pick)
    quick_picks.sort()
    for i in quick_picks:
        print("{:2}".format(i), end=" ")
    print()
    quick_picks = []
