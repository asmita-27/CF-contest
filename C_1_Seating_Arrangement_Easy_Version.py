from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,x,s = map(int,input().split())
    a = input().strip()
    # new = 0
    # free = 0
    # ans = 0
    # for ch in a:
    #     if ch == 'I':
    #         if new < x:
    #             new += 1
    #             free += s - 1
    #             ans += 1
    #     elif ch == 'E':
    #         if free:
    #             free -= 1
    #             ans += 1
    #     else: 
    #         if free:
    #             free -= 1
    #             ans += 1
    #         elif new < x:
    #             new += 1
    #             free += s - 1
    #             ans += 1
    # print(ans)
    dp = [-1]*(x+1)
    dp[0] = 0 
    for i in a:
        new = dp[:]
        for j in range(x+1):
            free = dp[j]
            if free==-1:
                continue 
            if i !="E" and j < x:
                new[j+1] = max(new[j+1], free)
            if i !="I" and free < j*(s-1):
                new[j] = max(new[j], free+1)
        dp = new
    res = 0
    for i in range(x+1):
        if dp[i]!=-1:
            res = max(res, i+dp[i])
    print(res)
