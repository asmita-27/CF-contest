from collections import defaultdict, Counter, deque
import os
import math
import sys

mxBIT = 30
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if all(x==0 for x in a):
        print(*range(1,n+1))
        continue
    
    cnt = [0]*(mxBIT+1)
    for i in a:
        for b in range(mxBIT):
            if(i>>b)&1:
                cnt[b] += 1
    ans  = []
    for k in range(1,n+1):
        flg = True
        for b in range(mxBIT):
            if cnt[b]%k != 0:
                flg = False
                break
        if flg:
            ans.append(k)
    print(*ans)            