class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sumi = 0
        for i in range(1,len(nums)+1):
            if len(nums) % i == 0:
                sumi += nums[i-1] * nums[i-1]
            else:
                pass
        return sumi
        