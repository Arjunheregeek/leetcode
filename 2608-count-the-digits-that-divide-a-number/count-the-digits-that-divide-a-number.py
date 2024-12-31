class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        for i in str(num):
            if num%int(i)==0:
                c+=1
        return c 
        