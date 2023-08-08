# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next

        while headB:
            if headB in s:
                return headB
            headB = headB.next

    def getIntersectionNode2(self, headA, headB):
        if not headA or not headB:
            return False
        pA = headA
        pB = headB
        '''
        while pA or pB:
            if not pA: pA = headB
            if not pB: pB = headA
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
        '''
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
