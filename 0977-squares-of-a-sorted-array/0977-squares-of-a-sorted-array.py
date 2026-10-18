class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        arr1 = []
        for i in range(len(nums)):
            ans = nums[i] ** 2
            arr1.append(ans)
        
        arr1.sort()
        return arr1
        