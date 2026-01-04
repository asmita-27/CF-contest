from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    e=0
    for i in range(1,n-1,2):
        if a[i]!=a[i+1]:
            e=1
            break
    print("NO" if e else "YES")