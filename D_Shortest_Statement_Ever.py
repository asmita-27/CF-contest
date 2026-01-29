import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())

    a = x & y

    p1, q1 = x - a, y + a
    p2, q2 = x + a, y - a

    cost1 = abs(x - p1) + abs(y - q1)
    cost2 = abs(x - p2) + abs(y - q2)

    if cost1 <= cost2:
        print(p1, q1)
    else:
        print(p2, q2)
