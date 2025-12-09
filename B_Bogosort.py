from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    print(*sorted(map(int, input().split()))[::-1])

    