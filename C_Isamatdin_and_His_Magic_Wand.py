from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    even = False
    odd = False
    for i in a:
        if i%2==0:
            even = True
        else:
            odd = True
    if odd and even :
        a.sort()
    print(*a)
    