from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if a[0] == -1:
        a[0] = a[n-1]
    if a[n-1] == -1:
        a[n-1] = a[0]
    for i in range(n):
        if a[i] == -1:
            a[i] = 0
    print(abs(a[n-1]-a[0]))
    print(*a)