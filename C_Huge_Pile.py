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
        half = x // 2

        if k > half:
            x = x - half     
        else:
            x = half   
        time += 1
    if x == k:
        print(time)
    else:
        print(-1)