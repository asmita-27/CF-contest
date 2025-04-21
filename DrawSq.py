for _ in range(int(input())):
    l,r,d, u = map(int,input().split())
    if l==r and d==u and l==d:
        print("Yes")
    else:
        print("No")