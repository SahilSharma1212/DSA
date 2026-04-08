from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = TreeNode(0)
left = TreeNode(1)
right = TreeNode(2)
root.left = left
root.right = right

leftLeft = TreeNode(3)
leftRight = TreeNode(4)


rightLeft = TreeNode(5)
rightRight = TreeNode(6)

right.left = rightLeft
right.right = rightRight

left.left = leftLeft
left.right = leftRight

# PREORDER
def preorder(root):
    if root == None:
        return

    print(f"{root.val}, ", end="")
    preorder(root.left)
    preorder(root.right)


# POSTORDER
def postorder(root):
    if root == None:
        return

    postorder(root.left)
    postorder(root.right)
    print(f"{root.val}, ", end="")

# INORDER
def inorder(root):
    if root == None:
        return

    inorder(root.left)
    print(f"{root.val}, ", end="")
    inorder(root.right)

def levelOrder(root):
    if root is None:
        return
    
    q = deque()
    deque.append(root)
    res = []

    
    while q:
        curr = q.popleft()
        res.append(curr.val)

        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)


def height(root):
    if root is None:
        return -1   # if counting edges
        # return 0  # if counting nodes
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    return 1 + max(left_height, right_height)

def diameterWithHeight(root):
    if root is None:
        return 0

    def helper(root):
        if root is None:
            return 0
        
        leftHt, leftDia = helper(root.left)
        rightHt, rightDia = helper(root.right)

        currDia = leftHt + rightHt

        dia = max(currDia, leftDia, rightDia)
        ht = 1 + max(leftHt, rightHt)
        return ht, dia
    
    return helper(root)[1]

def diameter(root):
    if root is None:
        return 0
    
    # diameter passing through root
    left_h = height(root.left)
    right_h = height(root.right)
    curr_d = left_h + right_h
    
    # diameter in subtrees
    left_d = diameter(root.left)
    right_d = diameter(root.right)
    
    return max(curr_d, left_d, right_d)

def balancedBinaryTree(root):

    leftHt = height(root.left)
    rightHt = height(root.right)

    if -1 <= rightHt - leftHt <= 1:
        return True
    else:
        return False

maxi = [float('-inf')]
def maxPathSum(root):
    if root is None:
        return 0
    
    leftSum = maxPathSum(root.left)
    if leftSum < 0:
        leftSum = 0

    rightSum = maxPathSum(root.right)
    if rightSum < 0:
        rightSum = 0

    maxi[0] = max(maxi[0], leftSum + rightSum + root.val)
    return root.val + max(leftSum, rightSum)

def zigzag(root):
    leftToRight = True
    q = deque([root])
    ans = []
    while q:
        qlen = len(q)
        tempArr = []

        # pop current level
        for i in range(qlen):
            node = q.popleft()
            tempArr.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        # apply zigzag
        if not leftToRight:
            tempArr.reverse()

        ans.extend(tempArr)

        leftToRight = not leftToRight
    return ans


def topView(root):
    if root is None:
        return []
    mp = {}
    q = deque([[root, 0]])
    ans = []
    while q:
        node, hd = q.popleft()
        if hd not in mp:
            mp[hd] = node.val
            
        if node.left:
            q.append([node.left, hd - 1])
            
        if node.right:
            q.append([node.right, hd + 1])

    for el in sorted(mp):
        ans.append(mp[el])
    return ans


def bottomView(root):
    if root is None:
        return []
    mp = {}
    q = deque([[root, 0]])
    ans = []
    while q:
        node, hd = q.popleft()
        if hd not in mp:
            mp[hd] = node.val
        else:
            mp[hd] = node.val
            
        if node.left:
            q.append([node.left, hd - 1])
            
        if node.right:
            q.append([node.right, hd + 1])

    for el in sorted(mp):
        ans.append(mp[el])
    return ans

def leftRighView(root):
    if root is None:
        return [], []

    leftviewans = []
    rightviewans = []
    q = deque([root])
    while q:
        qlen = len(q)
        tempArr = []
        for _ in range(qlen):
            currnode = q.popleft()
            if currnode.left:
                q.append(currnode.left)
            if currnode.right:
                q.append(currnode.right)
            tempArr.append(currnode.val)
        leftviewans.append(tempArr[0])
        rightviewans.append(tempArr[-1])

    return leftviewans, rightviewans


def find_path(root, target, path):
    if not root:
        return False

    # add current node
    path.append(root.val)

    # check if target found
    if root.val == target:
        return True

    # search left or right
    if find_path(root.left, target, path) or find_path(root.right, target, path):
        return True

    # backtrack
    path.pop()
    return False


def lca(root, t1, t2):
    if root is None:
        return None
    
    if root.val == t1 or root.val == t2:
        return root
    
    
    leftFoundRoot = lca(root.left, t1, t2)
    
    rightFoundRoot = lca(root.right, t1, t2)

    if leftFoundRoot and rightFoundRoot:
        return root
    elif leftFoundRoot:
        return leftFoundRoot
    elif rightFoundRoot:
        return rightFoundRoot
    else:
        return None


def widthOfTree(root):
    if root is None:
        return 0
    maxi = float("-inf")
    q = deque([root, 0])

    while q:
        qlen = len(q)
        firstIndex = q[0][1]
        lastIndex = q[-1][1]

        maxi = max(maxi, abs(firstIndex - lastIndex))
        for _ in range(qlen):
            currNode, currIndex = q.popleft()

            # normalize index to avoid large numbers
            index -= firstIndex

            if currNode.left:
                q.append(currNode.left, 2*currIndex)

            if currNode.right:
                q.append(currNode.right, 2*currIndex + 1)



print("Preorder: ")
preorder(root)
print('\n')
print("Inorder: ")
inorder(root)
print('\n')
print("Postorder: ")
postorder(root)
print("\n")

maxPathSum(root)

print(f"Balanced ? \n{balancedBinaryTree(root)}\n")

print(f"maxPathSum: {maxi[0]}")

print(f"zigzag order: {zigzag(root)}")

print(f"topView : {topView(root)}")

print(f"bottomView : {bottomView(root)}")

leftviewans, rightviewans = leftRighView(root)
print(f"leftView : {leftviewans}")
print(f"rightView : {rightviewans}")


print(lca(root, 3, 4).val)