from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    
    n = int(input())
    s = input().strip()
    cnt_0 = 0

    for ch in s:
        if ch == '0':
            cnt_0 += 1

    if cnt_0 == 1:
        print("BOB")
        continue

    if cnt_0 % 2 == 1:
        print("ALICE")
    else:
        print("BOB")