from collections import deque

class Solution(object):
    def continuousSubarrays(self, nums):
        start = 0
        result = 0
        
        # Deques to track the indices of min and max values
        min_deque = deque()
        max_deque = deque()
        
        for end in range(len(nums)):
            # Update the min deque
            while min_deque and nums[min_deque[-1]] > nums[end]:
                min_deque.pop()
            min_deque.append(end)
            
            # Update the max deque
            while max_deque and nums[max_deque[-1]] < nums[end]:
                max_deque.pop()
            max_deque.append(end)
            
            # Shrink the window if the condition is violated
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                if min_deque[0] == start:
                    min_deque.popleft()
                if max_deque[0] == start:
                    max_deque.popleft()
                start += 1
            
            # Count all subarrays ending at `end` that start between `start` and `end`
            result += (end - start + 1)
        
        return result
