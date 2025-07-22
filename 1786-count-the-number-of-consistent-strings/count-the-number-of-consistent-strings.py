class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Create the set of allowed characters once, outside the loop.
        allowed_set = set(allowed)
        consistent_count = 0

        for word in words:
            # Use the all() function with a generator expression.
            # It efficiently checks if all characters in the word are in the allowed_set.
            if all(char in allowed_set for char in word):
                consistent_count += 1

        return consistent_count