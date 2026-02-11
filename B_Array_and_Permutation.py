import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    possible = True
    
    for i in range(n):
        if a[i] != p[i]:
            left_ok = (i > 0 and a[i] == a[i-1])
            right_ok = (i < n-1 and a[i] == a[i+1])
            if not left_ok and not right_ok:
                possible = False
                break
    
    print("YES" if possible else "NO")
