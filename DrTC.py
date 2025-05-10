for i in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    for x in s :
        if x=='0':
            ans +=1
        else:
            ans +=n-1
    print(ans)