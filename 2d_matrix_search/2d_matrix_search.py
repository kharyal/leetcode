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
    
    # def col_search(self, matrix, start, end, target):
    #     if len(matrix)==0:
    #         return False
    #     if len(matrix[0])==0:
    #         return False
    #     mid = ((start+end)//2 + 1)%len(matrix)
    #     # print(start, end, mid)
    #     # exit()
    #     if start == end:
    #         mid = start
    #     l = len(matrix[mid])
        
    #     if not self.binary_search(matrix[mid], target, 0, (l-1)%l) == -1:
    #         return True
    #     if start == end:
    #         return False
    #     if matrix[mid][l//2]>target:
    #         return self.col_search(matrix, start, mid-1, target)
    #     else:
    #         return self.col_search(matrix, mid, end, target)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # print(len(matrix))
        if len(matrix)==0:
            return False
        if len(matrix[0])==0:
            return False
        for i in range(len(matrix)):
            if matrix[i][-1]>=target and matrix[i][0]<=target:
                if not self.binary_search(matrix[i], target, 0, len(matrix[i])-1)==-1:
                    return True

        return False        

sol = Solution()
print(sol.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 99))        