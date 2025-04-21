for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if n == 1:
        print(a[0])
    else:
        print(sum(a) - (n - 1))