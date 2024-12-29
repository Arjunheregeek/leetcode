class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        ans = []
        for i in range(len(strs)):
            

            if ''.join(sorted(strs[i])) in dic:
                dic[''.join(sorted(strs[i]))].append(strs[i])
                                   


            else:

                dic[''.join(sorted(strs[i]))] =[strs[i]]
        for key ,value in dic.items():
            ans.append(value)
        return ans 
                         