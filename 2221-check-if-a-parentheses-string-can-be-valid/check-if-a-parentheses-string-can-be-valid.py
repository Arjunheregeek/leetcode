class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)

        # If length of the string is odd, it's impossible to balance
        if n % 2 != 0:
            return False
        
        # First pass: Validate from left to right
        open_count = 0  # Count of unmatched '(' or potential '('
        for i in range(n):
            if s[i] == "(" or locked[i] == "0":  # '(' or unlocked
                open_count += 1
            else:  # Locked ')'
                open_count -= 1
            if open_count < 0:  # More ')' than possible '('
                return False

        # Second pass: Validate from right to left
        close_count = 0  # Count of unmatched ')' or potential ')'
        for i in range(n - 1, -1, -1):
            if s[i] == ")" or locked[i] == "0":  # ')' or unlocked
                close_count += 1
            else:  # Locked '('
                close_count -= 1
            if close_count < 0:  # More '(' than possible ')'
                return False

        return True
