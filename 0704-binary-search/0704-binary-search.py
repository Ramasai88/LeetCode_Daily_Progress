class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        found = 0
        while l <= h:
            mid = (l + h) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] <= target:
                l = mid + 1
            else:
                h = mid - 1
        if found == 0:
            return -1
                 