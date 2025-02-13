class Solution:
    def minOperations(self,nums, k):
        heapq.heapify(nums)  # Convert nums into a min-heap
        operations = 0

        while len(nums) > 1 and nums[0] < k:  
            x = heapq.heappop(nums)  # Smallest element
            y = heapq.heappop(nums)  # Second smallest element

            # Apply the operation
            new_val = 2 * min(x, y) + max(x, y)
            heapq.heappush(nums, new_val)

            operations += 1  # Increment operation count

        return operations if nums[0] >= k else -1