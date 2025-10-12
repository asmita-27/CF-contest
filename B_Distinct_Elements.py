import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input().strip())
    b = list(map(int, input().split()))
    prev = 0
    a = [0]*n
    nxt = 1
    for i in range(n):
        d = b[i] - prev
        prev = b[i]
        lst = (i+1) - d   
        if lst == 0:
            a[i] = nxt
            nxt += 1
        else: 
            a[i] = a[lst-1]
    print(' '.join(map(str,a)))
