from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    n = int(input())
    s = input()
    flg = 0
    mp = Counter(s)
    for i in range(1,n-1):
        if mp[s[i]] >1:
            flg = 1
            break
    if flg :
        print("Yes")
    else:
        print("No")

