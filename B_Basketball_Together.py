from collections import defaultdict, Counter, deque
import os
import math
import sys

n, D = map(int, input().split())
P = sorted(map(int, input().split()))

wins = 0
l = 0
r = n - 1
while l <= r:
    x = P[r]
    need = D // x + 1
    if l + (need - 1) > r:
        break
    wins += 1
    l += need - 1
    r -= 1

print(wins)
