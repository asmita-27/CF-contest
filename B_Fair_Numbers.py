from collections import defaultdict, Counter, deque
import os
import math
import sys

def is_fair(x):
    for ch in str(x):
        d = ord(ch) - 48
        if d != 0 and x % d != 0:
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    x = n
    while not is_fair(x):
        x += 1
    print(x)
