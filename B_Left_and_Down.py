from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    a, b, k = map(int, input().split())
    g = math.gcd(a, b)
    mn = max(a// k, b // k)
    if g> mn:
        print(1)
    else:
        print(2)