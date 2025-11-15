from collections import defaultdict, Counter, deque
import os
import math
import sys



for _ in range(int(input())):
    pass
    n = int(input())
    s = input().strip()
    Sset = set()
    for i in range(n):
        ss = ''
        for j in range(5):
            if i+j < n:
                ss += s[i+j]
                Sset.add(ss)
    for length in range(1, 6):
        t = ["a"] * length
        while True:
            ts = "".join(t)
            if ts not in Sset:
                print(ts)
                break

            idx = length - 1
            while idx >= 0 and t[idx] == 'z':
                t[idx] = 'a'
                idx -= 1
            if idx < 0:
                break
            t[idx] = chr(ord(t[idx]) + 1)

        else:
            continue
        break
    