class Solution:
    def stringHash(self, s: str, k: int) -> str:
       
        arr = [ord(ch)-97 for ch in s]
        
        return ''.join([ascii_lowercase[sum(arr[i:i+k])%26] 
                                for i in range(0, len(arr), k)])