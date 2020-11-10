import numpy as np
from copy import deepcopy
class Solution:
    def solve(self,i,j,visited, path_length):
        if self.grid[i,j]==2:
            if self.num_zeros+1 == path_length:
                self.solution = self.solution+1
            return
        # print(visited)
        for k in [i-1,i+1]:
            vs = deepcopy(visited)
            if k>=0 and k<self.grid.shape[0] and not vs[k,j]==1 and not self.grid[k,j]==-1:
                vs[k,j]=1
                self.solve(k,j,vs, path_length+1)
        
        for k in [j-1,j+1]:
            vs = deepcopy(visited)
            if k>=0 and k<self.grid.shape[1] and not vs[i,k]==1 and not self.grid[i,k]==-1:
                vs[i,k]=1
                self.solve(i,k,vs, path_length+1)
        
    def uniquePathsIII(self, grid):
        self.solution = 0
        self.grid = np.array(grid)
        self.num_zeros = 0
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i,j]==1:
                    start1 = i
                    start2 = j
                if self.grid[i,j]==0:
                    self.num_zeros = self.num_zeros+1
        # print(self.num_zeros)
        visited = np.zeros(self.grid.shape)
        visited[start1, start2]=1
        self.solve(start1, start2, visited,0)
        return self.solution

sol = Solution()
print(sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))