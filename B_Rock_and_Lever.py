from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(29,-1,-1):
        cnt =0
        lw = 1<<i
        hg = 1<<(i+1)
        for j in a:
            if lw <= j < hg:
                cnt+=1
        ans +=  cnt*(cnt-1)//2
    print(ans)