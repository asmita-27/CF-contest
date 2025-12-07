from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,l,r = map(int,input().split())
    
    pref = [i for i in range(n+1)]
    pref[r]= pref[l-1]
    res= []
    for i in range(1,n+1):
        res.append(pref[i]^ pref[i-1])

    print(*res)