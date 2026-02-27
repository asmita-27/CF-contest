from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    flg = True
    for i in range(n-1):
        if a[i] > a[i+1]:
            flg = False
            break
    if flg:
        print(n)
    else:
        print(1)