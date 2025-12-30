from collections import defaultdict, Counter, deque
import os
import math
import sys
powers = [1 << i for i in range(21)]  


for _ in range(int(input())):
    a, b= map(int, input().split())
    answer = 0
    for k in range(1, 21):
        w1 = d1 = 0  
        w2 = d2 = 0  

        for i in range(k):
            if i % 2 == 0:
                w1 += powers[i]
                d2 += powers[i]
            else:
                d1 += powers[i]
                w2 += powers[i]
 
        if (w1 <= a and d1 <= b) or (w2 <= a and d2 <= b):
            answer = k
        else:
            break   
    print(answer)