class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_zeros = 0
        for num in range(0,n+1,5):
            if num == 0:
                continue
            while num%5==0:
                num_zeros = num_zeros+1
                num = num//5
        
        return num_zeros

sol = Solution()
print(sol.trailingZeroes(1000))