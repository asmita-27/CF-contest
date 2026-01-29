import sys
input = sys.stdin.readline

def find_next(val, conflict):
    while val & conflict:
        bit = val & conflict & -(val & conflict)
        val = (val | (bit - 1)) + 1
    return val

def find_largest(val, conflict):
    result = 0
    for bit in range(30, -1, -1):
        if not ((1 << bit) & conflict):
            if result + (1 << bit) <= val:
                result += (1 << bit)
    return result

for _ in range(int(input())):
    x, y = map(int, input().split())
    
    best = float('inf')
    ans_p, ans_q = 0, 0
    
    candidates = [
        (x, y & ~x),
        (x & ~y, y),
        (find_next(x, y), y),
        (x, find_next(y, x)),
        (x, find_largest(y, x)),
        (find_largest(x, y), y),
    ]
    
    for p, q in candidates:
        if p >= 0 and q >= 0 and (p & q) == 0:
            cost = abs(x - p) + abs(y - q)
            if cost < best:
                best = cost
                ans_p, ans_q = p, q
    
    print(ans_p, ans_q)
