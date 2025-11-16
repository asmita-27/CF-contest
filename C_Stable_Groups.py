from collections import defaultdict, Counter, deque
import os
import math
import sys


n,k,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort() 
need = []
for i in range(n-1):
    gp = a[i+1]-a[i]
    if gp > x:
        nd = (gp+x-1)//x -1
        need.append(nd)
need.sort()
grps = 1 + len(need)
for nd in need:
    if nd <= k:
        k -= nd
        grps -= 1
    else:
        break
print(grps)
