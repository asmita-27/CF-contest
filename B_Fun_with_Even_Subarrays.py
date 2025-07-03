from collections import defaultdict, Counter, deque
import os
import math
import sys

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = a[::-1]  
    ans = 0
    x = 1
    while x < n: 
        if x < n and b[x] == b[0]:
            x += 1
            continue
        ans += 1
        x *= 2

    print(ans)
