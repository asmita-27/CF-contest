from collections import defaultdict, Counter, deque
import os
import math
import sys


for k in range(int(input())):
    a , b = map(int , input().split())
    print(2* (max(a , b) - min(a , b)))
    l = []
    if a *b <= 0:
        for j in range(abs(min(a,b))):
            l.append(0)
            l.append(-1)
        for j in range(max(a,b)):
            l.append(0)
            l.append(1)
    elif a*b > 0:
        for i in range(b ,a+1):
            l.append(i)
        for i in range(a-1 , b , -1):
            l.append(i)
    print(*l)