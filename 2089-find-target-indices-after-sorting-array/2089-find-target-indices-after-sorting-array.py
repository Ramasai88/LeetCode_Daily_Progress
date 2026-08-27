class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        nums1 = []
        for i in range(len(nums)):
            if nums[i] == target:
                nums1.append(i)
        
        return nums1

        