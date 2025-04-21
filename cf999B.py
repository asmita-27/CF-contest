import math

# Function to calculate gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to solve the problem for each test case
def solve(l, r):
    # To count minimal coprime segments
    count = 0
    
    # Iterate over all starting points from l to r
    for start in range(l, r + 1):
        # For each start, count how many end points from start to r
        # are coprime with the start (gcd(start, end) == 1)
        for end in range(start, r + 1):
            if gcd(start, end) == 1:
                count += 1
    
    return count

# Input reading
t = int(input())  # Number of test cases
for _ in range(t):
    l, r = map(int, input().split())  # Reading each l and r
    print(solve(l, r))  # Solve for each test case
