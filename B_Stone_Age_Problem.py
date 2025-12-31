import sys
input = sys.stdin.readline
 
n, q = map(int, input().split())
a = list(map(int, input().split()))

totSm = sum(a)
lastUpdt = [0] * n
lastFull =-1
base = 0
time = 0

for _ in range(q):
    time += 1
    ip = list(map(int, input().split()))
    t = ip[0]

    if t == 1:
        i, x = ip[1], ip[2]
        i -= 1

        if lastUpdt[i] > lastFull:
            old = a[i]
        else:
            old = base

        totSm += x - old
        a[i] = x
        lastUpdt[i] = time

    else:
        x = ip[1]
        base = x
        lastFull = time
        totSm = n * x

    print(totSm)
