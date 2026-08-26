class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        binary = ""
        temp = n
        while temp > 0:
            rem = temp % 2
            binary = str(rem) + binary
            temp = temp // 2
        
        for i in range(len(binary)):
            if binary[i] == "1":
                count += 1
        
        return count
        