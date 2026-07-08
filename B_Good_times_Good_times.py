from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    x = int(input())
    y = 1
    while x > 0:
        y *= 10
        x //= 10
    print(y + 1)
