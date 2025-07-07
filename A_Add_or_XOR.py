from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    a,b,x,y = map(int, input().split())
    
    if a-b >1:
        print(-1)
        continue
    elif a-b==1:
        if a %2==0:
            print(-1)
        else:
            print(y)
    else:
        c = 0
        while a!=b:
            if a % 2 == 1:
                c+=x
                a+=1
            else:
                c+= min(x,y)
                a+=1
        print(c)

