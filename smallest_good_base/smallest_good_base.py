import math
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        m_max = int(math.log(n,2))

        for m in range(m_max, 1, -1):
            k = int(n**(1/m))
            if (k**(m+1) -1) == n*(k-1):
                return str(k)

        return str(n-1)

sol = Solution()
print(sol.smallestGoodBase("13"))