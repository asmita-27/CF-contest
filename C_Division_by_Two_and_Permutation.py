from collections import defaultdict, Counter, deque
import os
import math
import sys


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    used = set()
    flg = 0
    a.sort(reverse=True)  
    for x in a:
        while x > 0:
            if x <= n and x not in used:
                used.add(x)
                break
            x //= 2
        else:
            flg = 1
  
    if flg :
        print("NO")
    else:
        print("YES")
