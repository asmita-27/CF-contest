t = int(input())
for _ in range(t):
    n, m, p, q = map(int, input().split())
    if n % p != 0:
        print("YES")
    else: 
        if m == (n // p) * q:
            print("YES")
        else:
            print("NO")
