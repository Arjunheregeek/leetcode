class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Track the first and last positions of each character
        first_pos = [-1] * 26
        last_pos = [-1] * 26
        result_set = set()
        
        # Iterate over the string
        for i, char in enumerate(s):
            idx = ord(char) - ord('a')
            # Update last position for this character
            last_pos[idx] = i
            
        # Iterate backward to fill the first position
        for i in range(len(s) - 1, -1, -1):
            idx = ord(s[i]) - ord('a')
            first_pos[idx] = i

        # Iterate over each character as the middle of a palindrome
        for mid_idx, mid_char in enumerate(s):
            mid = ord(mid_char) - ord('a')
            
            # For each character `a` in the alphabet
            for a in range(26):
                if first_pos[a] != -1 and first_pos[a] < mid_idx and last_pos[a] > mid_idx:
                    # Add unique palindrome
                    result_set.add((chr(a + ord('a')), mid_char, chr(a + ord('a'))))
        
        # The number of unique palindromes
        return len(result_set)
        
        