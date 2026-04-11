class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

inorder = [4, 2, 5, 1, 6, 3]

preorder = [1, 2, 4, 5, 3, 6]

def inpretoBinTree(inorder, preorder):
    # Base case
    if not inorder or not preorder:
        return None
    
    
    # Root is the first element in preorder
    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find root index in inorder traversal
    valIndex = inorder.index(root_val)

    root.left = inpretoBinTree(inorder[:valIndex], preorder[1:valIndex+1])
    root.right = inpretoBinTree(inorder[valIndex+1:], preorder[valIndex+1:])

    return root


# PREORDER
def pre(root):
    if root == None:
        return

    print(f"{root.val}, ", end="")
    pre(root.left)
    pre(root.right)

root = inpretoBinTree(inorder, preorder)

pre(root)