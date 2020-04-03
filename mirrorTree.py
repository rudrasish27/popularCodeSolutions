class createTree:
    def __init__(self,data):
        self.data = data;
        self.left = self.right = None
        
def mirrorImage(node):
    # Swap the mirrorImage
    if(node is None):
        return;
    if node.left is not None:
        mirrorImage(node.left)
    elif node.right is not None:
        mirrorImage(node.right)
    
    temp = node.left
    node.left = node.right
    node.right = temp
    # print(node)
    return node
    
def inorder(node): 
    if (not node): 
        return
  
    # first recur on left child  
    inorder(node.left)  
  
    # then print the data of node  
    print(node.data, end = " ")  
  
    # now recur on right child  
    inorder(node.right) 
  
if __name__ == '__main__':
    node = createTree(10);
    node.left = createTree(20);
    node.left.left = createTree(40);
    node.left.right = createTree(60);
    node.right = createTree(30);
    print("Before ====>")
    inorder(node);
    e = mirrorImage(node);
    print("\nAfter ====>")
    inorder(e)
    
    