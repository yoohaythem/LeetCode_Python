# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        temp = [root] if root else []
        deep = 0
        while temp:
            deep += 1
            l = len(temp)
            for i in range(l):
                t = temp.pop(0)
                if t.left:
                    temp.append(t.left)
                if t.right:
                    temp.append(t.right)
        return deep

    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0
