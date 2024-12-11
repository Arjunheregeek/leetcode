class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        k=Counter(arr)
        s= list(k.values())
        s.sort()
        j=0
        for i in range(1,len(s)):

            j=i-1
            if s[i]==s[j]:
                return False
        return True



        