class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digits = []
        max_iters = 100
        i = 0
        while i<max_iters:
            i = i+1
            if n == 4:
                return False
            if n==1:
                return True
            while n>0:
                digits.append(n%10)
                n = n//10
            # print(digits)
            power = 1
            n = 0
            for digit in digits:
                n = n + digit**2
                power = power*10

            digits = [] 

sol = Solution()
print(sol.isHappy(2699))