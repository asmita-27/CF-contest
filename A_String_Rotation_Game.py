from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input() 
    c = 0
    flg = False
    for i in range(n):
        if s[i] != s[(i+1) % n]:
            c += 1
        else:
            flg = True
    if c == 0:
        print(1)
    elif flg:
        print(c + 1)
    else:
        print(c)