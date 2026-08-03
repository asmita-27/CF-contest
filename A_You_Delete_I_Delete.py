from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    s = input()
    res = ""
    for i in range(len(s)):
        if s[i]=="0":
            cur = s[:i]+s[i+1:]
            j = cur.find("1")
            cur = cur[:j]+ cur[j+1:]
            if cur>res:
                res = cur
    print(res)