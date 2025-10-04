from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,  rK, cK, rD, cD = map(int, input().split())
    ans = 0
    if rK<rD:
        ans = max(ans , rD)
    elif rK>rD:
        ans = max(ans , n - rD )
    if cK<cD:
        ans = max(ans , cD)
    elif cK>cD:
        ans = max(ans , n - cD )
    print(ans)
        