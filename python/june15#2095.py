# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        sp = fp = head
        prev = None
        while fp and fp.next:
            prev = sp
            sp = sp.next
            fp = fp.next.next
        prev.next = sp.next
        return head
        