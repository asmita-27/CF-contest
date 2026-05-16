from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, x1, x2, k = map(int, input().split())
    d = abs(x1 - x2)
    d = min(d, n - d)
    print(d + k)