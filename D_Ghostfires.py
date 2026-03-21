from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    r, g, b = map(int, input().split())
    
    best = ""
    
    patterns = [
        ('R','G','B'),
        ('R','B','G'),
        ('G','R','B'),
        ('G','B','R'),
        ('B','R','G'),
        ('B','G','R')
    ]
    
    for p in patterns:
        cr, cg, cb = r, g, b
        s = []
        
        i = 0
        while True:
            ch = p[i % 3]
            
            if ch == 'R':
                if cr == 0: break
                cr -= 1
            elif ch == 'G':
                if cg == 0: break
                cg -= 1
            else:
                if cb == 0: break
                cb -= 1
            
            s.append(ch)
            i += 1
        
        if len(s) > len(best):
            best = "".join(s)
    
    print(best)
