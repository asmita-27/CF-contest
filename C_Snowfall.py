from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input()) 
    a, b, c, d = [], [], [], [] 
    arr = list(map(int, input().split())) 
    for x in arr:
        if x % 6 == 0:
            a.append(x)
        elif x % 2 == 0:
            b.append(x)
        elif x % 3 == 0:
            c.append(x)
        else:
            d.append(x) 
    ans = a + b + d + c
    print(*ans)