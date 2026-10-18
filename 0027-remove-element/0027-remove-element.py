class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        arr1 = []
        for i in range(len(nums)):
            if nums[i] == val:
                pass
            else:
                arr1.append(nums[i])
        
        nums[:] = arr1
        c = len(nums)

        return c



        