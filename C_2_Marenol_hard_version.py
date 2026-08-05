from collections import defaultdict, Counter, deque
import os
import math
import sys

for _ in range(int(input())):
    n = int(input())
    a = input().strip()
    b = input().strip()
    ae, ao = deque(), deque()
    be, bo = deque(), deque()
    for i in range(n):
        if a[i] == '1':
            if i % 2 == 0:
                ae.append(i)
            else:
                ao.append(i)
        if b[i] == '1':
            if i % 2 == 0:
                be.append(i)
            else:
                bo.append(i)
    if len(ae) != len(be) or len(ao) != len(bo):
        print(-1)
        continue
    ans = 0
    while ae:
        ans += abs(ae.popleft() - be.popleft()) // 2
    while ao:
        ans += abs(ao.popleft() - bo.popleft()) // 2
    print(ans)