# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sum = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def grade(node):
            if not node:
                return 0
            left = grade(node.left)
            right = grade(node.right)
            self.sum += abs(left - right)
            return left + right + node.val
        grade(root)
        return self.sum