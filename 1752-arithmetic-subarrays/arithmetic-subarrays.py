class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i in range(len(l)):
            sa=nums[l[i]:r[i]+1]
            sa.sort()
            d=sa[0]-sa[1]
            p=True
            for j in range(1,len(sa)-1):
                if sa[j]-sa[j+1]==d:
                    continue 
                else:
                    p=False
                    break
            ans.append(p)
        return ans
                

                

        
        