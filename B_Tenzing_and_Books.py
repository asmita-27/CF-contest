from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):

    n, x = map(int, input().split())
    pre = [[] for _ in range(3)]
    
    for i in range(3):
        s = 0
        pre[i].append(s)
        row = list(map(int, input().split()))
        for ai in row:
            if (s | ai) != s:
                s |= ai
                pre[i].append(s)
    
    ans = False
    for A in pre[0]:
        for B in pre[1]:
            for C in pre[2]:
                if (A | B | C) == x:
                    ans = True
                    break
            if ans:
                break
        if ans:
            break
    
    print("YES" if ans else "NO")