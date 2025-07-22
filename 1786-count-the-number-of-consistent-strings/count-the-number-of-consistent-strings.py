class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Renamed 'i' to 'allowed_set' for clarity
        allowed_set = set(allowed)
        
        # Renamed 'c' to 'count'
        count = 0
        
        # Renamed 'j' to 'word'
        for word in words:
            word_set = set(word)
            
            # This is the key change. issubset() directly checks if all
            # elements of word_set are present in allowed_set.
            # It's more readable than checking if the difference is an empty set.
            if word_set.issubset(allowed_set):
                count += 1
                
        return count