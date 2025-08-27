from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,a ,b = map(int, input().split())
    if (n - b) % 2 == 1:
        print("NO")
        continue
    if a <= b:
        print("YES")
        continue
    if (a - b) % 2 == 0:
        print("YES")
    else:
        print("NO")
