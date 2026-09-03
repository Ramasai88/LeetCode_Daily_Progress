class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        temp = n
        count = 0
        found = 0
        if n <= 0:
            return False
        
        while n % 3 == 0:
            count += 1
            n = n // 3
            if n == 0:
                break
        if 3**count == temp:
            found = 1
        
        if found == 1:
            return True
        else:
            return False
        