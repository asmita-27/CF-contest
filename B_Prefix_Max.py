from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = max(a)
    id = a.index(x)
    a[id], a[0] = a[0], a[id]
    pref = []
    curr = float('-inf')
    for i in a:
        curr = max(curr, i)
        pref.append(curr)
    print(sum(pref))