from copy import deepcopy
import numpy as np
class Solution:

    def solve(self, i,n, queens, num_q):
        if num_q == n:
            self.solution.append(queens)
            return
        if i==n:
            return

        for j in range(n):
            if not queens[i,j]==-1 and not queens[i,j]==1:
                qu = []
                qu = deepcopy(queens)
                for k in range(n):
                    qu[k][j] = -1
                    qu[i,k] = -1
                k = 1
                while i-k>=0 and j-k>=0:
                    qu[i-k, j-k] = -1
                    k = k+1
                k = 1
                while i+k<n and j+k<n:
                    qu[i+k, j+k] = -1
                    k = k+1
                k = 1
                while i-k>=0 and j+k<n:
                    qu[i-k, j+k] = -1
                    k = k+1
                k = 1
                while i+k<n and j-k>=0:
                    qu[i+k, j-k] = -1
                    k = k+1
                    
                qu[i,j] = 1
                self.solve(i+1, n, qu, num_q+1)
                    

    def solveNQueens(self, n):
        self.solution = []
        self.solve(0, n, np.array([[0]*n]*n), 0)
        if len(self.solution) == 0:
            return []
        else:
            ret = []
            for t in self.solution:
                sol = []
                for i in range(n):
                    s = ""
                    for j in range(n):
                        if t[i,j]==1:
                            s = s+"Q"
                        else:
                            s = s+"."
                    sol.append(s)
                ret.append(sol)

            return ret

sol = Solution()
print(sol.solveNQueens(5))
# k = sol.solveNQueens(10)