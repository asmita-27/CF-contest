from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    it = 0
    while True:
        flg = False
        for i in range(n):
            if a[i] > b[i]:
                a[i]-=1
                flg = True
                break
        for i in range(n):
            if a[i] < b[i]:
                a[i]+=1
                break
        it+=1
        if not flg:
            break
    print(it)