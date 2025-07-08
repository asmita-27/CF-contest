from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans  = a[0]
    minn =  min(0,a[0])
    sm = a[0]
    
    for i in range(1, n):
        if abs(a[i]%2)== abs(a[i-1]%2):
            minn = 0
            sm = 0
        
        sm += a[i]
        # sm = max(sm, a[i])
        ans = max(ans, sm - minn)
        minn = min(minn, sm)
    print(ans)