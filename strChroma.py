 
t = int(input())
for _ in range(t):
    n, x = map(int, input().split()) 
    for i in range(x):
        print(i, end=' ')

    for i in range(x + 1, n):
        print(i, end=' ')

    if x < n:
        print(x, end='')

    print()  
 