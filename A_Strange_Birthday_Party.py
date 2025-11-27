from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, m = map(int, input().split())
    k = list(map(int, input().split()))
    c = list(map(int, input().split()))
    k.sort(reverse=True)
    ptr = 0
    tot =0
    for i in k:
        if ptr < m and c[ptr] <c[i-1]:
            tot += c[ptr]
            ptr += 1
        else:
            tot += c[i-1]
    print(tot)
