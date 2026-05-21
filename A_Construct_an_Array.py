from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    arr = [str(i) for i in range(n + 1, 2 * n + 1)]
    print(" ".join(arr))