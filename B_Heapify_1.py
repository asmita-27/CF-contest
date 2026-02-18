from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a =[0]+ list(map(int,input().split()))
    i = 1
    while i<=n:
        j = i
        while j<=n:
            k = i*2
            while k<=n:
                if a[k//2]>a[k]:
                    a[k//2],a[k] = a[k],a[k//2]
                k*=2
            j*=2
        i+=2

    if a[1:]==sorted(a[1:]):
        print("YES")
    else:
        print("NO")