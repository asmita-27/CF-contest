from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    s = input()
    cnt = 0
    for i in range(1,n):
        if s[i]!= s[i-1]:
            cnt +=1 
    
    if cnt ==1:
        print(2)
    else:
        print(1)