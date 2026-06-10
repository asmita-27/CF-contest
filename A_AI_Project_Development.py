from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,x,y,z = map(int, input().split())
    nAI = (n + (x + y) - 1) // (x + y)
    mx = (n + x - 1) // x

    if mx <= z:
        ai = mx
    else:
        rem = n - z * x
        ai = z + (rem + (x + 10 * y) - 1) // (x + 10 * y)

    print(min(nAI, ai))