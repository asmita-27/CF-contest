from collections import defaultdict, Counter, deque
import os
import math
import sys


n, D = map(int, input().split())
P = sorted(map(int, input().split()))

wins = 0
used = 0
i = n - 1

while i >= 0:
    x = P[i]
    need = D // x + 1
    if i + 1 - used < need:
        break
    used += need
    wins += 1
    i -= 1

print(wins)
