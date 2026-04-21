from collections import defaultdict, Counter, deque
import os
import math
import sys


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
    
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            print(-1)
            return
    
    print(*a)

def main():
    t = int(input())
    while t:
        solve()
        t -= 1

if __name__ ==  "__main__":
    main()