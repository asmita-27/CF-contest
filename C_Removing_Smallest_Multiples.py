from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    
    # print(rem)

    rem = []
    for i in range(n):
        if s[i] == '0':
            rem.append(i + 1)
    cost = [0] * (n + 2) 
    for i in range(n, 0, -1):
        for j in range(i, n + 1, i):
            if s[j - 1] == '1':
                break
            cost[j] = i  
    ans = 0
    for i in rem:
        ans += cost[i]

    print(ans)