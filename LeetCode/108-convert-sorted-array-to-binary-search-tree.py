# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def BST(left, right):
            if left > right:
                return None
            
            middle = (left + right) // 2
            
            root = TreeNode(nums[middle])
            root.left = BST(left, middle - 1)
            root.right = BST(middle + 1, right)
            
            return root
        
        return BST(0, len(nums) - 1)