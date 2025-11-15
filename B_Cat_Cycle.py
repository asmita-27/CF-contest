from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,k = map(int,input().split())
    
    k -=1
    fl = n//2
    res = (k+(n%2)*(k//fl))%n
    print(res+1)