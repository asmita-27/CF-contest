from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted([(a[i], i+1) for i in range(n)], reverse=True)
    pos = [0]*(n+1)
    tm =0
    k =1
    for val, idx in b:
        if k%2==1:
            x = (k+1)//2
        else:
            x = - (k//2)
        pos[idx] = x
        tm += 2*abs(x)*val
        k+=1
    print(tm)
    print(*pos)