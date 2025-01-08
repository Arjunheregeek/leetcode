class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        xr=pref[0]
        for i in range(len(pref)-1,0,-1):
            
        

            pref[i]^=pref[i-1]
        return pref
        