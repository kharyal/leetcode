class Solution(object):

    def binary_search(self, arr, num, start, end):
        if len(arr)==0:
            return -1

        if end == start and arr[start]==num:
            return start
        elif end == start:
            return -1

        if end<start: 
            return -1
        
        mid = (start+end)//2
        if num == arr[mid]:
            return mid
        elif num<arr[mid]:
            return self.binary_search(arr, num, start, mid)
        else:
            return self.binary_search(arr, num, mid+1, end)

    def find_rot_index(self, nums, start, end):
        if end==start:
            return start
        mid = (start+end)//2+1
        if (mid>0 and mid<len(nums)-1) and nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] < nums[start]:
            return self.find_rot_index(nums, start, mid-1)
        elif nums[mid] > nums[end]:
            return self.find_rot_index(nums, mid, end)
        elif nums[mid] >= nums[start] and nums[mid] <= nums[end]:
            return end

    def unrotate(self, nums):
        rot_ind = self.find_rot_index(nums, 0, len(nums)-1)
        # print(rot_ind)
        l = len(nums)
        i = (rot_ind + 1)%l
        ret = []
        while not i == rot_ind:
            ret.append(nums[i])
            i = (i+1)%l
        ret.append(nums[rot_ind])
        return ret, rot_ind

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums, rot_ind = self.unrotate(nums)
        ind = self.binary_search(nums, target, 0, len(nums)-1)
        if not ind == -1:
            return (ind + (rot_ind+1)%len(nums))%len(nums)
        return ind

sol = Solution()
print(sol.search([4,5,6,7,0,1,2],1))