from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    cv = []
    for _ in range(n):
        d = list(map(int, input().split()))
        k = d[0]
        v = d[1:]
        
        b = 0 
        for j in range(k):
            b = max((b, v[j]-j))
        cv.append((b,k))
    cv.sort()
    totK = 0
    p =0
    for b, k in cv:
        p = max(p, b-totK)
        totK += k
    print(p+1)

