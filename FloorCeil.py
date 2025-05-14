
def F(x, n):
    while n > 0:
        if x == 0:
            return x
        x = x >> 1  
        n -= 1
    return x

def C(x, n):  
    while n > 0:
        if x <= 1:
            return x
        x = (x + 1) >> 1  
        n -= 1
    return x

t = int(input())
for _ in range(t):
    x, n, m = map(int, input().split())
    x_min = F(C(x, m), n)
    x_max = C(F(x, n), m)
    print(f"{x_min} {x_max}")
