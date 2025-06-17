from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    
    n = int(input()) 
    str = [input() for _ in range(n)]
     
    strSet = set(str)
     
    res = []
     
    for s in str:
        found = False 
        for i in range(1, len(s)):   
            pre = s[:i]
            suf = s[i:] 
            if pre in strSet and suf in strSet:
                found = True
                res.append("1")
                break
        if not found:
            res.append("0")
     
    print("".join(res))

