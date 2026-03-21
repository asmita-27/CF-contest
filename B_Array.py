from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        x,y= 0,0
        for j in range(i+1,n):
            if a[j]<a[i]:
                x+=1
            elif a[j]>a[i]:
                y+=1
        ans.append(max(x,y))
    print(*ans)