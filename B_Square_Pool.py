from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, s = map(int, input().split())
    ans = 0

    for _ in range(n):
        a,b,c,d = map(int, input().split())
        if a==b and c==d:
            ans +=1
        elif c+d == s :
            if (a==1 and b==-1) or (a==-1 and b==1):
                ans += 1
    print(ans)
                