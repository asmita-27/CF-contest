def mnSwaps(char, s):
    lst = [i for i, ch in enumerate(s) if ch == char]
    m = len(lst)
    if m <= 1:
        return 0
    arr = [lst[j] - j for j in range(m)]
    md = arr[m // 2]
    return sum(abs(x - md) for x in arr)

for _ in range(int(input())):
    n = int(input().strip())
    s = input().strip()
    cstA = mnSwaps('a', s)
    cstB = mnSwaps('b', s)
    print(str(min(cstA, cstB)))
