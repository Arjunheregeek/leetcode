from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maxf = Counter()  # Initialize the maximum frequency counter for words2
        ans = []  # List to store the result
        
        # Compute the maximum frequency of each letter across all words in words2
        for word in words2:
            c = Counter(word)  # Count the frequency of each letter in the word
            for char in c:
                maxf[char] = max(maxf[char], c[char])  # Update max frequency
        
        # Check each word in words1
        for word in words1:
            ca = Counter(word)  # Count the frequency of each letter in the word
            
            # If the word satisfies all conditions, add it to the result
            if all(ca[char] >= maxf[char] for char in maxf):
                ans.append(word)
        
        return ans
