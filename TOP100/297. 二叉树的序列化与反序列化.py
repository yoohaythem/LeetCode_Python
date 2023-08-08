# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = ""
        queue = [root]
        while queue:
            temp = queue.pop(0)
            if temp:
                result += str(temp.val)
                queue.append(temp.left)
                queue.append(temp.right)
            else:
                result += "null"
            result += ","
        return result.rstrip(",")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree = data.split(",")
        if tree[0] == "null":
            return None
        root = TreeNode(int(tree[0]))
        queue = [root]
        i = 1
        while queue:
            temp = queue.pop(0)
            if not temp:
                continue
            temp.left = TreeNode(int(tree[i])) if tree[i] != "null" else None
            temp.right = TreeNode(int(tree[i + 1])) if tree[i + 1] != "null" else None
            queue.append(temp.left)
            queue.append(temp.right)
            i += 2
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
