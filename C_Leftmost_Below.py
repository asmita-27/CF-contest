def is_possible(target, current_min):
    if target == 0:
        return True
    if 2 * current_min <= target:
        return False

    remaining = target
    limit = current_min

    while remaining > 0:
        if limit <= 0 or 2 * limit <= remaining:
            return False
        used = min(remaining, limit)
        remaining -= used
        limit = used - 1

    return True

def can_reach_target_array(arr):
    current_min = arr[0]
    for i in range(1, len(arr)):
        if not is_possible(arr[i], current_min):
            return False
        current_min = min(current_min, arr[i])
    return True
 
t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    print("YES" if can_reach_target_array(b) else "NO")
