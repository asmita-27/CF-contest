from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    while True:
        sz = len(s)
        if sz in s:
            print(sz)
            break
        else:
            s.add(sz)

