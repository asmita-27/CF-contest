from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    # n = int(input())
    # a = list(map(int, input().split()))
    # mx = 100*n
    # dp = [False]*(mx+1)
    # dp[0] = True
    # for i in a:
    #     sc = 100//i
    #     ndp = [False]*(mx+1)
    #     for j in range(mx+1):
    #         if not dp[j]:
    #             continue
    #         for k in range(i+1):
    #             nj = j+k*sc
    #             if nj<=mx:
    #                 ndp[nj] = True
    #     dp = ndp
    # ok = all(dp[i] for i in range(mx + 1))
    # print("Yes" if ok else "No")
    n = int(input())
    ans = False
    for _ in range(n):
        x = int(input()) if n == 1 else None
    a = list(map(int, input().split()))
    for x in a:
        if x == 100:
            ans = True
    print("Yes" if ans else "No")