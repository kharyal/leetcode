from copy import deepcopy
class Solution:
    def minSubArrayLen(self, s, nums):
        if len(nums)==0:
            return 0
        min_sz_till_now = deepcopy(nums)
        sum_till_now = deepcopy(nums)

        for i in range(len(min_sz_till_now)):
            min_sz_till_now[i] = -1
            sum_till_now[i] = -1

        sum_till_now[0] = nums[0]
        min_sz_till_now[0] = 1
        j = 0
        for i in range(1, len(nums)):
            sum_till_now[i] = sum_till_now[i-1]+nums[i]
            min_sz_till_now[i] = min_sz_till_now[i-1]+1
            while sum_till_now[i] - nums[j]>=s:
                sum_till_now[i] = sum_till_now[i] - nums[j]
                j = j+1
                min_sz_till_now[i] = min_sz_till_now[i]-1
        
        MIN_SZ = float('inf')
        for i in range(0, len(nums)):
            if sum_till_now[i]>=s and min_sz_till_now[i]<MIN_SZ:
                MIN_SZ = min_sz_till_now[i]
        if MIN_SZ == float('inf'):
            return 0 
        return MIN_SZ

sol = Solution()
print(sol.minSubArrayLen(100,[]))
