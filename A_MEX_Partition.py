from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = Counter(a)
    ans = 0 
    for i in range(102):
        if cnt[i] == 0:
            ans = i
            break
    print(ans)