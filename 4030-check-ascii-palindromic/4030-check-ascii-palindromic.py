class Solution:
    def isPalindromic(self, s: str) -> bool:
        arr = []
        
        for i in range(len(s)):
            arr.append(str(ord(s[i])))
        
        #Now converting the element into binary form which was stored in the array
        res = ""
        
        for i in range(len(arr)):
            temp = ""

            while int(arr[i]) > 0:
                ans = int(arr[i]) % 2
                temp = str(ans) + temp
                arr[i] = int(arr[i]) // 2


            while len(temp) < 8:
                temp = "0" + temp
            res += temp   
        found = 1
        l = 0
        r = len(res) - 1
        while l <= r:
            if res[l] != res[r]:
                found = 0
                break
            
            l += 1
            r -= 1

        
        if found == 1:
            return True
        else:
            return False
            


