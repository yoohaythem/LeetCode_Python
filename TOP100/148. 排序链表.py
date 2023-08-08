# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = 0
        head_mem = head
        while head:
            n += 1
            head = head.next
        if n > 1:
            h = p = ListNode()
            left = right = head_mem
            for i in range(n // 2):
                if i == n // 2 - 1:
                    temp = right
                    right = right.next
                    temp.next = None
                else:
                    right = right.next
            l = self.sortList(left)
            r = self.sortList(right)
            while l and r:
                if l.val < r.val:
                    p.next = l
                    l = l.next
                else:
                    p.next = r
                    r = r.next
                p = p.next
            p.next = r if r else l
            return h.next
        else:
            return head_mem
