# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):  # 0：不选中；1：选中
            if not node:
                return 0, 0
            left = dfs(node.left)
            right = dfs(node.right)
            selected = left[0] + right[0] + node.val
            unselected = max(left) + max(right)
            return unselected, selected

        return max(dfs(root))
