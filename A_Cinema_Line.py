from collections import defaultdict, Counter, deque
import os
import math
import sys
def main():
    n = int(input())
    arr = list(map(int, input().split()))

    l25 = 0
    l50 = 0

    for bill in arr:
        if bill == 25:
            l25 += 1
        elif bill == 50:
            if l25 >= 1:
                l50 += 1
                l25 -= 1
            else:
                print("NO")
                return
        elif bill == 100:
            if l50 >= 1 and l25 >= 1:
                l50 -= 1
                l25 -= 1
            elif l25 >= 3:
                l25 -= 3
            else:
                print("NO")
                return

    print("YES")




if __name__ == "__main__": 
    main()