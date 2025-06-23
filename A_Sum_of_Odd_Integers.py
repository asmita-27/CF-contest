from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    n,k = map(int, input().split())
    
    flg = 0
    if n%2==0 and k%2==1:
        flg = 1
    if k*k >n:
        flg = 1
    
    if flg :
        print("NO")
    else:
        print("YES")
    
    