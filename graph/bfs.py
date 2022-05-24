#User function Template for python3
from collections import deque
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        ans = []
        visited = [False]*V
        visited[0] = True
        queue = list()
        queue.append(0)
        
        while queue:
            s = queue.pop(0)
            ans.append(s)
            for i in adj[s] :
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
            
            
        
        return(ans)
        
#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
        

# } Driver Code Ends