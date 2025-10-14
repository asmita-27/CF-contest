from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    aQ = list(map(int, input().split()))
    minX = 31
    for x in aQ:
        add = 1 << (x - 1)   
        div = 1 << x      
        for i in range(n):
            if a[i] % div == 0:
                a[i] += add
    print(*a)