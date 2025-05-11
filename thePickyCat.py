 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = abs(a[0]) 
    s = sum(1 for i in a[1:] if abs(i) < x) 
    if s <= n//2:
        print("YES")
    else:
        print("NO")
