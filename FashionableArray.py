t = int(input())
for _ in range(t):
    input()  # we don't actually need n
    a = list(map(int, input().split()))
    evens = sum(x % 2 == 0 for x in a)
    odds = len(a) - evens
    print(0 if evens == 0 or odds == 0 else min(evens, odds))
