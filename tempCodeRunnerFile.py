from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = Counter(a)
    b = set()
    
    for num in a:
        b.add(num)
        b.add(num + 1)

    last = 0
    res = 0

    for x in sorted(b):
        c = cnt.get(x, 0)
        res += max(0, c - last)
        last = c

    print(res)