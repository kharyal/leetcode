class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        A = A
        B = B
        is_neg = False
        
        if A > 2**31-1 or A<-2**31+1:
            return (2**31-1)
        if B == 0:
            return 2**31-1
        if B == 1:
            return A
        if B == -1:
            return -1*A
        if A < 0 or B < 0:
            if A<0:
                A = -1*A
                is_neg = not is_neg
            if B<0:
                B = -1*B
                is_neg = not is_neg
        ret = 0
        while A-B>=0:
            i = 0
            while (A-(B<<(1<<i)))>=0:
                i = i+1
            if i >0:
                i = i-1
            ret = ret+(1<<i)
            A = A - (B<<(i))
            # print(ret)
        if is_neg:
            return -1*ret
        return ret

sol = Solution()
print(sol.divide(-2147483648,-1))