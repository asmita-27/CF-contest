from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    x = [False]*(n+1)
    curr =1
    x[curr] = True
    for i in range(n):
        if s[curr-1] == 'L':
            curr -= 1
        else:
            curr += 1
        x[curr] = True
    ans = 0
    for i in range(n+1):
        if  x[i]:
            ans += 1
    print(ans)