class Solution:
    def similarPairs(self, words: List[str]) -> int:
        c=0
        for i in  range (len(words)):
            for j in  range(i+1,len(words)):
                if set(words[i]).issubset(set(words[j])) and set(words[j]).issubset(set(words[i])):
                    c+=1
        return c 

        