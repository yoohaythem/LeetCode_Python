# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
        return check(root.left, root.right)

    def isSymmetric2(self, root):
        queue = [root, root]
        while queue:
            left = queue.pop()
            right = queue.pop()
            if left is None and right is None:
                continue
            if left is None or right is None or left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True
