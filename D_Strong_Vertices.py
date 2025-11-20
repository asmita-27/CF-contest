from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n=int(input())
    a=[*map(int,input().split())]
    b=[*map(int,input().split())]
    c=[a[i]-b[i] for i in range(n)]
    mx=max(c)
    ans=[]
    for i in range(n):
        if c[i]==mx:ans.append(i+1)
    print(len(ans))
    print(*ans)