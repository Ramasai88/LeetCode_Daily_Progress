class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        c = bin(n)[2:]
        for index, digit in enumerate(c):
            if digit == "1":
                count += 1
            else:
                pass
        
        return count
        