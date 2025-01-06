class Solution:
    def isPalindrome(self, s: str) -> bool:
        a =s.lower()
        j=""

        for i in a :
            if i.isalnum():
                j= j+i
                
       
        low=0
        high=len(j)-1
        while low<high:
            if j[low]==j[high]:
                low+=1
                high-=1
                continue
            else:
                return False
        return True


        

        
        





        

        