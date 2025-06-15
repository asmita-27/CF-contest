from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    k,a,b,x,y = map(int, input().split())
    ans = 0
    minn, rem , other = 0, 0, 0
    
    if x>= y:
        minn = y
        rem = k - b
        other = b
    else:
        minn = x
        rem = k - a
        other = a
    if rem>= 0:
        ans = rem//minn +1
        k -= (ans-1)*minn
        k -= minn
    else:
        ans = 0
    if other ==a:
        if k >= b:
            rem2 = k - b
            ans += rem2 // y + 1
    else:
        if k >= a:
            rem2 = k - a
            ans += rem2 // x + 1
                
    print(ans)