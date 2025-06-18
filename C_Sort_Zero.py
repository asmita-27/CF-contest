from collections import defaultdict, Counter, deque
import os
import math
import sys

 
for _ in range(int(input())):
    n = int(input())
    v = list(map(int, input().split()))
    s = set()
    st = []
    mx = v[0]
    st.append(v[0])
    
    for i in range(1, n):
        if v[i] in s:
            mx = 0
            while st:
                s.add(st.pop())
        elif v[i] < mx:
            while st:
                s.add(st.pop())
            if v[i] in s:
                mx = 0
            else:
                st.append(v[i])
                mx = v[i]
        else:
            mx = v[i]
            st.append(v[i])
    
    print(len(s))
