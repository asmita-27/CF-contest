from collections import defaultdict, Counter, deque
import os
import math
import sys

mx = 20
w = [0] * mx
c = [0] * mx

for x in range(mx):
    w[x] = 3 ** x
    c[x] = 3 ** (x + 1) + (0 if x == 0 else x * (3 ** (x - 1)))
for _ in range(int(input())): 
    n = int(input())
    ans = 0
    x = 0

    while n > 0:
        d = n % 3
        ans += d * c[x]
        n //= 3
        x += 1

    print(ans)
