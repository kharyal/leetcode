import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    def gcd(self, A, B):
        if A == 0:
            return B
        if B == 0:
            return A
        if A == 1 or B == 1:
            return 1 
        if A%2 == 0:
            if not B%2==0:
                return self.gcd(A//2, B)
            else:
                return 2*self.gcd(A//2, B//2)
        
        if B%2 == 0:
            return self.gcd(A, B//2)
        
        if A>B:
            return self.gcd((A-B)//2, B)
        
        return self.gcd((B-A)//2, A)

    def cpFact(self, A, B):
        
        i = 2
        while i < A+1:
            g = math.gcd(A,B)
            if g == 1:
                return A
            else:
                A = A//g


sol = Solution()
print(sol.cpFact(30,12)) 