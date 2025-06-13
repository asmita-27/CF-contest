from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    pass
    n, k = map(int, input().split())
    if n==k:
        print('1'*n)
        continue
    print("1"*(k)+ '0'*(n-k))
    # elif k<1:
    #     print('0'*n)
    # elif k==1:
    #     print('1'+'0'*(n-1))
    # else:
    #     if k%2==0:
    #         print('1'+'0'*(n-k-1)+'1'*(k//2)+"0")
    #     else:
    #         print('1'+ "0"*(n//3)+ "1"*(k-1)+'0')
