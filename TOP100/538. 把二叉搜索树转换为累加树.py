# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        sum = 0
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            node.val += sum
            sum = node.val
            node = node.left
        return root
