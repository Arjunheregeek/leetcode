class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic={}
        ans=[]
        for key,value in enumerate(groupSizes):
            if value not in dic:
                dic[value]=[]
            dic[value].append(key)
            if len(dic[value])==value:
                ans.append(dic[value])
                dic[value]=[]
        return ans
            

        