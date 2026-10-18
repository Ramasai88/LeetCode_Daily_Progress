class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        # For Every Iteration, I have to change the outer loop, 
        arr = []
        for i in range(len(nums)):
            count = 0
            arr.clear()
            arr = set(arr)
            for j in range(i,len(nums)):
                if nums[j] not in arr:
                    arr.add(nums[j])
                    count += 1
                ans = ans + count ** 2
        
        return ans 