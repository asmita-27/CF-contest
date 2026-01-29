import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())

    p = x & ~y
    while p < x and p & y:
        p += p & -p

    q = y & ~x
    while q < y and q & x:
        q += q & -q

    if abs(x - p) <= abs(y - q):
        print(p, y)
    else:
        print(x, q)
