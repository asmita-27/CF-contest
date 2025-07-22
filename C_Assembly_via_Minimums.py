from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    # a = []    
    b.sort()
    # set(b)
    # for i in b:
    #     if i not in a:
    #         a.append(i)
    # if len(a) < n:
    #     a.append(b[n-2] + b[n-1])

    # print(*a)
    i = 0
    for j in range(n-1,0,-1):
        print(b[i], end=' ')
        i += 1
    print(b[-1])
