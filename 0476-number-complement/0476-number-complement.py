class Solution:
    def findComplement(self, num: int) -> int:

        #Integer to Binary 
        arr = []
        binary = ""
        temp = num
        while temp > 0:
            rem = temp % 2
            binary = str(rem) + binary
            temp = temp // 2
        
        # Complement of binary
        for i in range(len(binary)):
            if binary[i] == "1":
                arr.append(0)
            elif binary[i] == "0":
                arr.append(1)
        
        # Converting the complement of binary into the Integer

        res = 0
        for i in range(len(arr)):
            res = res * 2 + int(arr[i])
        
        return res

        


        