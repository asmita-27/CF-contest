import math

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    ones = s.count('1')

    # Case 1: no students initially
    if ones == 0:
        print((n + 2) // 3)   # ceil(n/3)
        continue

    res = ones
    i = 0

    while i < n:
        if s[i] == '0':
            j = i
            while j < n and s[j] == '0':
                j += 1

            L = j - i
            left = (i > 0 and s[i - 1] == '1')
            right = (j < n and s[j] == '1')

            if left and right:
                # middle segment
                if L >= 2:
                    res += (L - 2 + 2) // 3   # ceil((L-2)/3)
            else:
                # edge segment
                res += (L - 1 + 2) // 3       # ceil((L-1)/3)

            i = j
        else:
            i += 1

    print(res)
