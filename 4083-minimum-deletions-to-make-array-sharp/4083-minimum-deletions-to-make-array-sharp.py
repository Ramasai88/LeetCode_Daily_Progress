class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        xor = 1
        count = 0
        for i in range(len(nums)-1):
            if nums[i] ^ nums[i+1] == 0:
                count += 1
            else:
                pass

        return count
                
        