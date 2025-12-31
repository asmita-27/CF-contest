from collections import defaultdict, Counter, deque
import os
import math
import sys

from itertools import product

for _ in range(int(input())):
    n = int(input().strip())
    s = input().strip()

    se = set() 
    for i in range(n):
        for l in range(1, 6):
            if i + l <= n:
                se.add(s[i:i+l])
 
    for length in range(1, 6):
        for p in product('abcdefghijklmnopqrstuvwxyz', repeat=length):
            t = ''.join(p)
            if t not in se:
                print(t)
                break
        else:
            continue    
        break
