from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    l, r = 0, 1
    flg = 0
    if n==1:
        print("YES" if a[0] == k else "NO")
        continue
    a.sort()
    while r < n:
        diff = a[r] - a[l]
        if diff ==k:
            flg =1
            break
        elif diff<k:
            r+=1
        else:
            l+=1
        if l==r:
            r+=1
            
    if flg:
        print("YES")
    else:
        print("NO")
    

