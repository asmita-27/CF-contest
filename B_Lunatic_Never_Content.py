from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    g = 0
    for i in range(n):
        g = math.gcd(g, abs(a[i]-a[n-i-1]))
        
    print(g)

