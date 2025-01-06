class Solution:
    def isPalindrome(self, s: str,i=0,n=None,k=0) -> bool:
        if k <1:
            s="".join(s.split())
        
        
        
        if n is None:
            n=len(s)-1
        if n<=i:
            return True
        while s[i].isalnum() is False:
            i+=1
            if i >len(s)-1:
                break
        while s[n].isalnum() is False:
            n-=1
            if n<0:
                break
        if n<=i:
            return True
        if s[i].lower()==s[n].lower():
            return self.isPalindrome(s,i+1,n-1,2)
        else:
            return False

        

        

        
        





        

        