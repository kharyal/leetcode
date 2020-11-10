class Solution:
    def bin_search(self, num, start, end):
        if start==end:
            return start
        mid = (start+end)//2

        # print(start, end, mid)
        if mid*mid == num or (mid*mid<num and (mid+1)*(mid+1)>num):
            return mid
        elif mid*mid>num:
            return self.bin_search(num, start, mid)
        else:
            return self.bin_search(num, mid+1, end)

    def mySqrt(self, x: int) -> int:
        return self.bin_search(x, 1, x)

sol = Solution()
print(sol.mySqrt(67))