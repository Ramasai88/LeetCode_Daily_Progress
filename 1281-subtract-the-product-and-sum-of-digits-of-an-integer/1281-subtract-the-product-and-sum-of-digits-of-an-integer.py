class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp1 = n
        temp2 = n
        pro = 1
        ans = 1
        ans2 = 0
        while temp1 > 0:
            res = temp1 % 10
            ans = ans * res
            temp1 = temp1 // 10
        
        while temp2 > 0:
            resl = temp2 % 10
            ans2 = ans2 + resl
            temp2 = temp2 // 10
        result = ans - ans2
        return result


        