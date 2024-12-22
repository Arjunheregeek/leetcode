class Solution:
    def scoreOfString(self, s: str) -> int:
        total_diff = 0
        for i in range(1, len(s)):
            total_diff += abs(ord(s[i]) - ord(s[i - 1]))
        return total_diff

solution = Solution()
s = "hello"
result = solution.scoreOfString(s)
print(result)
s = "zaz"
result = solution.scoreOfString(s)
print(result)