t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x = None
    min_x, max_x = 0, float('inf')
    valid = True

    for i in range(n):
        if b[i] != -1:
            curr_x = a[i] + b[i]
            if x is None:
                x = curr_x
            elif x != curr_x:
                valid = False
                break
        else:
            min_x = max(min_x, a[i])
            max_x = min(max_x, a[i] + k)

    if not valid:
        print(0)
    elif x is not None:
        print(1 if min_x <= x <= max_x else 0)
    else:
        print(max(0, max_x - min_x + 1))
