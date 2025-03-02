class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans=[]
        dic={}
        for i in nums1 :
            dic[i[0]]=i[1]
        for j in nums2 :
            if j[0] not in dic:
                dic[j[0]]=j[1]
            else:
                dic[j[0]]+=j[1]
        return sorted(list(dic.items()))
        

            
                
                


        
        