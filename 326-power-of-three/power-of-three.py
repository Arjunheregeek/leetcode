class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        base3 = ""
        while n > 0:
            base3 = str(n % 3) + base3
            n //= 3
        return bool(re.match(r"^10*$", base3))