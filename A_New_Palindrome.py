from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    s = input().strip()
    s = s[:len(s)//2] 
    unQ = []
    for i in s:
        if not unQ or unQ[-1] != i:
            unQ.append(i)
    m = len(unQ)
    if m==1:
        print("NO")
    else:   
        print("YES")