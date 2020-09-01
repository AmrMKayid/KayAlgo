# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

  def isValidBST(self, root):
    """
        :type root: TreeNode
        :rtype: bool
        """
    if not root:
      return True

    def isBST(node, lower, upper):
      if lower is not None and node.val <= lower:
        return False
      if upper is not None and upper <= node.val:
        return False

      left = isBST(node.left, lower, node.val) if node.left else True
      if left:
        right = isBST(node.right, node.val, upper) if node.right else True
        return right
      else:
        return False

    return isBST(root, None, None)
