'''
class Solution(object):

    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        length = max(len(l1), len(l2))
        l = [0 for i in range(length + 1)]
        j = 0
        for i in range(length + 1):
            if i < min(len(l1), len(l2)):
                sum = l1[i] + l2[i] + j
                l[i] = sum % 10
                j = sum // 10
            elif len(l1) <= i < length:
                sum = l2[i] + j
                l[i] = sum % 10
                j = sum // 10
            elif len(l2) <= i < length:
                sum = l1[i] + j
                l[i] = sum % 10
                j = sum // 10
            else:
                if j == 1:
                    l[i] = j
                else:
                    l.pop()
        return l


if __name__ == '__main__':
    s = Solution()
    l1 = [9, 7, 7, 2, 3, 4]
    l2 = [8, 6, 4]
    print(s.addTwoNumbers1(l1, l2))
'''


class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        tail = None
        carry = 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            summary = n1 + n2 + carry
            if head is None:
                head = tail = ListNode(summary % 10)
            else:
                tail.next = ListNode(summary % 10)
                tail = tail.next
            carry = summary // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:  # 防止最高位进位出错
            tail.next = ListNode(carry)
        return head

if __name__ == '__main__':

    # 初始化链表 1
    head1 = temp = ListNode(2)
    temp.next = ListNode(4)
    temp = temp.next
    temp.next = ListNode(5)
    # 初始化链表 2
    head2 = temp = ListNode(5)
    temp.next = ListNode(6)
    temp = temp.next
    temp.next = ListNode(4)

    s = Solution()
    node = s.addTwoNumbers(head1, head2)
    while node:
        print(node.val)
        node = node.next