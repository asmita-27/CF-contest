from collections import defaultdict, Counter, deque
import os
import math
import sys


 
for _ in range(int(input())):
    pass
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    ans = 10**18
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        ans = min(ans, (i + n - j) * a[i])
        i = j
    print(ans)