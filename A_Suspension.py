from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    y,r = map(int, input().split())
    ans = 0
    if y == 0 and r == 0:
        print(0)
        continue
    if y // 2 >= r: 
        ans += y // 2 
        n -= y // 2 
 
        if n > 0: 
            ans += min(n, r) 
            n -= min(n, r)
    else:
        ans += r 
        n -= r
        if n > 0: 
            ans += min(n, y // 2) 
            n -= min(n, y // 2)
    
    print(ans)
 