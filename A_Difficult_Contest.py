from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    s = input()
    cntF = s.count('F')
    cntN = s.count('N')
    cntT = s.count('T')
    
    res = []
     
    for c in s:
        if c not in 'FNT':
            res.append(c)
    
    output = 'T' * cntT + 'F' * cntF + 'N' * cntN + ''.join(sorted(res))
    print(output)