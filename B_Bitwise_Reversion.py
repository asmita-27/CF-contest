from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    x, y, z = map(int, input().split())
    mask = ((x & y) | (y & z) | (z & x)) & ~(x & y & z) 
    print("YES" if mask == 0 else "NO")