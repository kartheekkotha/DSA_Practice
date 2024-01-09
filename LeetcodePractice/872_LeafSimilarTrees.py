# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        self.helper(root1, arr1)
        self.helper(root2, arr2)
        if(len(arr1)!= len(arr2)):
            return False
        for i in range(len(arr1)):
            if(arr1[i] != arr2[i]):
                return False
        return True
    def helper(self, root1: Optional[TreeNode], array):
        if(root1 == None):
            return
        if(root1.left == None and root1.right == None):
            array.append(root1.val)
            return 
        self.helper(root1.left , array)
        self.helper(root1.right , array)
        return 


 