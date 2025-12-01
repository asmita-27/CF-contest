from collections import defaultdict, Counter, deque
import os
import math
import sys



MAXN = 300005
numbers = [0] * MAXN
 
for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    mn = arr[0]
    mx = arr[0]
    res = 0

    for i in range(1, n):
        if arr[i] > mx:
            mx = arr[i]
        if arr[i] < mn:
            mn = arr[i]
        if mx - mn > 2 * x:
            res += 1
            mn = mx = arr[i]

    print(res)