from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,x, m = map(int, input().split())
    l,r =  x,x
    for _ in range(m):
        a,b = map(int, input().split())
        if max(a,l)<=min(b,r):
            l = min(l,a)
            r = max(r,b)
    print(r-l+1)