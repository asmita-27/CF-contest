def fun(s):
    digits = sorted(s)
    res = [''] * 10
    used = [False] * 10
    for i in range(10):
        for j in range(10):
            if not used[j] and int(digits[j]) >= (9 - i):
                res[i] = digits[j]
                used[j] = True
                break
    return ''.join(res)
 
t = int(input())
for _ in range(t):
    s = input() 
    print(fun(s))
