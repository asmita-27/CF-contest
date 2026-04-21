from collections import defaultdict, Counter, deque
import os
import math
import sys


def sol(s, tar):
    n = len(s)
    i = 0
    while i < n and s[i] == tar[i]:
        i += 1
    while i < n and s[i] != tar[i]:
        i += 1
    while i < n:
        if s[i] != tar[i]:
            return False
        i += 1
    return True
 
for _ in range(int(input())):
    s = input().strip()
    n = len(s)
    t1 = ''.join('a' if i % 2 == 0 else 'b' for i in range(n))
    t2 = ''.join('b' if i % 2 == 0 else 'a' for i in range(n))
    if sol(s, t1) or sol(s, t2):
        print("YES")
    else:
        print("NO")