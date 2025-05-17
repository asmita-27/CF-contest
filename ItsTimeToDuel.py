for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    tot = sum(a)
    if tot==0 or tot > n-1 :
        print("YES")
        continue
    flag = False
    for i in range(n - 1):
        if a[i] == 0 and a[i+1] == 0:
            flag = True
            break
    if flag:
        print("YES")
    else:
        print("NO")
