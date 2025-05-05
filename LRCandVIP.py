from math import gcd
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    if all(x == a[0] for x in a):
        print("No")
        continue
 
    found = False
    for i in range(n):
        g = 0
        for j in range(n):
            if j == i: continue
            g = gcd(g, a[j])
        if g != a[i]: 
            ans = ['2'] * n
            ans[i] = '1'
            print("Yes")
            print(" ".join(ans))
            found = True
            break

    if not found: 
        print("No")
