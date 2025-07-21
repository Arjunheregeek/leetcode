class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        k=0
        for i in range(len(nums1)):
            k=nums2.index(nums1[i])
            for j in range (k+1,len(nums2)):
                
                if nums2[j]>nums1[i]:
                    ans.append(nums2[j])
                    break
            if len(ans)<i+1:
                ans.append(-1)
        return ans 


        