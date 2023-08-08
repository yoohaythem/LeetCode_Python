# Definition for singly-linked list.
"""
    :type head: ListNode
    :type n: int
    :rtype: ListNode
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def removeNthFromEnd1(self, head, n):
        s = ListNode()
        s.next = head
        node = s
        length = 0

        while node.next:
            length += 1
            node = node.next

        node = s
        for i in range(length - n):
            node = node.next

        node.next = node.next.next if node.next.next else None

        return s.next

    def removeNthFromEnd2(self, head, n):
        s = ListNode()
        s.next = head
        left = right = s
        for i in range(n):
            right = right.next

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next if left.next.next else None

        return s.next
