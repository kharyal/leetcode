def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums = sorted(nums)
    ret = []
    k = len(nums)-1
    while k > 0:
        num = nums[k]
        i = 0; j = k-1
        while i<j:
            if nums[i]+nums[j] > -num:
                j = j-1
            elif nums[i]+nums[j] < -num:
                i = i+1
            else:
                ret.append([num, nums[i], nums[j]])
                sel_num = nums[i]
                while sel_num == nums[i] and i<j:
                    i = i+1
                sel_num = nums[j]
                while sel_num == nums[j] and i<j:
                    j = j-1
        while k>=0 and nums[k] == num:
            nums.pop(k)
            k = k-1
    return ret


print(threeSum([0,0]))