from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, k = map(int, input().split())

    if k > n:
        print(-1)
        continue
    time = 0
    x = n
    while x > k:
        a = x // 2
        b = x - a
        if a >= k:
            x = a
        elif b >= k:
            x = b
        else:
            time = -1
            break

        time += 1

    print(time)