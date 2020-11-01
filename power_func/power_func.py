class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if A == 0:
            return 0
        ret = 1
        while B>0:
            if B%2:
                ret = (ret*A)%C

            A = (A*A)%C
            B = B//2
        
        return ret

sol = Solution()
print(sol.pow(2,3,3))