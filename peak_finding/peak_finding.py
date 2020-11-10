class Solution(object):
    def find_peak(self, nums, start, end, l):
        if start == end:
            return start
        
        mid = (start+end)//2+1
        if (mid>0) and nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif mid>0 and nums[mid-1]>nums[mid]:
            return self.find_peak(nums, start, mid-1,l)
        elif nums[mid+1]>nums[mid]:
            return self.find_peak(nums, mid, end, l)
        

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        nums.append(-float('inf'))
        return self.find_peak(nums, 0, l-1, l)

sol = Solution()
print(sol.findPeakElement([1]))
