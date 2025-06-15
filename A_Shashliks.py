from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    k,a,b,x,y = map(int, input().split())
    ans = 0
    
    
    if x<y:
        if k>=a:
            k1 = (k-a)//x+1
            ans += k1
            k -= k1*x
        if k>=b:
            k2 = (k-b)//y+1
            ans += k2
            k -= k2*y
    else:
        if k>=b:
            k1 = (k-b)//y+1
            ans += k1
            k -= k1*y
        if k>=a:
            k2 = (k-a)//x+1
            ans += k2
            k -= k2*x
    print(ans)
            