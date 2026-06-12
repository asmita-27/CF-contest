import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, x = map(int, input().split())

    ra, rb = [], []
    n, s = a, 0
    while True:
        ra.append((n, s))
        if n == 0: break
        n //= x; s += 1
    n, s = b, 0
    while True:
        rb.append((n, s))
        if n == 0: break
        n //= x; s += 1

    ans = abs(a - b)
    for va, sa in ra:
        for vb, sb in rb:
            c = sa + sb + abs(va - vb)
            if c < ans:
                ans = c

    print(ans)
