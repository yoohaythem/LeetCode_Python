# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        def rootSum(node, targetSum):
            if not node:
                return 0
            ret = 0
            if node.val == targetSum:
                ret += 1
            ret += rootSum(node.left, targetSum - node.val)
            ret += rootSum(node.right, targetSum - node.val)
            return ret

        if not root:
            return 0
        ret = rootSum(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret
