from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    r0, x,d,n = map(int, input().split())
    s = input().strip()
    
    mn = r0
    ans = 0
    for i in range(n):
        if s[i]=="2":
            if r0 <x:
                ans += 1
            elif mn <x:
                ans +=1 
        else:
            ans += 1
            mn = mn -d
    print(ans )