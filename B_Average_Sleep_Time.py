from collections import defaultdict, Counter, deque
import os
import math
import sys

   
n, k = map(int, input().split())
a = list(map(int, input().split()))
pref = [0]*(n+1)
for i in range(n):
    pref[i+1] = pref[i] + a[i]
tot = 0.0
wks = n - k + 1
for i in range(wks):
    tot += pref[i+k] - pref[i]
print(f"{tot / wks:.10f}")
