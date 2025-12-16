from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())

    ele = []
    bitCnt = {}
 
    for _ in range(n):
        data = list(map(int, input().split()))
        k = data[0]
        bits = data[1:]
        ele.append(bits)
        for b in bits:
            bitCnt[b] = bitCnt.get(b, 0) + 1
 
    ans = "No"
    for bits in ele:
        uniQ = False
        for b in bits:
            if bitCnt[b] == 1:
                uniQ = True
                break
        if not uniQ:
            ans = "Yes"
            break

    print(ans)



