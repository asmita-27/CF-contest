from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,l,r,k = map(int, input().split())
    
    if n==1:
        print(l)
        continue
    if n%2==1:
        print(l)
    
    else:
        if n==2:
            print(-1)

        else:
            v = l.bit_length()
            x = 2**v
            if x not in range(l, r+1):
                print(-1)
            else:
                if k<=n-2:
                    print(l)
                else:
                    print(x)
    
 
