from collections import defaultdict, Counter, deque
import os
import math
import sys

n = int(input())
a = list(map(int, input().split()))

flg  = 0
cnt = a[0]
for i in range(1, n):
    if a[0]!=25:
        flg = 1
        continue

if flg:
    print("NO")
else:
    print("YES")
    



