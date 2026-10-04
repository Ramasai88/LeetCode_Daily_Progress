n = int(input())
arr = list(map(int,input().split()))
found = 0
for i in range(len(arr)-1):
    if arr[i] <= arr[i+1]:
        found = 1
    else:
        found = 0
        break

if found == 1:
    print("Yes")
else:
    print("No")

# Tc: Traversal -> N, total -> N, Space: O(1)
