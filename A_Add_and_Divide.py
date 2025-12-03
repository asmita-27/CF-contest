 
for _ in range(int(input())):
    A, B = map(int, input().split())

    ans = 10**18

    start = 0 if B > 1 else 1

    for add in range(start, start + 40):
        b = B + add
        a = A
        ops = add

        while a > 0:
            a //= b
            ops += 1

        ans = min(ans, ops)

    print(ans)
