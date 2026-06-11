from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    y = 0
    ans = []
    for i in reversed(range(n)):
        x = -a[i] if y else a[i]
        if x > 0:
            ans.append(i)
            y ^= 1
    print(len(ans))
    print(*(i + 1 for i in ans))