from collections import defaultdict, Counter, deque
import os
import math
import sys

for _ in range(int(input())):
    s = input().strip()
    digits = list(map(int, s))
    n = len(digits)
    
    if sum(digits) <= 9:
        print(0)
        continue
    fst = digits[0]
    rest = sorted(digits[1:])
    def chose(arr, cap):
        s = cnt = 0
        for d in arr:
            if s + d > cap: break
            s += d
            cnt += 1
        return cnt
    k1 = 0
    if fst <= 9:
        k1 = 1 + chose(rest, 9 - fst)
    k2 = chose(rest, 8)
    
    print(n - max(k1, k2))