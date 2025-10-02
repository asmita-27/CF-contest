from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[n-2] > a[n-1]:
        print(-1)
    else:
        print(n-2)
        for i in range(1, n-1):
            print(i, i+1, n)
