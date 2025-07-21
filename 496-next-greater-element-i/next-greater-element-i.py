class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        stk = [] 
        for num in nums2 :
            while stk and num > stk[-1] :
                dic[stk.pop()] = num 
            stk.append(num)
            
        ans= [] 
        for i in nums1:
            ans.append(dic.get(i,-1))
        return ans
            
        
       
        