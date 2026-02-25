from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,m = map(int,input().split())
    a = list(set(map(int,input().split()))) 
    b = list(map(int,input().split()))
    freq = set(a) 
    alice = 0
    for y in b:
        found = False
        d = 1
        while d*d <= y:
            if y % d == 0:
                if d in freq or (y//d) in freq:
                    found = True
                    break
            d += 1
        if found:
            alice += 1
    bob = m - alice
    print("Alice" if alice > bob else "Bob")
