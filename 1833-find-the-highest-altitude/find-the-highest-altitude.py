class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=0
        altmax=0
        for i in gain:
            alt=alt+i
            altmax=max(altmax,alt)
        return altmax


        