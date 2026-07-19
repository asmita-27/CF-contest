from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    res = n+1
    for i in range(n+1):
        if i > n - k:
            continue 
        if i < k:
            continue
        x =0 
        for j in range(i):
            if s[j]=="L":
                x+=1
        for j in range(i,n):
            if s[j] =="R":
                x+=1
        res = min(res, x)
    if res == n+1:
        print(-1)
    else:
        print(res)