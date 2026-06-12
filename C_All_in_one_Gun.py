from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,h,k = map(int,input().split())
    a = list(map(int,input().split()))
    sm = sum(a)
    full = h // sm
    time = full * (n + k)
    rem = h - full*sm
    
    if rem == 0:
        print(time - k)
        continue
    
    pref = 0
    normal = float('inf')
    for i in range(n):
        pref += a[i]
        if pref >= rem:
            normal = time + i + 1
            break
    mx = max(a)
    pref = 0
    swp = float('inf')
    for i in range(n):
        pref += a[i]
        if pref - a[i] + mx >= rem:
            swp = time + i + 1
            break
    
    print(min(normal, swp))