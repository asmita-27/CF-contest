import math

def help(x):
    if x < 2:
        return 0
    else:
        return math.floor(math.log2(x - 1)) + 1

for _ in range(int(input())):
    n, m, a, b = map(int, input().split())
    rowCutA = min(a,n-a+1)

    colCutB = min(b,m-b+1)
    
    helpR = help(rowCutA) + help(m)
    helpC = help(n) + help(colCutB)
    print(min(helpR+1, helpC+1))