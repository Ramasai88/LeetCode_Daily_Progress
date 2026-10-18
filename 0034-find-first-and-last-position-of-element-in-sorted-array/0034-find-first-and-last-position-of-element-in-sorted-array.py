
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        arr = [-1, -1]

        # Find the first occurrence
        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                arr[0] = mid
                h = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

        # Find the last occurrence
        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                arr[1] = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

        return arr
