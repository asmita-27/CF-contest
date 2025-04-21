import math

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    centers = list(map(int, input().split()))
    radii = list(map(int, input().split()))
    
    D = {}
    
    for i in range(n):
        c = centers[i]
        r = radii[i]
        left = c - r
        right = c + r
        for x in range(left, right + 1):
            dx = x - c
            d = math.isqrt(r * r - dx * dx)
            if x in D:
                if d > D[x]:
                    D[x] = d
            else:
                D[x] = d

    total_points = 0
    for d in D.values():
        total_points += 2 * d + 1
        
    print(total_points)
