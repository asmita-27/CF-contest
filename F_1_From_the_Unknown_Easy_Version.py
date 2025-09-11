import sys

# Example: single test case
# First query
print("? 2 100000 100000")
sys.stdout.flush()
res1 = input().strip()
if res1 == "-1":
    exit()
res1 = int(res1)

# Second query
print("? 1 1")
sys.stdout.flush()
res2 = input().strip()
if res2 == "-1":
    exit()
res2 = int(res2)

# Report answer
W = 100000 if res1 == 1 else 1  # just example logic
print(f"! {W}")
sys.stdout.flush()
