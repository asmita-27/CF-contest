from collections import defaultdict, Counter, deque
import os
import math
import sys

def add_divs(x, divs):
    i = 2
    while i * i <= x:
        while x % i == 0:
            divs[i] = divs.get(i, 0) + 1
            x //= i
        i += 1
    if x > 1:
        divs[x] = divs.get(x, 0) + 1

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    divs = {}
    for x in a:
        add_divs(x, divs)

    for p, cnt in divs.items():
        if cnt % n != 0:
            print("NO")
            break
    else:       
        print("YES")