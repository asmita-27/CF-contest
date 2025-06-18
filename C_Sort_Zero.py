from collections import defaultdict, Counter, deque
import os
import math
import sys

 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    stk = []
    maxx = a[0]
    stk.append(a[0])
    for i in range(n):
        if a[i] in s:
            maxx =0
            while stk:
                s.add(stk.pop())
        elif a[i]<maxx:
            while stk:
                s.add(stk.pop())
            if a[i] not in s:
                maxx = a[i]
                stk.append(a[i])
            else:
                maxx = 0
        else:
            stk.append(a[i])
            maxx = a[i]
    print(len(s))