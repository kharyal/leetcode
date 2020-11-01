class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x = str(x)
        i = 0
        j = len(x)-1
        while i<j:
            # print(x[i], x[j])
            if x[i] == x[j]:
                i = i+1
                j = j-1
            
            else:
                return False
        return True

sol = Solution()
print(sol.isPalindrome(-121)) 
