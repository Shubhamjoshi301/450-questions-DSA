class Solution:
    
    def __init__(self):
        self.count = 0
    
    #Function to find minimum time required to rot all oranges. 
    def canRott(self, grid, i,j):
        if (i-1 >= 0 and grid[i-1][j] ==2) or (i+1 < len(grid) and grid[i+1][j] ==2) or (j-1 >= 0 and grid[i][j-1] ==2) or (j+1 < len(grid[0]) and grid[i][j+1] ==2):
            return True
        return False
        
    
    def isIsolated(self, grid, i,j):
        if (i-1 >= 0 and grid[i-1][j] ==0) and (i+1 < len(grid) and grid[i+1][j] ==0) and (j-1 >= 0 and grid[i][j-1] ==0) and (j+1 < len(grid[0]) and grid[i][j+1] ==0):
            return True
        return False
    
    
    
    def orangesRotting(self, grid):
        
        #Code here
        
        
        stack = []
        ans= []
        for row in grid:
            set1 = set(row)
            if 1 in set1:
                break
            return 0
                
                
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    stack.append([i,j])
                    
                    
        for orange in stack:
            if self.isIsolated(grid, orange[0] ,orange[1]):
                return -1
        
        while stack:
            # print(grid)
            print(stack)
            for orange in stack:
                
                if self.canRott(grid,orange[0],orange[1]):
                    print("can rot ",orange)
                    stack.remove(orange)
                    ans.append(orange)
                    
                    
            for orange1 in ans:
                grid[orange1[0]][orange1[1]] = 2
                ans.remove(orange1)
    
            self.count += 1
        
        return self.count
        
#{ 
#  Driver Code Starts
from queue import Queue

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.orangesRotting(grid)
        print(ans)

# } Driver Code Ends