from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):

    n , k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    a.sort()
    while k!=0:
        for i in a :
            if i%2==0:
                i+=1
                k-=1
            ans += i.bit_count()
    print(ans)
