# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        temp = [root] if root else []
        result = []
        while temp:
            l = len(temp)
            r = []
            for i in range(l):
                t = temp.pop(0)
                r.append(t.val)
                if t.left:
                    temp.append(t.left)
                if t.right:
                    temp.append(t.right)
            result.append(r)
        return result
