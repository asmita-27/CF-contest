from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    idx = -1
    for i in range(1,n):
        if a[i]!=a[i-1]:
            idx= i
            res.append((1,  i+1))
    if idx==-1:
        print("NO")
        continue
    for i in range(1,n):
        if a[i]==a[i-1]:
            res.append((idx+1, i+1 ))    
    print("YES")
    for u,v in res:
        print(u,v)