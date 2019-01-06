# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal = []
        stack = []
        curr = root
        while curr != None or len(stack) != 0:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            traversal.append(curr.val)
            curr = curr.right
        return traversal