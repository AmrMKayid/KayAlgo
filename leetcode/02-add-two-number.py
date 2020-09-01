# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

  def addTwoNumbers(self, l1, l2):
    """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    carry = 0
    result = head = ListNode(0)
    while l1 or l2 or carry:
      l1, v1 = [l1.next, l1.val] if l1 else [0, 0]
      l2, v2 = [l2.next, l2.val] if l2 else [0, 0]
      carry, num = divmod(v1 + v2 + carry, 10)
      head.next = ListNode(num)
      head = head.next
    return result.next
