from collections import defaultdict, Counter, deque
import os
import math
import sys
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pos = {}
for i in range(n):
    pos[b[i]] = i

mx = -1
ans = 0
for i in range(n):
    curr = pos[a[i]]
    if curr > mx:
        mx = curr
    else:
        ans += 1

print(ans)
