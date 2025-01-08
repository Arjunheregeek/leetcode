class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        soFar = 0
        ret = []
        last = 0
        for i in pref:

            ret.append(i ^ last)
            last = i 

        return ret