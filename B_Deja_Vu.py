from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    used = [False] * 31   
    for x in queries:
        if not used[x]:
            add_val = 1 << (x - 1)
            div_val = 1 << x
            for i in range(n):
                if a[i] % div_val == 0:
                    a[i] += add_val
            used[x] = True 
            for j in range(x + 1, 31):
                used[j] = True  
    print(*a)