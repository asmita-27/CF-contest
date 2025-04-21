def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n, l, r = map(int, input().split())  # Read n, l, r
        a = list(map(int, input().split()))  # Read the array a
        
        # Convert 1-based index to 0-based index
        l -= 1
        r -= 1
        
        # Extract the subarray from l to r
        subarray = a[l:r+1]
        
        # Sort the subarray and assign the minimum elements from the sorted array
        a_sorted = sorted(a)
        
        # Reassign the minimum elements to the subarray [l, r] using the sorted array
        a[l:r+1] = a_sorted[l:r+1]
        
        # Calculate the sum of the modified subarray
        result = sum(a[l:r+1])
        
        # Output the result for the current test case
        print(result)

# Call the function to process the input and output
solve()
