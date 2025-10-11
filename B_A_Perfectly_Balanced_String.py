from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    s = input()
    n = len(s)
    k = len(set(s))
    flg =  True
    for i in range(k,n):
        if s[i] != s[i-k]:
            flg = False
            break
    if flg:
        print("YES")    
    else:
        print("NO")
            

