from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = input().strip()
    b = input().strip()
    x = y = 0
    for i in range(1, n, 2):   
        if a[i] == '1':
            x += 1
        if b[i] == '1':
            y += 1
    if a.count('1') == b.count('1') and x == y:
        print("YES")
    else:
        print("NO")
    