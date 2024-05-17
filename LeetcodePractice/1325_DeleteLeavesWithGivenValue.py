'''
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.left == None and root.right == None and root.val == target:
            root = None
            return None
        root.left = self.removeLeafNodes(root.left , target)
        root.right = self.removeLeafNodes(root.right , target)
        if root.left == None and root.right == None and root.val == target:
            root = None
            return None
        return root