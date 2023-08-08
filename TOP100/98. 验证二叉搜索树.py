class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        stack = []
        while root or len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if len(result) != 0 and root.val <= result[-1]:
                return False
            result.append(root.val)
            root = root.right
        return True

    def isValidBST2(self, root):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if node is None:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            if not helper(node.left, lower, node.val):
                return False
            if not helper(node.right, node.val, upper):
                return False
            return True
        return helper(root)
