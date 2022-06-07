from dataclasses import dataclass


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def createNode(val):
    newNode = Node(0)
    newNode.val = val
    newNode.left = None
    newNode.right = None
    return newNode

def inorder(root):
    if (root == None):
        return
    inorder(root.left)
    print( root.val, end = " ")
    inorder(root.right)  

        
def mirrorify(root:Node,mirror):
    if root == None:
        return None
    que  = list()
    que.append(root)
    print(root.data)
    while que:
        temp = que.pop(0)
        # print(temp)
        if temp != None:
            temp.left , temp.right = temp.right , temp.left
            que.append(temp.left)
            que.append(temp.right)
         
if __name__=='__main__':
 
    tree = createNode(5)
    tree.left = createNode(3)
    tree.right = createNode(6)
    tree.left.left = createNode(2)
    tree.left.right = createNode(4)
 
    # Print inorder traversal of the input tree
    print("Inorder of original tree: ")
    inorder(tree)
    mirror = None
    mirror = mirrorify(tree, mirror)
 
    # Print inorder traversal of the mirror tree
    print("\nInorder of mirror tree: ")
    inorder(tree)
    

        
    
        