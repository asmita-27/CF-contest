def main():
    q = int(input())
    stack = [0] * 100
    results = []
    
    for _ in range(q):
        query = input().split()
        if query[0] == "1":
            x = int(query[1])
            stack.append(x)
        else:
            results.append(str(stack.pop()))
    
    print("\n".join(results))


main()
