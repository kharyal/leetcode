class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        
        # i = 0
        # X = max(A)
        # while X>0:
        #     X = X>>1
        #     i = i+1

        # num = 2**i
        # arr = [0]
        # highest2pow = 1
        # next_highest2pow = 2
        # for number in range(1, num+1):
        #     if number == 1:
        #         arr.append(1)
        #     elif number == 2:
        #         arr.append(1)
        #         highest2pow = 2
        #         next_highest2pow = highest2pow*2
        #     else:
        #         # print(number, number%highest2pow)
        #         arr.append(arr[number%highest2pow]+arr[highest2pow])

        #         if number%next_highest2pow == 0:
        #             highest2pow = next_highest2pow
        #             next_highest2pow = highest2pow*2
        arr = [-1]*1000000
        ret = 0
        for i in range(1,len(A)):
            for j in range(i+1):
                # print(arr[A[i]^A[j]], A[i], A[j])
                n = A[i]^A[j]
                if n < len(arr) and not arr[n]==-1:
                    count = arr[n]
                else:    
                    count = 0
                    while n>0:
                        n = n&(n-1)
                        count = count+1
                    if A[i]^A[j]<len(arr):
                        arr[A[i]^A[j]] = count

                ret = (ret+count)%(1e9+7)

        return int(2*ret)

sol = Solution()
print(sol.cntBits([2,2,2]))