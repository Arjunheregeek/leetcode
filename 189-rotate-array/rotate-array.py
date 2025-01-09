class Solution(object):
   def rotate(self, nums, k):
       # Get the actual number of rotations
       k = k % len(nums)      
       # Get the number of elements to move from the end to the beginning
       r = len(nums) - k
       # Store the elements to move
       new = nums[0:r]
       # Remove the elements from the beginning
       nums[0:r] = []
       # Append the stored elements to the end
       nums.extend(new)