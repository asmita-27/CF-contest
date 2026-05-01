from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input()
    
    cnt = 0
    for i in range(n):
        cnt += s[i]=="("

    if cnt*2==n:
        print("YES")
    else:
        print("NO")