class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        s=0
        k=[]
        for i in range(len(number)):
            if i==len(number)-1 and number[i]==digit:
                if s>int(number[:i]):
                    return str(s)
                return number[:i]

            if number[i]==digit:
                if s<int(number[:i]+number[i+1:]):
                    s=int(number[:i]+number[i+1:])
               
        return str(s)
    
        

        

        
        