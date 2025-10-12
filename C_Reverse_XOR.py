from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print("YES")
        continue

    bits = []
    x = n
    while x:
        bits.append(x & 1)
        x >>= 1
    m = len(bits)

    found = False
    for l in range(m, 61):   
        ok = True 
        for i in range((l + 1) // 2):
            lft = bits[i] if i < m else 0
            rghtId = l - 1 - i
            rght = bits[rghtId] if rghtId < m else 0
            if lft != rght:
                ok = False
                break
        if not ok:
            continue 
        if l % 2 == 1:
            mid = l // 2
            midBit = bits[mid] if mid < m else 0
            if midBit != 0:
                continue
        found = True
        break

    print("YES" if found else "NO")
