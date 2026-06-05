class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        x=math.log(n)/math.log(2)
        return abs(x-round(x))<1e-10
        