from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    sm = sum(a)
    if (n*k)%2==0:
        print("YES")
    else:
        print("YES" if sm % 2 else "NO")