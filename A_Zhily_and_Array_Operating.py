from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # cur = a[-1]
    # ans = 1 if cur > 0 else 0
    # for i in range(n-2,-1,-1):
    #     if a[i]+cur >0:
    #         cur = a[i]+ cur
    #     else:
    #         cur = a[i]
    #     if cur >0:
    #         ans +=1
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]
    mx = pref[n]
    ans = 0
    for i in range(n - 1, -1, -1):
        if mx > pref[i]:
            ans += 1
        mx = max(mx, pref[i])
    print(ans)
    