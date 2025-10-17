from collections import defaultdict, Counter, deque
import os
import math
import sys

 
for _ in range(int):
    a, b = map(int, input().split())

    if a == b:
        print(0)
        continue

    m = a.bit_length() - 1
    all_mask = (1 << (m + 1)) - 1

    if b > all_mask:
        print(-1)
        continue

    c = a ^ b
    if c <= a:
        print(1)
        print(c)
        continue

    x1 = all_mask ^ a
    x2 = all_mask ^ b
    print(2)
    print(x1, x2)
