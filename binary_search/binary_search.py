class Solution():
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

sol = Solution()
print(sol.binary_search([1,2,3,4,7,9,10], 9, 0, 6))