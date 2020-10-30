from copy import deepcopy
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p1 = deepcopy(nums)
        p2 = deepcopy(nums)

        for i in range(1,len(nums)):
            p1[i] = p1[i-1]*nums[i]
        
        p2[0] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            p2[i] = p2[i+1]*nums[i]

        # print(p1)
        # print(p2)
        for i in range(len(nums)):
            if i==0:
                nums[i] = p2[1]
            
            elif i == len(nums)-1:
                nums[i] = p1[-2]
            
            else:
                nums[i] = p1[i-1]*p2[i+1]

        return nums

sol = Solution()
print(sol.productExceptSelf([0,1]))