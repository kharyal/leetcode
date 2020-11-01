class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n>=2*m:
            return 0
        ret = m
        for num in range(m,n+1):
            ret = ret & num
        return ret

sol = Solution()
print(sol.rangeBitwiseAnd(10,20))