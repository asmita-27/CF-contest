from collections import defaultdict, Counter, deque
import os
import math
import sys



for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    cnt = 0
    for i in range(1, n+1):
        k = a[i]
        for j in range(k, n - i + 1, k):
            x = i + j
            if a[x] == j // k:
                cnt += 1
    print(cnt)