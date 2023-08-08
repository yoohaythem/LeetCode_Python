# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            if (left and right) or ((node == p or node == q) and (left or right)):
                self.result = node  # return node
            return left or right or node == p or node == q

        dfs(root)
        return self.result

    def lowestCommonAncestor2(self, root, p, q):
        if root in (None, p, q):
            return root
        L = self.lowestCommonAncestor(root.left, p, q)
        R = self.lowestCommonAncestor(root.right, p, q)
        return R if not L else L if not R else root
