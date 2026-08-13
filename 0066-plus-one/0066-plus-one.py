class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 0
        for i in range(len(digits)):
            c = c * 10 + digits[i]

        temp1 = c
        temp2 = c
        while c != 0:
            temp1 = temp1 // 10
            temp2 = temp2 % 10
            break

        result = temp1 * 10 + temp2 + 1
        arr1 = []
        # Now integer to array

        while result != 0:
            res1 = result % 10
            arr1.append(res1)
            result = result // 10

        arr1.reverse()
        return arr1
        
        
        