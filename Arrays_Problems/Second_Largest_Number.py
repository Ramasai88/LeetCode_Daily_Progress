# Brute Force Approach

#n = int(input())
#arr = list(map(int,input().split()))
#arr.sort()
#largest = arr[n-1]
#second_largest = -1
#for i in range(len(arr)-2,-1,-1):
#    if arr[i] != largest:
#        second_largest = arr[i]
#        break

#print(second_largest)

# TC: Sorting -> NlogN, Traversal -> N, total -> NlogN + N = NlogN, Space: O(1)

# Better Approach

#n = int(input())
#arr = list(map(int,input().split()))
#largest = arr[0]
#second_largest = -1
#for i in range(0,n):
#    if arr[i] > largest:
#        largest = arr[i]

#for i in range(0,n):
#    if arr[i] > second_largest and arr[i] != largest:
#        second_largest = arr[i]

#print(second_largest)

# Tc: 1st Traversal -> N, 2nd Traversal -> N, total -> N + N = 2N, Space: O(1)


# Optimal Approach
n = int(input())
arr = list(map(int,input().split()))
largest = arr[0]
second_largest = -1
for i in range(1,n):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print(second_largest)
# Tc: Traversal -> N, total -> N, Space: O(1)