from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, x1, x2, k = map(int, input().split())

    if n <= 3:
        print(1)
    else:
        diff = abs(x1 - x2)
        d = min(diff, n - diff)
        print(d + k)