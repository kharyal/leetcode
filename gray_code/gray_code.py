from copy import deepcopy
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self,i,n, string, reverse = False):
        # print(i)
        self.solution.append("".join(string))
        if not reverse:
            for j in range(i,n):
                if string[j]=="0":
                    string1 = deepcopy(string)
                    string1[j]="1"
                    self.solve(j, n, string1, reverse)
        
        # else:
        #     for j in range(n-1, i-1, -1):
        #         if string[j]=="0":
        #             string1 = deepcopy(string)
        #             string1[j]="1"
        #             self.solve(j, n, string1, reverse)

    def grayCode(self, A):
        ret = []
        i = 0
        while i<2**A:
            ret.append(i^(i>>1))
            i = i+1
        return ret

sol = Solution()
print(sol.grayCode(20))

'''
#   000
#   100
#   110
#   111
  101  011  
  001     001
  010     101
       111
#   010
#   011
#   001
#   101
#   111

11^01
10^01
11

00^00 = 00
01^00 = 01
10^01 = 11
11^01 = 10

000^000 = 000
001^000 = 001
010^001 = 011
011^001 = 010
100^010 = 110
101^010 = 111
110^011 = 101
111^011 = 100
'''

