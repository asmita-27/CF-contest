from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    if n%2==0:
        print(n//2 , n//2)
        continue
    d = n
    limit = int(math.isqrt(n))
    for x in range(3, limit + 1, 2):
        if n % x == 0:
            d = x
            break
    if d == n:
        print(1, n - 1)
    else:
        a = n // d
        b = n - a
        print(a, b)