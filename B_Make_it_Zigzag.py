from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    pre = [0]*(n)
    res =0
    pre[0] = a[0]
    for i in range(n):
        pre[i] = max(pre[i-1],a[i])
    for i in range(0,n,2):
        dif = -1
        if i>0:
            dif = max(dif, a[i]-pre[i-1])
        if i<n-1:
            dif = max(dif, a[i]-pre[i+1])
        res += dif+1
    print(res)