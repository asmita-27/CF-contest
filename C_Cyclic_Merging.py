from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    m = 0
    for i in range(n):
        if a[i]>a[m]:
            m = i
    a.append (a[0])
    k = -a[m]
    for i in range(n):
        k += max(a[i], a[i+1])
    print(k)