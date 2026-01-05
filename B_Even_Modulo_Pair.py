from collections import defaultdict, Counter, deque
import os
import math
import sys

def solve():

    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 1, -1, -1):
        for j in range(0, n - 1):
            if i != j and (a[i] % a[j]) % 2 == 0 and a[i] > a[j]:
                print(a[j], a[i])
                return 
    print(-1)
for _ in range(int(input())):
    solve()