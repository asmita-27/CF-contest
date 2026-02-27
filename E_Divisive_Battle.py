from collections import defaultdict, Counter, deque
import os
import math
import sys

MX = 10**6
spf = list(range(MX+1))
for i in range(2, int(MX**0.5)+1):
    if spf[i] == i:
        for j in range(i*i, MX+1, i):
            if spf[j] == j:
                spf[j] = i

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    def isPrPow(x):
        p = spf[x]
        while x % p == 0:
            x //= p
        return x == 1
    res = "Bob"
    for i in range(n-1):
        if a[i] > a[i+1]:
            if not isPrPow(a[i]):
                res = "Alice"
            break
    print(res)