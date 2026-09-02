class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        #First dealing with even elements in the array
        odd_value = 0
        found = 0
        nums2 = []
        count_even = 0
        for i in range(len(nums1)):
            if nums1[i] % 2 == 0:
                count_even += 1
            else:
                odd_value = nums1[i]
        
        if count_even == len(nums1):
            return True

            
            

        # Now dealing with odd elements in the array
        for i in range(len(nums1)):
            if nums1[i] % 2 == 0 or nums1[i] % 2 != 0:
                if nums1[i] % 2 == 0:

                    c = nums1[i] - odd_value
                    nums2.append(c)
                else:
                    nums2.append(nums1[i])

        count_odd = 0
        for i in range(len(nums2)):
            if nums2[i] % 2 != 0:
                count_odd += 1
        if count_odd == len(nums2):
            return True


        
        