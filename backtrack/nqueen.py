#User function Template for python3

class Solution:
    def isSafe(self,row,col,board,rows,upd,lowd):
        if upd[row+col] == 1:
            return False
        if lowd[n-1+col-row] == 1:
            return False
        if rows[row] == 1:
            return False
        return True
        
    def nQueenUtils(self,n,col,ans,board,rows,upd,lowd):
        if col > n-1 and -1 not in board:
            ans.append(board.copy())
            # print(type(ans))
            # board = [-1]*n
            return
        for i in range(n):
            if self.isSafe(i,col,board,rows,upd,lowd):
                # print(f"safe {col} , {i}")
                board[col] = i
                # print(f"board: {board}")
                rows[i] = 1
                upd[i+col] = 1
                lowd[n-1+col-i] = 1
                # print(f"lrow: {rows}")
                # print(f"upd: {upd}")
                # print(f"lowd: {lowd}")
                # if ans :
                #     print(f"ans: {ans}")
                self.nQueenUtils(n,col+1,ans,board,rows,upd,lowd)
                board[col] = -1
                rows[i] = 0
                upd[i+col] = 0
                lowd[n-1+col-i] = 0
            # else: print(f"not safe {col} , {i}") 
    def nQueen(self, n):
        # code here
        board = [-1]*n
        ans = []
        rows = [0]*n
        upd = [0]*2*n
        lowd = [0]*2*n
        # print(type(self.nQueenUtils(n,0,ans,board,rows,upd,lowd)))
        
        self.nQueenUtils(n,0,ans,board,rows,upd,lowd)
        # print(ans)
        return ans
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends