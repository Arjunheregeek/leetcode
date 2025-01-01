class Solution:
    def maxScore(self, s: str) -> int:
        n=len(s)

        left = [0] *(n+1)

        right = [0] * (n+1)

        for i in range(1, len(s)):

            if s[i - 1] == "0":
                left[i] = left[i - 1] + 1
            else:
                left[i]=left[i-1]
        

        for j in range(len(s) - 2, -1, -1):

            if s[j + 1] == "1":
                right[j+1] = right[j +2] + 1
            else:
                right[j+1]= right[j+2]
        

        
        for i in range(len(s)):
            left[i] = left[i] + right[i]
        return max(left)
