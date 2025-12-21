from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    l,a,b = map(int, input().split())
    maxi = 0   
    n = 5000
    j = 1
    while n > 0:
        val = (a + j * b) % l
        maxi = max(maxi, val)
        j += 1
        n -= 1

    print(maxi)