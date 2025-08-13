class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # pt=[]
        # if n==1 :return True
        # if n%3==1 or n%3==2: return False
        # for i in range(1,20):
        #     pt.append(3**i)
        # if n in pt : return True
        # return False
        if n<=0: return False
        while n>1:
            if n%3==0: n=n//3
            else:
                return False
        return True