t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
 
    a = [max(l[i], r[i]) for i in range(n)]
    b = [min(l[i], r[i]) for i in range(n)]

    total = sum(a)
 
    extra = 0
    if k > 1:
        b.sort(reverse=True)
        extra = sum(b[:k-1])
 
    print(total + extra + 1)
