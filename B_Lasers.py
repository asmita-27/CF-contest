from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,m,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    print(n+m)
