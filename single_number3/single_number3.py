class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            nums[i] = nums[i]+2**31

        # print(nums)

        ret = 0
        for num in nums:
            ret = ret^num
        
        for j in range(32):
            m = ret%2
            if m==1:
                break
            
            ret = ret//2
        
        a1 = []
        a0 = []

        for num in nums:
            if (num>>(j))%2 == 1:
                a1.append(num)
            else:
                a0.append(num)
        
        # print(a0)
        # print(a1)

        ret1 = 0
        ret2 = 0

        for num in a1:
            ret1 = ret1^num

        for num in a0:
            ret2 = ret2^num

        return [ret1 - 2**31, ret2 - 2**31]


sol = Solution()
print(sol.singleNumber([0,1])) 