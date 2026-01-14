from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    
    a.sort()
    cnt =0
    for i in range(n-1,-1,-1):
        cnt += a[i]*m
        m = max(0,m-1)
    print(cnt)