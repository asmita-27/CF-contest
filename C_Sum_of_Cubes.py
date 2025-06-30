from collections import defaultdict, Counter, deque
import os
import math
import sys

N = 10**12
 
cubes = set()
i = 1
while i**3 <= N:
    cubes.add(i**3)
    i += 1

def solve(x):
    i = 1
    while i**3 <= x:
        if (x - i**3) in cubes:
            return "YES"
        i += 1
    return "NO"
 
t = int(input())
for _ in range(t):
    x = int(input())
    print(solve(x))
