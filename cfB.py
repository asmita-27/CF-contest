
import math
for _ in range(int(input())):
    n = int(input())
    tot = n * (n + 1) // 2 
    if math.isqrt(tot) ** 2 == tot:
        print(-1)
        continue

    p = list(range(1, n + 1))
    curr = 0 
    for i in range(n - 1):
        curr += p[i]
        if math.isqrt(curr) ** 2 == curr: 
            p[i], p[i+1] = p[i+1], p[i] 
            curr = curr - p[i+1] + p[i]
    print(" ".join(map(str, p)))
