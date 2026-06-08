from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())

    if n == 10:
        print(-1)
        continue
    r = n % 12
    if r <= 9:
        a = r
    elif r == 10:
        a = 22
    else:
        a = 11
    print(a, n - a)