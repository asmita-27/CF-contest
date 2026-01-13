from collections import defaultdict, Counter, deque
import os
import math
import sys

def main():
    n, k = map(int, input().split())

    if n==k:
        print(0)
    cnt =0
    flg = False
    if n&1 :
        flg = True
    while n >= k:
        if n & 1:
            flg = True

        n //= 2
        cnt += 1

        if n == k:
            print(cnt)
            return
        if flg:
            if n + 1 == k:
                print(cnt)
                return
    print(-1)

for _ in range(int(input())):
    main()