class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        arr = [1]*(A+1)
        ret1 = []
        ret1_num = []
        for i in range(2,len(arr)):
            if arr[i]==1:
                j = 2
                while i*j<=A:
                    arr[i*j] = 0
                    j = j+1
                if A%i == 0:
                    ret1.append(i)
                    ret1_num.append(0)
                temp = A
                while temp%i==0:
                    ret1_num[-1] = ret1_num[-1]+1
                    temp = temp//i

        
        arr = [1]*(B+1)
        ret2 = []
        for i in range(2,len(arr)):
            if arr[i]==1:
                j = 2
                while i*j<=B:
                    arr[i*j] = 0
                    j = j+1
                if B%i == 0:
                    ret2.append(i)
                temp = B
                while temp%i==0:
                    temp = temp//i
        
        ret = 1

        for i,num1 in enumerate(ret1):
            if not num1 in ret2:
                ret = ret*(num1**ret1_num[i])

        return ret


sol = Solution()
print(sol.cpFact(35,12)) 