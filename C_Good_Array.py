from collections import defaultdict, Counter, deque
import os
import math
import sys

n = int(input())
a = list(map(int, input().split()))
counts = Counter(a)
sum_a = sum(a)

answers = []  
for i in range(n):  
	new_sum = sum_a - a[i]  
	counts[a[i]] -= 1  
	if new_sum % 2 == 0 and (new_sum // 2) <= 10**6 and counts[new_sum // 2] > 0:
		answers.append(i + 1)  
	counts[a[i]] += 1   
print(len(answers))
if answers:
	print(*answers)