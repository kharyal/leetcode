class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        power = 2**31
        ret = 0
        for i in range(32):
            ret = ret+ power*(A%2)
            A = A>>1
            power = power/2
    
        return int(ret)

sol = Solution()
print(sol.reverse(3))