from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l,r  = 0, n - 1
    sumL = a[0]
    sumR = a[n-1]
    ans = 0
    while l < r:
        if sumL == sumR:
            ans = max(ans, l + 1 + n - r)

        if sumL <= sumR:
            l+=1
            sumL+=a[l]

        elif sumR < sumL:
            r-=1
            sumR+=a[r]

    print(ans)