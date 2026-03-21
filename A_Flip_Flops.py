from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,c,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for x in a:
        if x > c:
            break
        use = min(k, c - x)
        c += x + use
        k -= use
    print(c)