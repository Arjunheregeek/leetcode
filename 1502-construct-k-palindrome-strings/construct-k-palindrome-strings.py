class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True

        odd = 0

        for chr in s:
            odd ^= (1 << (ord(chr) - ord('a')))

        return bin(odd).count('1') <= k