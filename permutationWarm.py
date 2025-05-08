def solution(n):
    k = n // 2
    if n % 2:
        print(k * (k + 1) + 1)
    else:
        print(k * k + 1)

t = int(input())
for _ in range(t):
    n = int(input())
    solution(n)
