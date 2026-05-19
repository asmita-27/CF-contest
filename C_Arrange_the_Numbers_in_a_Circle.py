from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))

    ans = 0

    for x in c:
        ans = max(ans, x)

    for i in range(n):
        for j in range(i + 1, n):
            x = c[i]
            y = c[j]

            ans = max(ans, min(x + y, 3 * x))

    if ans < 3:
        print(0)
    else:
        print(ans)