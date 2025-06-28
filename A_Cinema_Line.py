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
    if a[i] == 25:
        cnt += 25
    elif a[i] == 50  :
        if cnt < 25:
            flg = 1
            continue
        cnt -= 25
        cnt += 50
    elif a[i] == 100:
        if cnt < 75:
            flg = 1
            continue
        if cnt >= 75:
            cnt -= 75
            cnt += 100
        else:
            cnt -= 25

if flg:
    print("NO")
else:
    print("YES")
    



