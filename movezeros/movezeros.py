def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    ret = []
    zeros_count = 0
    for num in nums:
        if num == 0:
            zeros_count = zeros_count+1
        else:
            ret.append(num)
    for num_zero in range(zeros_count):
        ret.append(0)    
    nums = ret
    return nums

print(moveZeroes([0,1,0,3,12]))