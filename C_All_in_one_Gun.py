from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,h,k = map(int,input().split())
    a = list(map(int,input().split()))
    
    S = sum(a)
    
    full = h // S
    time = full * (n + k)
    rem = h - full*S
    
    if rem == 0:
        print(time - k)
        continue
    
    prefix = 0
    normal = float('inf')
    
    for i in range(n):
        prefix += a[i]
        if prefix >= rem:
            normal = time + i + 1
            break
    
    mx = max(a)
    prefix = 0
    swapped = float('inf')
    
    for i in range(n):
        prefix += a[i]
        if prefix - a[i] + mx >= rem:
            swapped = time + i + 1
            break
    
    print(min(normal, swapped))