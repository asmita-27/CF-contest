from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    tot = 0
    cntO = 0

    for x in a:
        if x > 0:
            cntO += 1
        tot += x

    sum2 = tot - cntO
    sub = n - 1 - sum2

    print(cntO - max(0, sub))