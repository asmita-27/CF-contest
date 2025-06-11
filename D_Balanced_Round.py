from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cnt , ans= 1,1
    for i in range(1,n):
        if a[i]-a[i-1]>k:
            cnt = 1
        else:
            cnt += 1
        ans = max(ans, cnt)
        
    print(n-ans)
    

    