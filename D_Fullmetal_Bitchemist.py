from collections import defaultdict, Counter, deque
import os
import math
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    total = n * (n + 1) // 2
    cnt = [1, 0, 0]
    pref = 0
    for c in s:
        if c == '0':
            pref = (pref + 1) % 3
        else:
            pref = (pref + 2) % 3
        cnt[pref] += 1
    bad = 0
    for x in cnt:
        bad += x * (x - 1) // 2
    ans = total - bad
    i = 0
    while i < n:
        j = i
        while j + 1 < n and s[j] != s[j + 1]:
            j += 1
        m = j - i + 1
        odd = ((m + 1) // 2) * ((m + 2) // 2)
        ans -= odd - m
        i = j + 1
    print(ans)