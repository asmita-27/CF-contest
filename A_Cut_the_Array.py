from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    flg= False
    for l in range(1, n-1):         
        for r in range(l+1, n):     
            s1 = sum(a[:l]) % 3
            s2 = sum(a[l:r]) % 3
            s3 = sum(a[r:]) % 3
            if s1 == s2 == s3 or {s1, s2, s3} == {0, 1, 2}:
                print(l, r)
                flg= True
                break
        if flg:
            break
    if not flg:
        print(0, 0)