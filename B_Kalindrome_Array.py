from collections import defaultdict, Counter, deque
import os
import math
import sys

def isPal(s):
    return s == s[::-1]

def isKal(x,a):
    b = [i for i in a if i!=x]
    return isPal(b)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    flg = True
    for i in range(n):
        if a[i]!= a[n-1-i]:
            flg = False
            if isKal(a[i], a) or isKal(a[n-1-i], a):
                flg = True
            break
    if flg:
        print("YES")
    else:
        print("NO")