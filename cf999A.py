def max_points(test_cases):
    results = []
    for n, a in test_cases:
        evens = [x for x in a if x % 2 == 0]
        odds = [x for x in a if x % 2 != 0]
        sorted_a = evens + odds
        s = 0
        points = 0
        for num in sorted_a:
            s += num
            if s % 2 == 0:
                points += 1
                while s % 2 == 0:
                    s //= 2
        
        results.append(points)
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = max_points(test_cases)
print("\n".join(map(str, results)))
