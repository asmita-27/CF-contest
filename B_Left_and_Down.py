from collections import defaultdict, Counter, deque
import os
import sys
import math

for _ in range(int(input())):
    a, b, k = map(int, input().split())
    g = math.gcd(a, b)
    mn = max((a+k-1)// k, (b+k-1) // k)
    if g>= mn:
        print(1)
    else:
        print(2)