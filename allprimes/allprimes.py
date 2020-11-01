class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        arr = [1]*(A+1)
        ret = []
        for i in range(2,len(arr)):
            if arr[i]==1:
                j = 2
                while i*j<=A:
                    arr[i*j] = 0
                    j = j+1
                ret.append(i)

        return ret


sol = Solution()
print(sol.sieve(123)) 
