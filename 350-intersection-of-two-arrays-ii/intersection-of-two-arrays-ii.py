class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d=Counter(nums1)
        ans=[]
        f=Counter(nums2)
        intersection=d & f
        for key,count in intersection.items():
            ans.extend([key]*count)
        return ans

        