from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,k,m = map(int,input().split())
    if k>m:
        print("NO")
        continue
    else:
        print("YES")
    res = []
    for i in range(1,n+1):
        if i%k==0:
            res.append(m-k+1)
        else:
            res.append(1)
    print(*res)