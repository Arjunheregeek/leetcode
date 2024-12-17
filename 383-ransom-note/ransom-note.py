class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote)==1 and len( magazine)==1:
            if  magazine==ransomNote:
                return True
            else:
                return False
        if len(ransomNote)==1:
            if ransomNote in magazine:
                return True
            else:
                return False
        
        mag=Counter( magazine)
        ran=Counter(ransomNote)
        for  key , value in ran.items():
            if ran[key]<=mag[key]:
                continue
            else:
                return False
        return True