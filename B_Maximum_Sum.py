from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    
    ans = sum(a)
    while k > 0:
        a.sort()
        if a[0]+a[1]<= a[-1] or a[-1] > ans:
            ans -= (a[0] + a[1])
            a.pop(0)
            a.pop(0)
        elif a[0]+a[1]>a[-1] or a[-1]<=ans:
            ans -= a[-1]
            a.pop()
            
        k -= 1

    print(ans)

