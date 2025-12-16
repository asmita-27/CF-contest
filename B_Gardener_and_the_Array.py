from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())

    elements = []
    bit_count = {}

    # Read elements and count bits
    for _ in range(n):
        data = list(map(int, input().split()))
        k = data[0]
        bits = data[1:]
        elements.append(bits)
        for b in bits:
            bit_count[b] = bit_count.get(b, 0) + 1

    # Check condition
    answer = "No"
    for bits in elements:
        has_unique_bit = False
        for b in bits:
            if bit_count[b] == 1:
                has_unique_bit = True
                break
        if not has_unique_bit:
            answer = "Yes"
            break

    print(answer)



