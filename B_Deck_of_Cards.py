from collections import defaultdict, Counter, deque
import os
import math
import sys

for _ in range(int(input())):
    n, k = map(int, input().split())
    s =  input().strip()

    a = s.count('0')
    b = s.count('1')
    c = s.count('2')

    ans = ['+'] * n
    for i in range(n):
        if i < a + c or i >= n - b - c:
            ans[i] = '?'
        if i < a or i >= n - b or k == n:
            ans[i] = '-'

    print(''.join(ans))
