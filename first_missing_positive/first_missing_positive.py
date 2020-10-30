class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [0]*301
        for num in nums:
            if num>0 and num<=300:
                a[num] = 1

        for i in range(1,len(a)):
            if a[i] == 0:
                return i

sol = Solution()
print(sol.firstMissingPositive([7,8,9,11,12]))