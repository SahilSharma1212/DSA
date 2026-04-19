from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_sample_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    return root

root = build_sample_tree()


def serialize(root):
    ans = []
    if root is None:
        return ans
    
    q = deque([root])

    while q:
        qlen = len(q)
        for _ in range(qlen):
            
            node = q.popleft()
            if node is None:
                ans.append("#")
            else:
                ans.append(node.val)
                q.append(node.left)
                q.append(node.right)
    return ans





print(serialize(root))