from collections import defaultdict, Counter, deque
import os
import math
import sys

 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d,c = {},sorted(a)
    b = c.copy()
    for i in range(1 , n):
        if b[i] == b[i-1]:
            continue
        if b[i] % b[i-1] == 0:
            continue
        b[i] = b[i-1] * (1 + b[i] // b[i-1])
    for i in range(n):
        if c[i] != b[i]:
            d[c[i]] = b[i] - c[i]
    l = []
    for i in range(n):
        if a[i] in d:
           l.append([i+1 , d[a[i]]])
    print(len(l))
    for v in l:
        print(*v)

