# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traversal(root, [])
    
    def traversal(self, root, result):
        if not root:
            return []
        
        self.traversal(root.left, result)
        result.append(root.val)
        self.traversal(root.right, result)

        return result