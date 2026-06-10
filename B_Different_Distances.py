from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    b1 = list(range(1, n + 1))
    b2 = list(range(n, 0, -1))
    b3 = list(range(1, n + 1))
    b4 = list(range(1, n + 1))
    if n % 2:
        m = (n + 1) // 2
        i = b2.index(m)
        b2[i], b2[i + 1] = b2[i + 1], b2[i]
    ans = b1 + b2 + b3 + b4
    print(*ans)