from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # ans = sum(1 for i in range(n)if a[i]== i + 1)
    # print(ans)
    res = 1
    x = defaultdict(int)
    for i in range(n):
        
        a[i] -= i
        res += x[a[i]]
        x[a[i]] += 1
    print(res-1)
