class Solution:
    def convertToBase7(self, num: int) -> str:
        s=""
        k=1
        if -7<num<7:
            return str(num)
        
        while True :
            if num<0:
                k=0
                num=abs(num)         
            
            
            
            s=s+str(num%7)
            num=num//7
            if num<7:
                s=s+str(num)
                s=s[::-1]
                if k ==0:
                    s="-"+s
                return s
            
        