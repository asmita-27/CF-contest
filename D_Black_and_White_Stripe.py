from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip() 
    w = [0] * (n + 1)
    for i in range(1, n + 1):
        w[i] = w[i - 1] + (s[i - 1] == 'W')

    result = float('inf')
    for i in range(k, n + 1):
        result = min(result, w[i] - w[i - k])

    print(result)