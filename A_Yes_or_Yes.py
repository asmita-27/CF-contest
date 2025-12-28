from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    s = input().strip()
    if s.count('Y') >1:
        print("NO")
    else:
        print("YES")