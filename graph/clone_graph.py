"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = set()
        stack = []
        s = Node(node.val,node.neighbors)
        # visited.add(s.val)
        stack.append(s)
        # ans = {s.val:s.neighbours}
        ans = dict()
        while (len(stack)):
            t = stack[-1]
            stack.pop()
            
            if t.val not in visited:
                ans[t.val] = t.neighbors
                visited.add(t.val)
                
            for neig in t.neighbors:
                if neig.val not in visited:
                    temp = Node(neig.val,neig.neighbors)
                    stack.append(temp)
                    
        return s