from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    l,r = 0,n-1
    minn,maxx = 1,n
    while l <= r:
        if a[l] == minn:
            l+=1
            minn +=1
        elif a[r] == maxx:
            r-=1
            maxx -= 1
        elif a[l] == maxx:
            l+=1
            maxx -= 1
        elif a[r] == minn:
            r-=1
            minn += 1
        else:
            break
    if l<=r:
        print(l+1, r+1)
    else:
        print(-1)