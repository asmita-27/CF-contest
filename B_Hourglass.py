from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    s, k, m = map(int, input().split())
    r = m % k

    if s <= k:
        print(max(0, s - r))
    else:
        print(max(0, k - r))