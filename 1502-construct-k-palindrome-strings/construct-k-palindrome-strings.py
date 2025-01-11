class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if len(s) < k:
            return False
        odd = 0
        for char in set(s):
            if s.count(char) % 2:
                odd += 1
        if odd > k:
            return False
        return True