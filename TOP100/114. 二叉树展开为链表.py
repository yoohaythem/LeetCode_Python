# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = []
        result = []
        while root or len(stack) != 0:
            while root:
                stack.append(root)
                result.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        for i in range(0, len(result) - 1):
            result[i].left = None
            result[i].right = result[i + 1]


    def flatten2(self, root):
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right


