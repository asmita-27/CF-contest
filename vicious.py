t = int(input())
for _ in range(t):
    n, k = map(int, input().split()) 
    if k % 2 == 1:
        ans = [n] * (n - 1) + [n - 1]
    else:
        ans = [n - 1] * (n - 2) + [n, n - 1]
    print(" ".join(map(str, ans)))
    