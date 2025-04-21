import sys
def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if all(x < 0 for x in a):
            print(sum(-x for x in a))
            continue
        start = 0
        while start < n and a[start] < 0:
            start += 1
        res = 0
        cur = a[start]
        i = start + 1
        while i < n:
            if a[i] * cur > 0:
                cur += a[i]
            else:
                res += abs(cur)
                cur = a[i]
            i += 1
        res += abs(cur)
        print(res)
if __name__ == '__main__':
    main()
