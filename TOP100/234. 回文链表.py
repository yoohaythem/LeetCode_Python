# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = []
        while head:
            result.append(head.val)
            head = head.next
        n = len(result)
        for i in range(int(n / 2)):
            if result[i] - result[n - 1 - i]:
                return False
        return True

    def isPalindrome2(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        def reverse(node):
            pre = None
            curr = node
            while curr:
                next = curr.next
                curr.next = pre
                pre = curr
                curr = next
            return pre
        tail = reverse(slow)
        while head and tail:
            if head.val - tail.val:
                return False
            head = head.next
            tail = tail.next
        return True

