class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        
        ans = []
        count = 1
        
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:  # Increment count for consecutive characters
                count += 1
            else:
                ans.append(chars[i - 1])  # Append character
                if count > 1:
                    ans.extend(list(str(count)))  # Append count if greater than 1
                count = 1  # Reset count
        
        # Handle the last character sequence
        ans.append(chars[-1])
        if count > 1:
            ans.extend(list(str(count)))
        
        chars.clear()  # Update the original list
        chars.extend(ans)
        
        return len(chars)
