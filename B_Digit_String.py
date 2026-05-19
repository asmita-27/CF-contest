from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    s = input()
    n = len(s)
    pre = [0]*(n+1)
    suf = [0]*(n+1)
    for i in range(n):
        pre[i+1] = pre[i]+(s[i]=='2')
    for i in range(n-1,-1,-1):
        suf[i] = suf[i+1]+(s[i]=="1"or s[i]=="3")
    ans = 0
    for i in range(n+1):
        ans = max(ans, pre[i]+suf[i])
    print(n-ans)