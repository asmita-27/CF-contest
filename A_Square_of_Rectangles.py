from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    l1,b1,l2,b2,l3,b3 = map(int, input().split())

    if l1==l2==l3 and b1+b2+b3 == l1:
        print("YES")
    elif b1==b2==b3 and l1+l2+l3 == b1:
        print("YES")
    elif l2 + l3 == l1 and b2 == b3 and b1 + b2 == l1:
        print("YES")
    elif  b2 + b3 == b1 and l2 == l3 and l1 + l2 == b1:
        print("YES")
    else:
        print("NO")