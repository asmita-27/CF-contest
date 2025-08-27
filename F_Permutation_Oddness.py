MOD = 10**9 + 7

def lowbit(x): 
    if x == 0:
        return 0
    return x & (-x)

def solve_permutation_oddness(c0, c1, c2, c3):
   
    n = c0 + c1 + c2 + c3
    max_oddness = 2 * (n - 1)
     
    lowbit_vals = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            lowbit_vals[i][j] = lowbit(i ^ j)
    
    cache = {}
    
    def count_ways(pos, last, counts, target_oddness, current_oddness):
       
        if pos == n:
            return 1 if current_oddness == target_oddness else 0
        
        if current_oddness > target_oddness:
            return 0  # Pruning: can't reduce oddness
            
        key = (pos, last, tuple(counts), target_oddness, current_oddness)
        if key in cache:
            return cache[key]
        
        result = 0
        for elem in range(4):
            if counts[elem] > 0:
                new_counts = counts[:]
                new_counts[elem] -= 1
                if pos == 0:
                    result += count_ways(pos + 1, elem, new_counts, target_oddness, current_oddness)
                else:
                    contribution = lowbit_vals[last][elem]
                    new_oddness = current_oddness + contribution
                    result += count_ways(pos + 1, elem, new_counts, target_oddness, new_oddness)
                
                result %= MOD
        
        cache[key] = result
        return result
     
    results = []
    for target_oddness in range(max_oddness + 1):
        cache.clear()   
        total = count_ways(0, -1, [c0, c1, c2, c3], target_oddness, 0)
        results.append(total)
    
    return results

def main(): 
    t = int(input())
    
    for _ in range(t):
        c0, c1, c2, c3 = map(int, input().split())
        result = solve_permutation_oddness(c0, c1, c2, c3)
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()