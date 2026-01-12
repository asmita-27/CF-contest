from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    s, k, m = map(int, input().split())
    lastFlip = (m // k) * k 
    after = min(s, k)
 
    elapsed = m - lastFlip
 
    rem = after - elapsed

    if rem < 0:
        rem = 0

    print(rem)