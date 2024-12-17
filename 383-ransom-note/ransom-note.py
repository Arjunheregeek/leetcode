class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mag=Counter( magazine)
        ran=Counter(ransomNote)
        for  key , value in ran.items():
            if ran[key]<=mag[key]:
                continue
            else:
                return False
        return True