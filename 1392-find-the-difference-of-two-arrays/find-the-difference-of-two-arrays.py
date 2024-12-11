class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1=set(nums1)
        set2=set(nums2)
        ans=[0]*2
        k=list(set1-set2)
        j=list(set2-set1)
        k.sort()
        j.sort()
        ans[0]=k
        ans[1]=j
        return ans
        

        