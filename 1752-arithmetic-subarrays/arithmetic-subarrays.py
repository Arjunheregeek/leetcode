class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i in range(len(l)):
            sa=nums[l[i]:r[i]+1]
            sa.sort()
            d=sa[0]-sa[1]
            p=0
            for j in range(1,len(sa)-1):
                if sa[j]-sa[j+1]==d:
                    continue 
                else:
                    p=1
                    break
            if p==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
                

                

        
        