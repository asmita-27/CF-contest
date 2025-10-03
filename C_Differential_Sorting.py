from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[n-2] > a[n-1]:
        print(-1)
    else:
        if a[n-1] < 0:
            if all(a[i] <= a[i+1] for i in range(n-1)):
                print(0)
            else:
                print(-1)
        else:
            print(n-2)
            for i in range(1, n-1):  
                print(i, n-1, n)