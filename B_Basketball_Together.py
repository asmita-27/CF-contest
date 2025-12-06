from collections import defaultdict, Counter, deque
import os
import math
import sys




n, D = map(int, input().split())
P = sorted(map(int, input().split()))

wins = 0
team = []

for p in P:  
    team.append(p)
    if team[-1] * len(team) > D:
        wins += 1
        team = []

print(wins)
