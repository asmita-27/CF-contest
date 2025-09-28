
from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pos = {v: i + 1 for i, v in enumerate(a)}
    ans = 0
    for i, x in enumerate(a, 1):
        for y in range(1, 2 * n // x + 1):
            j = pos.get(y, 0)
            if j and i < j and x * y == i + j:
                ans += 1
    print(ans)