from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        unique_numbers = set()  # Initialize a set to store unique integers
        
        for num in nums:
            unique_numbers.add(num)  # Add the original number
            reversed_num = int(str(num)[::-1])  # Reverse the number
            unique_numbers.add(reversed_num)  # Add the reversed number
        
        return len(unique_numbers)  # Return the count of distinct integers
