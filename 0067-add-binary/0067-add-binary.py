class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        elif a == "0" and b == "1":
            return "1"
        #Integer tp binary conversion
        decimal = 0
        for x in a:
            decimal = decimal * 2 + int(x)
        
        decimal1 = 0
        for x in b:
            decimal1 = decimal1 * 2 + int(x)
        
        # Here both a & b converted into integers 
        ans = decimal + decimal1

        # Now Integer to Binary conversion
        binary = ""
        while ans > 0:
            rem = ans % 2
            binary = str(rem) + binary
            ans = ans // 2
        return binary



