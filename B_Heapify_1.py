from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    cpy = sorted(a)
    x = []
    for i in range(n):
        if a[i] != cpy[i]:
            x.append(i)
    n = len(x) 
    if n== 0:
        print("YES")
    elif n%2==0 and n>=2:
        print("YES")
    else:
        print("NO")