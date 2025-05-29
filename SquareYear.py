import math
for i in range(int(input())):
    n = int(input())
    sqrt = math.ceil(math.sqrt(n))
    if sqrt*sqrt ==n:
        print(0 , sqrt)
    else:
        print(-1)