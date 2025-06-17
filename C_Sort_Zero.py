from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    n = int(input())
    a = list(map(int,input().split()))
    cnt = Counter(a)
    ans = 0
    for i in range(1,n):
        if a[i] in cnt and cnt[a[i]]>=1:
            ans += 1
            cnt[a[i]] = 0
        else:
            
    
    print(ans)