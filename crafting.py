def can_craft(n, a, b):
    S_a = sum(a)
    S_b = sum(b)
    
    if n == 2:
        # For n = 2, the total is invariant. We can shift amounts if and only if:
        #   a[0] + a[1] >= b[0] + b[1]
        return "YES" if S_a >= S_b else "NO"
    else:
        if S_a < S_b:
            return "NO"
        threshold = (S_a - S_b) / (n - 2)
        for i in range(n):
            if b[i] - a[i] > threshold:
                return "NO"
        return "YES"

if __name__ == '__main__':
    import sys
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index+n]))
        index += n
        b = list(map(int, data[index:index+n]))
        index += n
        results.append(can_craft(n, a, b))
    sys.stdout.write("\n".join(results))
