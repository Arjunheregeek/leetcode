class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
       
            

        start=0
        end=len(nums)-1
        while start<=end:
            mid = start+ (end-start)//2
            if nums[mid] == target :
                l=mid

                while nums[l]==target:

                    l-=1
                    if l<0:
                        break
                r=mid
                if mid==len(nums)-1:
                    return (l+1,mid)
                while nums[r]==target :
                    r+=1
                    if r >len(nums)-1:
                        break
                return [l+1,r-1]
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return [-1,-1]
                

                