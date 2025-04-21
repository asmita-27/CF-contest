from collections import Counter

def minSteps(n, digits):
    target = "01032025"
    target_count = Counter(target)
    current_count = Counter()
    for i in range(n):
        current_count[str(digits[i])] += 1 
        if all(current_count[d] >= target_count[d] for d in target_count):
            return i + 1
    return 0

for _ in range(int(input())):
    n = int(input())
    digits = list(map(int, input().split()))
    res  = minSteps(n, digits)
    print(res)
