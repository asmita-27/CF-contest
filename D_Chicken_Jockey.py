from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    attacks = 0
    fall_pot = 0  # accumulated fall damage from above

    # Process bottom to top
    for i in range(n):
        health = h[i] - fall_pot
        if health > 0:
            attacks += health
            # killed with sword -> reset fall damage (stack breaks)
            fall_pot = 0
        else:
            # killed via fall -> add 1 fall damage for next mob
            fall_pot += 1

    print(attacks)