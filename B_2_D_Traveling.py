from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, k, s, t = map(int, input().split())
    x = [0] * (n + 1)
    y = [0] * (n + 1)
    
    for i in range(1, n + 1):
        xi, yi = map(int, input().split())
        x[i] = xi
        y[i] = yi
 
    ans = abs(x[s] - x[t]) + abs(y[s] - y[t])

    mins = float('inf')
    mint = float('inf')
 
    for i in range(1, k + 1):
        mins = min(mins, abs(x[s] - x[i]) + abs(y[s] - y[i]))
        mint = min(mint, abs(x[t] - x[i]) + abs(y[t] - y[i]))

    ans = min(ans, mins + mint)
    print(ans)

