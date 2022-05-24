#User function Template for python3

class Solution:
    def valid_moves(self,n,curr):
        moves = [(curr[0]-1,curr[1]),(curr[0]+1,curr[1]),(curr[0],curr[1]+1),(curr[0],curr[1]-1)]
        for move in moves:
            if move[0] < 1 or move[0] >n or move[1] <0 or move[1] > n:
                moves.remove(move)
        return moves
    
    
    def findPath(self, m, n):
        curr = (0,0)
        pos_moves = [[move]for move in self.valid_moves(n,curr) ]
        if m[n-1][n-1] == 0:
            
            return
        print(pos_moves)
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends