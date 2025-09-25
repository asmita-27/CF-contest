from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = float('-inf')
    for i in range(0,n,2):
        ans = max(ans, a[i+1]-a[i])
    print(ans)