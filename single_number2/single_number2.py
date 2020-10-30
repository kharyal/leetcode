class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        power = 1
        nums = nums
        for i in range(len(nums)):
            nums[i] = nums[i]+2**31

        for j in range(32):
            xr = 0 
            for i in range(len(nums)):
                m = nums[i]%2
                # print(nums[i], end=" ")
                if not(j == 0 or j==31) and nums[i]==-1:
                    continue
                nums[i] = nums[i]//2
                
                xr = xr + m
                # print("\n")
            ret = ret+power*(xr%3)
            power = power*2

        return (ret-2**31)

sol = Solution()
print(sol.singleNumber([0,1,0,1,0,1,-1]))        