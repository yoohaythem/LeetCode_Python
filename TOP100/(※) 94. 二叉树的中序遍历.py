# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def inorder(root, list):
            if root is None:
                return
            inorder(root.left, list)
            list.append(root.val)
            inorder(root.right, list)

            '''
            前序：
            list.append(root.val)
            inorder(root.left, list)
            inorder(root.right, list)
            
            后序：
            inorder(root.left, list)
            inorder(root.right, list)
            list.append(root.val)
            '''

        list = []
        inorder(root, list)
        return list

    def inorderTraversal2(self, root):
        result = []
        stack = []

        while root or len(stack) != 0:
            while root:
               stack.append(root)
               root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result


