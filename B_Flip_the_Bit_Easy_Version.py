from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    p = int(input())
    x = [a[p - 1]] + a + [a[p - 1]]
    l = 0
    r = 0
    for i in range(p):
        if x[i] != x[i + 1]:
            l += 1
    for i in range(p, n + 1):
        if x[i] != x[i + 1]:
            r += 1  
    print(max(l, r))