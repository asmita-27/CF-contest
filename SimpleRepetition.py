import math

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    if k > 1 and x > 1:
        print("NO", end='')
    elif k == 1:
        print("YES" if is_prime(x) else "NO", end='')
    else:
        print("YES" if k == 2 else "NO", end='')
    print()
 