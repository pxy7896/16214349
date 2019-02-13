"""
Given a singly linked list, determine if it is a palindrome.
Could you do it in O(n) time and O(1) space?

使用两个指针，快的每次跳两步先跳到end，此时慢的正好在中间节点。如果fast先跳到None，则表明是偶数，此时
slow正好在后半段开始；如果fast.next先到None，则表明是奇数列，那slow要再走一步。然后比较。

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        return not rev
