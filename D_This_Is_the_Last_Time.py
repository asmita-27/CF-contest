import heapq

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    casinos = []
    for _ in range(n):
        l, r, reali = map(int, input().split())
        casinos.append((l, r, reali))
    
    casinos.sort()  
    heap = []
    index = 0
    curr = k

    while True:
        while index < n and casinos[index][0] <= curr:
            l, r, reali = casinos[index]
            if curr <= r:
                heapq.heappush(heap, (-reali, r))             
            index += 1
        
        while heap and heap[0][1] < curr:
            heapq.heappop(heap)
        
        if not heap:
            break
        
        reali, _ = heapq.heappop(heap)
        curr = -reali

    print(curr)
