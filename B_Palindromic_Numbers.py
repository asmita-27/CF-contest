from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):

    n = int(input())
    s = input()
    
    if s[0] == '9':
        num = '1'*(n+1)
        ans =str(int(num) - int(s))
    else:
        num = '9'*n
        ans = ''.join(str(9-int(x))for x in s)

    print(ans)
 