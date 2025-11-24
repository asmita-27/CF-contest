from collections import defaultdict, Counter, deque
import os
import math
import sys

s = list(input().strip())
n = len(s)
i =0
while i<n:
    j= i
    while j<n and s[j]==s[i]:
        j+=1
    c = 'a'
    while (c == s[i] or (i > 0 and c == s[i - 1]) or(j < n and c == s[j])):
        c = chr(ord(c) + 1)
    for k in range(i, j):
        if(i+k)&1:
            s[k]= c
    i = j
print("".join(s))