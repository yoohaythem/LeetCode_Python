# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.result = float("-inf")

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def areamax(node):
            if not node:
                return 0
            left = max(0, areamax(node.left))
            right = max(0, areamax(node.right))
            self.result = max(self.result, left + right + node.val)
            return node.val + max(0, left, right)

        areamax(root)
        return self.result
