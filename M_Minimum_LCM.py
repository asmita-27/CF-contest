from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a =1 
    i=2 
    while i*i<=n:
        if n%i==0:
            a= n//i
            break
        i+=1
    print(a, n-a)