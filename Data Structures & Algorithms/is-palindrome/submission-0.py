class Solution:
    def isPalindrome(self, s: str) -> bool:
        strn=""
       
        for i in s: 
            if i.isalnum():
                strn=strn+i.lower()
    
        rev=""
        for i in strn:
            rev=i+rev

        if strn==rev:
            return True

        return False

        