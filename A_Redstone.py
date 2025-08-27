from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    g = list(map(int, input().split()))
    
    fq = {}
    ok = False
    
    for g in g:
        fq[g] = fq.get(g, 0) + 1
        if fq[g] >= 2:
            ok = True   
    print("YES" if ok else "NO")