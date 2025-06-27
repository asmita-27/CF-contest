from collections import defaultdict, Counter, deque
import os
import math
import sys


n = int(input())
a= sum(list(map(int,input().split())))
b= sum(list(map(int,input().split())))
c= sum(list(map(int,input().split())))

print(a-b)
print(b-c)