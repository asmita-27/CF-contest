from collections import defaultdict, Counter, deque
import os
import math
import sys
n = int(input())
a = list(map(lambda x: int(x) - 1, input().split()))
b = list(map(lambda x: int(x) - 1, input().split()))

pos = [0] * n
for i in range(n):
    pos[b[i]] = i

c = [0] * n
for i in range(n):
    c[i] = pos[a[i]]

mx = -1
ans = 0
for i in range(n):
    if c[i] > mx:
        mx = c[i]
    else:
        ans += 1

print(ans)
