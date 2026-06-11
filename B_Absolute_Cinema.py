from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # mx = max(a)
    # for i in range(n):
    #     if a[i]!= mx and a[i]>b[i]:
    #         a[i], b[i] = b[i], a[i]
    # print(mx+sum(b))
    mx ,s= 0,0
    for x, y in zip(a, b):
        s += max(x, y)
        mx = max(mx, min(x, y))
    print(s + mx)