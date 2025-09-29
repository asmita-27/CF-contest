def getDiv (n):
    res = []
    for i in range(1,n//2+1):
        if n%i==0:
            res.append(i)
    res.append(n)
    return len(res)

def checkPrime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for _ in range(int(input())):
    l,r = map(int,input().split())
    cnt = 0
    for i in range(l,r+1):
        pr = getDiv(i)
        if checkPrime(pr):
            cnt +=1 
    print(cnt)