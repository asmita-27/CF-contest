from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,k = map(int, input().split())
    s = input()
    res = 0
    lst = float('-inf')    
    for i in range(n):
        if s[i]=="1" and i-lst>=k:
            res+=1
        if s[i]=="1":
            lst = i
    print(res)
