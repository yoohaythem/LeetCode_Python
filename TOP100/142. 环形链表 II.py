# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = set()
        while head:
            if head in tmp:
                return head
            tmp.add(head)
            head = head.next
        return None

    def detectCycle2(self, head):
        slow = fast = flag = head
        if not head or not head.next:
            return None
        slow = slow.next
        fast = fast.next.next

        while slow != fast:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next

        while flag != slow:
            flag = flag.next
            slow = slow.next

        return flag
