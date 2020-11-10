from copy import deepcopy
class Solution:
    def check_palindrome(self,string):
        i = 0
        j = len(string)-1
        while i<j:
            if not string[i] == string[j]:
                return False
            i = i+1
            j = j-1
        return True

    def solve(self, i, partitions):
        if i==len(self.s):
            check = ""
            # print(partitions)
            for p in partitions:
                check = check+p
            if check==self.s:  
                self.solution.append(partitions)
            else:
                return
        
        for j in range(i+1, len(self.s)+1):
            # print(i,j)
            pa = deepcopy(partitions)
            # print(self.s[i:j], self.check_palindrome(self.s[i:j]))
            if self.check_palindrome(self.s[i:j]):
                pa.append(self.s[i:j])
                self.solve(j, pa)
            

    def partition(self, s):
        self.s = s
        self.solution = []
        self.solve(0,[])
        return self.solution
    
sol = Solution()
print(sol.partition("hahaha"))