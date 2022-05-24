class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
        



class Solution:

    #Function to find out minimum steps Knight needs to reach target position.
    def possible_moves(self, KnightPos, N):
        x = KnightPos[0]
        y = KnightPos[1]
        
        possible = [(x-2,y-1),(x-2,y+1),(x+2,y-1),(x+2,y+1),(x-1,y-2),(x+1,y-2),(x-1,y+2),(x+1,y+2)]
        
        for i in possible:
            if i[0] < 1 or i[0] >N or i[1] <0 or i[1] > N:
                possible.remove(i)
                print("removed" , i)
        print("possibe : " ,possible)
        return possible
        
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        #Code here
        visited = set()
        KnightPos = tuple(KnightPos)
        print(KnightPos)
        visited.add(KnightPos)
        print(visited)
        curr = KnightPos
        level = 1
        curr_children = self.possible_moves(curr,N)
        while TargetPos not in curr_children: 
            nextChildren = []
            children = curr_children
            print(children)
            for child in children:
                if child not in visited:
                    visited.add(child)
                    temp = self.possible_moves(child,N)
                    if TargetPos in temp:
                        return(level+1)
                    nextChildren.append(temp)
            curr_children = nextChildren
            level +=1
        return level
                
#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        KnightPos = list(map(int, input().split()))
        TargetPos = list(map(int, input().split()))
        obj = Solution()
        ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
        print(ans)

# } Driver Code Ends