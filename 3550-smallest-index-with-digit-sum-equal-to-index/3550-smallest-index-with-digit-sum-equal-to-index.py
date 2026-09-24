class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        digit_sum = 0
        found = 0
        ans = 0
        for i in range(len(nums)):
            temp = nums[i]
            while temp > 0:
                num = temp % 10 
                digit_sum = digit_sum + num
                temp = temp // 10
            if digit_sum == i:
                found = 1
                ans = i
                break
            else:
                found = 0
                digit_sum = 0
        
        if found == 1:
            return ans
        else:
            return -1
             
        