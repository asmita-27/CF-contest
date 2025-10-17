from collections import defaultdict, Counter, deque
import os
import math
import sys


n, q = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))
  
pos = {}
for i, color in enumerate(a):
    if color not in pos:
        pos[color] = i + 1 

for t in q:
    p = pos[t]
    print(p, end=' ')
     
    for c in pos:
        if pos[c] < p:
            pos[c] += 1
    pos[t] = 1
