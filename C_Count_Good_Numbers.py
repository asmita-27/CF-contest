from collections import defaultdict, Counter, deque
import os
import math
import sys
import sys
input = sys.stdin.readline
 
bad_primes = [2, 3, 5, 7]
m = len(bad_primes)

def cntUpto(n):
    bad = 0 
    for mask in range(1, 1 << m):
        prod = 1
        bits = 0
        for i in range(m):
            if mask & (1 << i):
                prod *= bad_primes[i]
                bits += 1
        term = n // prod
        if bits % 2 == 1:
            bad += term
        else:
            bad -= term 
    return n - bad

def cntGood(l, r): 
    return cntUpto(r) - cntUpto(l-1)
 

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(cntGood(l, r))

