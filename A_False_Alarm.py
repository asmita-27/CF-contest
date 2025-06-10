from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    c,d = -1,-1
    for i in range(n):
        if a[i]==1:
            c=i
            break
    for i in range(n-1,-1,-1):
        if a[i]==1:
            d=i
            break
    if c==d:
        print("YES")
    else:
        if d-c+1>x:
            print("NO")
        else:
            print("YES")