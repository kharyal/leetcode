from copy import deepcopy
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 0
        max_ending_here = 0
        for i in range(len(nums)):
            max_ending_here = max_ending_here + nums[i]             
            if max_ending_here<0:
                max_ending_here = 0
            if max_ending_here>max_sum:
                max_sum = max_ending_here
        
        for num in nums:
            if num>0:
                return max_sum

        min_neg = nums[0]
        for num in nums:
            if num > min_neg:
                min_neg = num
        
        return min_neg

sol = Solution()
print(sol.maxSubArray([-1]))