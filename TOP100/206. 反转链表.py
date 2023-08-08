# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        tail = stack[-1] if stack else None
        while stack:
            tmp = stack.pop()
            tmp.next = stack[-1] if stack else None
        return tail

    # 最优
    def reverseList2(self, head):
        # pre = None
        # curr = head
        # while curr:
        #     next = curr.next
        #     curr.next = pre
        #     pre = curr
        #     curr = next
        # return pre
        pre, curr = None, head
        while curr:
            # pre, pre.next, curr = curr, pre, curr.next
            curr.next, pre, curr = pre, curr, curr.next
        return pre

    def reverseList3(self, head):
        if head is None or head.next is None:
            return head
        new = self.reverseList3(head.next)
        head.next.next = head
        head.next = None
        return new
