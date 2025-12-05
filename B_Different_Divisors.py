from collections import defaultdict, Counter, deque
import os
import math
import sys


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for _ in range(int(input())):
    x = int(input())
    p = []
    i = x + 1
    while True:
        if is_prime(i):
            p.append(i)
            break
        i += 1 
    i = p[0] + x
    while True:
        if is_prime(i):
            p.append(i)
            break
        i += 1
    print(min(p[0] * p[1], p[0] ** 3))
