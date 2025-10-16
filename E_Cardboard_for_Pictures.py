from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,c = map(int, input().split())
    a = list(map(int, input().split()))
    l,r = 1 , int(1e9)
    while l<=r:
        mid = (l + r) // 2
        total = 0
        for ai in a:
            total += (ai + 2 * mid) * (ai + 2 * mid)
            if total > c:   
                break

        if total == c:
            print(mid)
            break
        elif total > c:
            r = mid - 1
        else:
            l = mid + 1
    

