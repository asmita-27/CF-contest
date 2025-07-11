for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    zero = ones = 0
    valid = [False] * n

    for i in range(n):
        if a[i] == '0':
            zero += 1
        else:
            ones += 1
        if zero == ones:
            valid[i] = True

    flip = True

    for i in range(n - 1):
        if (a[i] == b[i]) != (a[i + 1] == b[i + 1]):
            if not valid[i]:
                print("NO")
                flip = False
                break

    if flip:
        if a[-1] != b[-1] and not valid[-1]:
            print("NO")
        else:
            print("YES")
