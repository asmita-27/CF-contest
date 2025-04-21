def fizz(n): 
    cycles = n // 15
    count = cycles * 3
     
    rem = n % 15
    count += min(rem + 1, 3)
    
    return count
 
t = int(input())   
results = []

for _ in range(t):
    n = int(input())   
    results.append(fizz(n))
 
for res in results:
    print(res)
