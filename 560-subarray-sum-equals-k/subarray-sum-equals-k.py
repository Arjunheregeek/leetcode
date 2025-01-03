class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        summ = 0
        count = 0
        for i in nums:
            summ += i
            if summ - k in dic:
                count += dic[summ - k]
            if summ in dic:
                dic[summ] += 1
            else:
                dic[summ] = 1
        return count
