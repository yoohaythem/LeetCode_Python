"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        def find_deep(node):
            if not node:
                return 0
            m = 0
            for child in node.children:
                m = max(m, find_deep(child))
            return 1 + m

        return find_deep(root)

    def maxDepth2(self, root):
        stack = [root] if root else None
        deep = 0
        while stack:
            n = len(stack)
            for i in range(n):
                node = stack.pop(0)
                for child in node.children:
                    if child:
                        stack.append(child)
            deep += 1
        return deep

    '''
    if root is None:
        return 0
    ans = 0
    queue = [root]
    while queue:
        queue = [child for node in queue for child in node.children]
        ans += 1
    return ans
    '''