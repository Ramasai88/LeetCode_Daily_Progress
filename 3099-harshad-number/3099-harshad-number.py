class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        ans = 0
        res = x
        while x != 0:
            temp = x % 10
            ans = ans + temp
            x = x // 10
        if res % ans == 0:
            return ans
        else:
            return -1

        