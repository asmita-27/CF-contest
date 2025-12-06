from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,k = map(int, input().split())
    s = input()
    res = 0
    for i in range(n):
        if s[i]=='0':
            flg = True
            for j in range(max(0,i-k),i):
                if s[j]=='1':
                    flg = False
                    break
            if flg:
                res +=1
    print(res)