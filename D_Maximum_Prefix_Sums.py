from collections import defaultdict, Counter, deque
import os
import math
import sys

NEG = -10**15
 

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = a[:]

    pref = 0
    mx = -10**18

    ok = True

    for i in range(n):

        if i > 0 and c[i] < c[i - 1]:
            ok = False
            break

        if s[i] == '1':

            pref += ans[i]
            mx = max(mx, pref)

            if mx != c[i]:
                ok = False
                break

        else:

            if c[i] > mx: 
                ans[i] = c[i] - pref
                pref = c[i]
                mx = c[i]

            else: 
                ans[i] = NEG
                pref += ans[i]

    print("Yes" if ok else "No")

    if ok:
        print(*ans)