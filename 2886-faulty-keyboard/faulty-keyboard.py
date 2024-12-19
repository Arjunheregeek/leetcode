class Solution(object):
    def finalString(self, s):
        while "i" in s:
            index=s.index("i")
            s=s[:index][::-1]+s[index+1:]
        return s 
        
        