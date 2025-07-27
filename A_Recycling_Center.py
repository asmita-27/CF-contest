from collections import defaultdict, Counter, deque
import os
import math
import sys
def floor_log2(x):
    if x <= 0:
        return -1
    return x.bit_length() - 1

for _ in range(int(input())):
    n,c = map(int, input().split())
    a = list(map(int, input().split()))
    y = []
    for w in a:
        if w > c:
            y.append(-1)
        else:
            x = c // w
            y.append(floor_log2(x))
    y.sort()
    free = 0
    for d in y:
        if d >= free:
            free += 1
    print( n - free)