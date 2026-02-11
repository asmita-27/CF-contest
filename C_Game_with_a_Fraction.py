import sys
input = sys.stdin.readline
 
for _ in range(int(input())):
    p, q = map(int, input().split()) 
    if p < q <= (3 * p) // 2:
        print("Bob")
    else:
        print("Alice")
