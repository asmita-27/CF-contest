import sys
input = sys.stdin.readline

MAX = 10**6
spf = [0]*(MAX+1)
isPrPow = [True]*(MAX+1)
for i in range(2, MAX+1):
    if spf[i] == 0:
        for j in range(i, MAX+1, i):
            if spf[j] == 0:
                spf[j] = i
for x in range(2, MAX+1):
    y = x
    p = spf[x]
    while y % p == 0:
        y //= p
    if y != 1:
        isPrPow[x] = False
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    def nonDec(a):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                return False
        return True
    if nonDec(a):
        print("Bob")
        continue
    allPrPow = True
    prevPrime = -1
    flg = True
    for x in a:
        if not isPrPow[x]:
            allPrPow = False
        p = spf[x]
        if prevPrime > p:
            flg = False
        prevPrime = p

    if allPrPow and flg:
        print("Bob")
    else:
        print("Alice")