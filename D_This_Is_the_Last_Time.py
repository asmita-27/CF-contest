
import heapq


 
 
for _ in range(int(input())):
    n, k = map(int, input().split())
    cas = [tuple(map(int, input().split())) for _ in range(n)] 
    cas.sort(key=lambda x: x[0])
    
    x = k
    i = 0
    maxHeap = []   
    while True: 
        while i < n and cas[i][0] <= x:
            l, r, real = cas[i]
            if r >= x: 
                heapq.heappush(maxHeap, -real)
            i += 1
        
        if not maxHeap: 
            break
            
        best = -heapq.heappop(maxHeap)
        if best <= x: 
            break
        x = best
    
    print(x)


