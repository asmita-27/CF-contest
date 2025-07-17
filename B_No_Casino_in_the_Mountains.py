from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    zro = sum(1 for i in range(k) if a[i] == 0)
    hk = 0
    i = 0
    while i <= n - k:
        if zro == k:
            hk += 1
            i += k + 1
            if i <= n - k:
                zro = sum(1 for j in range(i, i + k) if a[j] == 0)
        else:
            if i + k < n:
                if a[i] == 0:
                    zro -= 1
                if a[i + k] == 0:
                    zro += 1
            i += 1
    print(hk)