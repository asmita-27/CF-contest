from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    g = [a[0], a[1]]  
    for i in range(n):
        g[i % 2] = math.gcd(g[i % 2], a[i])
    
    good = [1,1]
    for i in range(n):
        if a[i] % g[(i % 2) ^ 1] == 0:
            good[i % 2] = False
    
    ans = 0
    for i in range(2):
        if good[i]:
            ans = max(ans, g[i ^ 1])
    
    print(ans)
