from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a = [x % k if x % k != 0 else k for x in a]

    ord = list(range(n))

    ord.sort(key=lambda i: a[i], reverse=True)

    print(*[i + 1 for i in ord])