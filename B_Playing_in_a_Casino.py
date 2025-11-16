from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,m = map(int,input().split())  
    cols= [[] for _ in range(m)]
    for i in range(n):
        row = list(map(int,input().split()))
        for j in range(m):
            cols[j].append(row[j])
    res = 0
    for j in range(m):
        arr = cols[j]
        arr.sort()
        
        for i in range(n):
            res += arr[i] * (2*i - n + 1)
    print(res)