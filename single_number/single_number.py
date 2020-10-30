class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xr = 0
        for num in nums:
            xr = xr^num
        
        return xr

sol = Solution()
print(sol.singleNumber([2,2,1]))