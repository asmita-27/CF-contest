from collections import defaultdict, Counter, deque
import os
import math
import sys

n,d = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = wn= 0
for i in reversed(a):
    ans+=1
    if ans*i >= d:
        wn+=1
        ans =0
print(wn)
