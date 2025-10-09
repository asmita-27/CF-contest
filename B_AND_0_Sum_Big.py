from collections import defaultdict, Counter, deque
import os
import math
import sys
MOD = 10**9 + 7

for _ in range(int(input())): 
    n, k = map(int, input().split())
    ans = 1
    for _ in range(k):
        ans = (ans * n) % MOD
    print(ans)