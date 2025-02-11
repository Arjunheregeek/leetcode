'''class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        l = len(part)

        for i in range(len(s)):
            stack.append(s[i])

            if len(stack) >= l and stack[-l:] == list(part):  # Fix: Check if last l characters match `part`
                stack = stack[:-l]  # Fix: Remove last `l` elements
        
        return "".join(stack)  # Fix: Use `"".join(stack)` instead of manually appending to `k`'''
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part,"",1)
        return s
