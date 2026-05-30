from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n =int(input())
    a = list(map(int, input().split()))
    x  = 0
    res = []
    cur =  float('inf')
    for i , j in enumerate(a, 1):
        x += j
        cur = min(cur, x//i)
        res.append(cur)
    print(*res)