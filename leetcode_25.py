# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        count = 1
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        if not curr:
            return head
        nextHead = self.reverseKGroup(curr.next, k)
        curr.next = None
        newHead = self.reverseGroup(head)
        head.next = nextHead
        return newHead
    
    def reverseGroup(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev