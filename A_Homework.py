from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = input()
    
    m = int(input())
    b = input()
    c = input()
    s = a
    for chB, chC in zip(b, c):
        if chC == 'V':
            s = chB + s
        else:
            s += chB
    print(s)