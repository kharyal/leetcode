class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ret = ""
        c = 0
        if len(a)>len(b):
            b = "0"*(len(a)-len(b))+b
        elif len(b)>len(a):
            a = "0"*(len(b)-len(a))+a

        for i in range(len(a)-1,-1,-1):
            A = int(a[i])
            B = int(b[i])
            sum_int = A+B+c

            if sum_int==0:
                ret = "0" + ret
                c = 0
            elif sum_int == 1:
                ret = "1" +ret
                c = 0
            elif sum_int == 2:
                ret = "0" +ret
                c = 1
            elif sum_int == 3:
                ret = "1" +ret
                c = 1
        if c == 1:
            ret = "1"+ret
        return ret

sol = Solution()
print(sol.addBinary("1010", "1011"))     
