from collections import defaultdict, Counter, deque
import os
import math
import sys

 
n = int(input())
cnt1, cnt2  = 0,0
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        cnt1 += 1
    elif a < b:
        cnt2 += 1
if cnt1 and cnt2:
    print("Happy Alex")
else:
    print("Poor Alex")
