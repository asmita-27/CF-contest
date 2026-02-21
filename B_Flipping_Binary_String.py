from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input() 
    o = [i+1 for i,ch in enumerate(s) if ch=='1']
    z = [i+1 for i,ch in enumerate(s) if ch=='0']
    cnt1 = len(o)
    cnt0 = len(z)
    if cnt1 % 2 == 0:
        print(cnt1)
        if cnt1:
            print(*o)
    elif cnt0 % 2 == 1:
        print(cnt0)
        print(*z)
    else:
        print(-1)