from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    x = input()
    digits = set(x)
    for y in range(0, 10):
        if str(y) in digits:
            print(y)
            break