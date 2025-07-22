from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    a, b, k = map(int, input().split())

    if max(a, b) <= k:
        print(1)
    else:
        print(2)
