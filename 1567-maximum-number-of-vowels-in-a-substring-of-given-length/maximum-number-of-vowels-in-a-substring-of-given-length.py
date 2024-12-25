class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        start=0
        end= k-1
        ma=0
        l=0
        vo={"a","i","e","o","u"}
        while end <len(s):
            if l==0:
                for j in s[start:end+1]:
                    if j in vo:
                        count+=1
                start+=1
                end+=1
                ma=count
                l=1
                continue
            if s[end] in vo :
                count+=1
            if s[start-1] in vo :
                count-=1
            ma=max(ma,count)
           
            
            start+=1
            end+=1
        return ma 


            
            
            
            

        