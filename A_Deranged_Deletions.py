from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    cnt = Counter(b)

    if any (i >= n//2 for i in cnt.values()):
        print("NO")
        continue
        