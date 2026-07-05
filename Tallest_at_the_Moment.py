from collections import defaultdict, Counter, deque
import os
import math
import sys
from bisect import bisect_right 

# for _ in range(int(input())):
n = int(input())
h= []
l = []
for _ in range(n):
    hi,li = map(int,input().split())
    h.append(hi)
    l.append(li)
suf = [0] * n
suf[-1] = h[-1]
for i in range(n - 2, -1, -1):
    suf[i] = max(h[i], suf[i + 1])
q = int(input())
t = list(map(int, input().split()))
for i in t:
    pos = bisect_right(l, i) 
    print(suf[pos])