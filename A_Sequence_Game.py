from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n =  int(input())
    a = list(map(int, input().split()))
    x = int(input())
    
    if max(a)<x or min(a)>x:
        print("NO")
    else:
        print("YES")