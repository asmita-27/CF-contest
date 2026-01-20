from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,m,h = map(int, input().split())
    a = list(map(int, input().split()))
    org = a[:]
    mod = []
    flg = [False]*n
    for i in range(m):
        b,c = map(int, input().split())
        b-=1
        if a[b]+ c<=h :
            if not flg[b]:
                flg[b] = True
                mod.append(b)
            a[b] += c
        else:
            for i in mod:
                a[i] = org[i]
                flg[i] = False
            mod.clear()
    print(*a)