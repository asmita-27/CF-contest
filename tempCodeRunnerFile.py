def minOp(n):
    if '7' in str(n):
        return 0
    
    count = 0
    add_val = 9
    while '7' not in str(n):
        n += add_val
        count += 1
    return count

def solve():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        results.append(str(minOp(n)))
    print("\n".join(results))
solve()