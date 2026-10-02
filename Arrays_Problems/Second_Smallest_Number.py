n = int(input())
arr = list(map(int,input().split()))
smallest = arr[0]
second_smallest = float('inf')  # Initialize second_smallest to infinity
for i in range(1,n):
    if arr[i] < smallest:
        second_smallest = smallest
        smallest = arr[i]
    elif arr[i] < second_smallest and arr[i] != smallest:
        second_smallest = arr[i]

print(second_smallest)
# Tc: Traversal -> N, total -> N, Space: O(1)