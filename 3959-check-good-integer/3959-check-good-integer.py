class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        temp1 = n
        temp2 = n
        sumi = 0
        sumi1 = 0
        while temp1 > 0:
            digit_sum = temp1 % 10
            sumi = sumi + digit_sum
            temp1 = temp1 // 10
        
        while temp2 > 0:
            digit_sum1 = temp2 % 10
            sumi1 = (sumi1 + (digit_sum1)**2)
            temp2 = temp2 // 10
        c = abs(sumi - sumi1)
        if c >= 50:
            return True
        else:
            return False

        