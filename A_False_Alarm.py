from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = True
    first = True
    i =0 
    while i <n:
        if not first and a[i] == 1:
            ans = False
            break
        if first and a[i] == 1:
            i = i+ x - 1
            first = False
        i+=1
    if   ans:
        print("YES")
    else:
        print("NO")