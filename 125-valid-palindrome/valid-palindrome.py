class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        j=""
        for i in s :
            if i.isalnum():
                j=j+i
        if j==j[::-1]:
            return True
        else:
            return False
         
        
        