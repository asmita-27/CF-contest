from collections import defaultdict, Counter, deque
import os
import sys
import math

def main():
    
    a, b, k = map(int, input().split())
    
    if a == 0 and b == 0:
        print(0)
        return
    g = math.gcd(a, b)
    if a // g <= k and b // g <= k:
        print(1)
        return
    
    if a <= k and b <= k:
        print(1)
        return

    print(2)
for _ in range(int(input())):    
    main()