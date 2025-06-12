from collections import defaultdict, Counter, deque
import os
import math
import sys

n = int(input())
s =  list(map(int, input().split()))
cnt =  0
stk = []
s.sort(reverse=True)
for i in s :
    if i== 4:
        cnt+=1 
    else:
        while stk and i + stk[-1] <= 4:
            cnt+=1
            stk.pop()
        if i != 4:
            stk.append(i)
print(cnt)
    
