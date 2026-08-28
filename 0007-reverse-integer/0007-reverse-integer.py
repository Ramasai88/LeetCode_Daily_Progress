class Solution:

    def reverse(self, x: int) -> int:

        temp = abs(x)

        res = 0

        while temp > 0:

            digit = temp % 10

            res = res * 10 + digit

            temp = temp // 10

        if res > 2**31 - 1 or res < -2**31:

            return 0

        if x > 0:

            return res

        else:

            return -res