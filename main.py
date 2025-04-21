def max_students_around_coffee_machines(t, test_cases):
    results = []
    
    for case in test_cases:
        n, a = case
        left = [0] * (n + 2)
        right = [0] * (n + 2)
        
        for i in range(1, n + 1):
            left[i] = a[i - 1] + left[i - 1] // 2
        
        for i in range(n, 0, -1):
            right[i] = a[i - 1] + right[i + 1] // 2
       
        result = []
        for i in range(1, n + 1):
            result.append(max(left[i], right[i]))
        
        results.append(result)
    
    return results

def main():
    t = int(input())
    test_cases = []
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        test_cases.append((n, a))
    
    results = max_students_around_coffee_machines(t, test_cases)
    
    for result in results:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()