from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = sorted([int(_) for _ in input().split()])
    print(max(a[0], a[1]-a[0]))