from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, c = input().split()
    n = int(n)
    s = input().strip()
 
    if all(ch == c for ch in s):
        print(0)
        continue 
    flg = False
    for x in range(1, n+1):
        ok = True
        for i in range(x, n+1, x):  
            if s[i-1] != c: 
                ok = False
                break
        if ok:
            print(1)
            print(x)
            flg = True
            break
    if not flg:
            print(2)
            print(n, n-1)