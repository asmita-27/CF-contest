from collections import defaultdict, Counter, deque
import os
import math
import sys

def main():
    n, k = map(int, input().split())

    if n == k:
        print(0)
        return

    s = {n}
    m = 0

    while s:
        m += 1
        nxt = set()
        ok = False
        for x in s:
            if x < 2:
                continue
            a = x // 2
            b = (x + 1) // 2
            if a == k or b == k:
                ok = True
                break
            if a > k:
                nxt.add(a)
            if b > k:
                nxt.add(b)
        if ok:
            print(m)
            return
        if not nxt:
            break
        s = nxt
    print(-1)
    
    
for _ in range(int(input())):
    main()